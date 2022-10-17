from django.db import models

# Create your models here.
class test(models.Model):
    test = models.TextField()

class customer(models.Model):
    customer_no = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)

class wamessage_log(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    bot_id = models.CharField(max_length=200)
    message = models.TextField()
    customer_mess = models.BooleanField()#true for customer
    reply_id = models.CharField(max_length=200)
    message_status = models.CharField(max_length=200)#complete, on-going

class rec_numbers(models.Model):#recepients numbers
    number = models.BigIntegerField()