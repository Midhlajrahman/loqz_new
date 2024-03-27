from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (('fablock_ace', 'Fablock Ace'),('smart_fablock_plus', 'Smart Fablock Plus'))
    title=models.CharField(max_length=200)
    sub_title=models.CharField(max_length=200)
    slug = models.SlugField(blank=True,null=True)
    description=models.TextField()
    main_image=models.ImageField(upload_to='products/')
    sub_image=models.ImageField(upload_to='products/')
    # is_fablock_ace = models.BooleanField(default = False)
    # is_smart_fablock_plus = models.BooleanField(default = False)
    category = models.CharField(max_length=128,choices=CATEGORY_CHOICES,blank=True,null=True)

    def get_image(self):
        return ProductImages.objects.filter(product=self)
    
    def get_feature(self):
        return ProductFeature.objects.filter(product=self)
    
    def get_absolute_url(self):
        return reverse("web:product_details", kwargs={"slug": self.slug})

  
    def __str__(self):
        return str(self.title)
    

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")
    

class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.CharField(max_length=200,blank=True,null=True)


class Updates(models.Model):
    image=models.ImageField(upload_to='updates/')
    detail_image=models.ImageField(upload_to='updates_/detail')
    title=models.CharField(max_length=50)
    date=models.DateField(blank=True,null=True)
    description= HTMLField()
    slug = models.SlugField(blank=True,null=True)

    def get_absolute_url(self):
        return reverse("web:update_details", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    

class Team(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='team/')
    position=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    number=models.IntegerField()
    message=models.TextField()

    def __str__(self):
        return self.name
    

class Testimonial(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='Testimonial/')
    description=models.TextField()
    position=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Dealership(models.Model):
    DEALERSHIP_CHOICES = (
        ('dealership', 'Dealership'),
        # Add other choices here if needed
    )
    firm_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.IntegerField()
    whatsapp_number=models.IntegerField(blank=True , null=True)
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    business = models.CharField(max_length=200)
    year_of_experience = models.CharField(max_length=150)
    brand_handled=models.CharField(max_length=200)
    annual_turnover=models.CharField(max_length=200)
    interest = models.CharField(max_length=100,choices=DEALERSHIP_CHOICES)
    why_loqz = models.TextField() 

    def __str__(self):
        return self.firm_name
    


    

