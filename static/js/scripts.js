$(document).ready(function(){
	var form = $('#form-buying-product');
	console.log(form);
	form.on('submit', function(e){
		e.preventDefault();
		var nmb = $('#number').val();
		console.log(nmb);
		var submit_btn = $('#submit-btn');
		var product_id = submit_btn.data('product_id');
		var product_name = submit_btn.data('product_name');
		var product_price = submit_btn.data('product_price');
		console.log(product_id);
		console.log(product_name);
		console.log(product_price);

		var data = {};
		data.product_id = product_id;
		data.quantity = nmb;

		var csrf_token = $('#form-buying-product [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		var url = form.attr('action');
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function (data) {
				console.log('OK');
			},
			error: function () {
				console.log('error');
			}
		});

		$('.cart-items ul').append('<li>'+product_name +', '+ nmb + ', '+ product_price*nmb 
			+' <a class="delete-item" href="">x</a></li>');
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
		$(this).closest('li').remove();
	});
});