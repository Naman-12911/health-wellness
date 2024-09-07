from django.db import models
from listing.models import Listing
from account.models import User
# Create your models here.




class Booking(models.Model):
    listing = models.ForeignKey(Listing,models.CASCADE)
    #payment_done = models.ForeignKey(payment,models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    name = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    email = models.CharField(max_length=100)
    # agreement = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "House Tour"  
        verbose_name_plural = "House tour"  


class payment(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    listing = models.ForeignKey(Listing,models.CASCADE)
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE,null=True,blank=True)
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    card_no = models.CharField(max_length=17,blank=True)
    month = models.CharField(max_length=5,blank=True)
    year = models.CharField(max_length=5,blank=True)
    name_on_card = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return f"amount {self.price}"
    
# class GetpaymentStatus(models.Model):
#     booking = models.ForeignKey(Booking)

class HelpTransportation(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    house_tour = models.ForeignKey(Booking,null=True,blank=True,on_delete=models.CASCADE)
    number_of_boxes = models.CharField(max_length=100)
    family_members = models.CharField(max_length=100)
    truck_required = models.CharField(max_length=100)
    def __str__(self):
        return self.family_members



class ContactUs(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    email = models.CharField(max_length=100,null=True,blank=True)
    query = models.TextField()
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.query
    
    class Meta:
        verbose_name = "Contact Us"  # Set the singular display name
        verbose_name_plural = "Contact Us"  # Set the plural display name
    

    



