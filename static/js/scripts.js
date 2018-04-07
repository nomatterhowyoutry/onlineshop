$(document).ready(function(){
	var form = $('#form-buying-product');
	console.log(form);

	function cart_update(product_id, nmb, is_delete) {
		var data = {};
		data.product_id = product_id;
		data.quantity = nmb;

		if (is_delete) {
			data['is_delete'] = 'true';
		}

		// var csrf_token = $('#form-buying-product [name="csrfmiddlewaretoken"]').val();
		var csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
		console.log('session key:' + csrf_token);
		data["csrfmiddlewaretoken"] = csrf_token;
		var url = form.attr('action');
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function (data) {
				console.log('OK');
				if (data.products_total_quantity || data.products_total_quantity == 0){
					$('#products_total_quantity').text('('+data.products_total_quantity+')');
					console.log(data.products)
					$('.cart-items ul').html("");
					$.each(data.products, function(k, v){
						$('.cart-items ul').append(
							'<li>'+v.name +' * '+ v.quantity + ' = '+ v.total_price +' <a href="" class="delete-item" data-product_id="'+v.id+'">x</a></li>');
					});
				}
			},
			error: function () {
				console.log('error');
			}
		});
	};

	form.on('submit', function(e){
		e.preventDefault();
		var nmb = $('#number').val();
		var submit_btn = $('#submit-btn');
		var product_id = submit_btn.data('product_id');
		var product_name = submit_btn.data('product_name');
		var product_price = submit_btn.data('product_price');

		cart_update(product_id, nmb, is_delete=false);

	});

	$('.cart-container').on('mouseover', function(e){
		e.preventDefault();
		$('.cart-items').removeClass('hidden');
	});
	$('.cart-container').on('mouseout', function(e){
		e.preventDefault();
		$('.cart-items').addClass('hidden');
	});

	$(document).on('click', '.delete-item', function(e){
		e.preventDefault();
		product_id = $(this).data("product_id");
		nmb = 0;
		cart_update(product_id, nmb, is_delete=true);
	})

	function calculating_cart_price(){
		var total_order_price = 0;
		$('.total_product_price').each(function(){
			total_order_price += parseFloat($(this).text());
		});
		console.log(total_order_price);
		$('#total_order_price').text(total_order_price.toFixed(2));
	};

	$(document).on('change', '.product_in_cart_quantity', function(){
		var current_quantity = $(this).val();
		var current_row = $(this).closest('tr');
		var current_price = parseFloat(current_row.find('.product_in_cart_price_per_item').text()).toFixed(2);
		var total_price = parseFloat(current_quantity*current_price).toFixed(2);
		current_row.find('.total_product_price').text(total_price);

		calculating_cart_price();
	});

	calculating_cart_price();
});