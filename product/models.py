from datetime import date

from django.conf import settings
from django.db import models

from django.template.defaultfilters import floatformat

class Currency(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'

class ExchangeRate(models.Model):
    base = models.ForeignKey(Currency, related_name='base_currency', on_delete=models.CASCADE)
    quoted = models.ForeignKey(Currency, related_name='quoted_currency', on_delete=models.CASCADE)
    at = models.DateField('on date')
    value = models.DecimalField(max_digits=10, decimal_places=4, default=0)

    class Meta:
        verbose_name = 'quotation'
        verbose_name_plural = 'quotations'

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Products categories'

class SeoModel(models.Model):
    seo_title = models.CharField('Title', blank=True, max_length=250)
    seo_description = models.CharField('Description', blank=True, max_length=250)
    seo_keywords = models.CharField('Keywords', blank=True, max_length=250)

    def get_seo_title(self):
        if self.seo_title:
            return self.seo_title
        return self.name

    def get_seo_description(self):
        if self.seo_description:
            return self.seo_description
        return self.description

    def get_seo_keywords(self):
        if self.seo_keywords:
            return self.seo_keywords
        return ''

    class Meta:
        abstract = True

class Product(SeoModel):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    # _price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    in_stock = models.IntegerField(default=1, blank=False)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s, %s" % (self.name, self.id)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def price_at(self, at_date, for_currency):
        rate = (ExchangeRate.objects
                            .filter(base=self.product_price.currency,
                                    quoted=for_currency,
                                    at=at_date)
                            .first())
        price = self.product_price.value * rate.value
        return round(price, 2) if rate else 0

    @property
    def price(self):
        if not hasattr(self, '_price'):
            default = Currency.objects.get(name=settings.DISPLAY_CURRENCY)
            if self.product_price.currency == default:
                self._price = self.product_price.value
            else:
                self._price = self.price_at(date.today(), default)
        return self._price

class Product_price(models.Model):
    product = models.OneToOneField(Product, verbose_name='Product', on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, verbose_name='Currency', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '%s [%s] '.format(self.currency.name, self.id)

    class Meta:
        verbose_name = 'current price'
        verbose_name_plural = 'current prices'


class Product_image(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/media/products_images/')
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'