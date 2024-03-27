from django.contrib import admin
from .models import Updates,Team,Contact,Product,ProductImages,Testimonial,Dealership,ProductFeature

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'image','position',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','number','message',)

@admin.register(Updates)
class UpdatesAdmin(admin.ModelAdmin):
    list_display = ('title','description',)
    prepopulated_fields = {"slug": ("title",)}

class ProductImageInline(admin.TabularInline):
    model = ProductImages
    fields = ("image",)
    extra = 1

class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    fields = ("feature",)
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    inlines = [ProductImageInline,ProductFeatureInline,]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display =('name','description','image','position',)

@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ("firm_name","full_name")

