from django.db import models
import secrets

# Create your models here.

class test(models.Model):
    test = models.TextField()

class customer(models.Model):
    customer_no = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200, default='none')
    customer_email = models.CharField(max_length=100, default='none')
    customer_address = models.TextField(default='none')
    
    #def __str__(self):
    #    return f"name: {self.customer_name} email: {self.customer_email} no: {self.customer_no}"
    
class wamessage_log(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    bot_id = models.CharField(max_length=200)
    message = models.TextField()
    customer_mess = models.BooleanField()#true for customer
    reply_id = models.CharField(max_length=200)
    message_status = models.CharField(max_length=200)#complete, on-going
    
class product(models.Model):
    id = models.CharField(max_length=600, primary_key=True)# this represents the product UID
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=400)
    discountperc = models.IntegerField(default=0)

    def __str__(self):
        return f"UID:{self.id} Product name: {self.name}"

class cart(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    status = models.BooleanField(max_length=200, default= False)#still-buying = false, completed = true
    def __str__(self):
            return str(self.product)
            
class rec_numbers(models.Model):#recepients numbers
    number = models.BigIntegerField()

class payment(models.Model):
    id = models.CharField(max_length=200, primary_key=True, editable=False)#This will be used as the reference
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    items = models.TextField(default=None, editable=False)
    total_amount = models.PositiveIntegerField(blank=True, editable=False)
    payment_status = models.BooleanField(default=False)#if false payment hasnt been approved or completed by api
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_status = models.TextField(default='none')

    class Meta():
        ordering = ('-order_date',)
    
    def __str__(self)-> str: #adding a unique constraint
        return f"user: {self.customer} price: {self.total_amount} "
    
    def save(self, *args, **kwargs) -> None: #when creating reference, ensure that the refernce is unique
        while not self.id: #if the current object does not have a refernce, we create a reference
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = payment.objects.filter(id=ref)
            if not object_with_similar_ref == ref:
                self.id = ref
        cartitem = cart.objects.filter(customer = self.customer)
        self.items = str(cartitem)
        vals = []
        for price in cartitem:
            vals.append(int(price.product.price))
        self.total_amount = sum(vals)* 100
        cartitem.delete()

        super().save(*args, **kwargs)