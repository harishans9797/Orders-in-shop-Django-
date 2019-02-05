from django.db import models



class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adress = models.CharField(max_length=300)
    email = models.CharField(max_length=300)



    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.first_name + ' ' + self.last_name







class Product(models.Model):
    description = models.CharField(max_length=1000)
    price = models.FloatField(default=0)
    brand = models.CharField(max_length=1000)
    quantity = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.description






class Order(models.Model):
    customer = models.ForeignKey(Customer,  related_name='customertoproduct', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  related_name='producttocustomer', on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return self.customer.__str__() + "  -  " + self.product.__str__()

    def __bool__(self):
        return self.paid






