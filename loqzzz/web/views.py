from django.shortcuts import render
from .models import Updates,Team,Product,Testimonial
from django.http import JsonResponse
from .forms import ContactForm,DealershipForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    updates= Updates.objects.all()[:4]
    fablock_ace = Product.objects.filter(category="fablock_ace")
    smart_fablock_plus = Product.objects.filter(category="smart_fablock_plus")
    testimonials = Testimonial.objects.all()
    context={
        'updates'  : updates,
        'fablock_ace' : fablock_ace,
        'testimonials' : testimonials,
         "smart_fablock_plus" :  smart_fablock_plus,

    }
    return render(request ,'web/index.html',context)


def about(request):
    teams = Team.objects.all()
    context={
        'teams' : teams,
    }
    return render(request,'web/about.html',context)


def product(request):
    products=Product.objects.all()
    context={
        'products' : products,

    }
    return render(request,'web/product.html',context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
            return JsonResponse(response_data)
        else:
            print(form.errors)
            response_data = {"status": "false", "title": "Form validation error"}
            return JsonResponse(response_data)

    else:
        form = ContactForm() 
        context = {
            "is_contact": True,
            "form":form,
            }
    return render(request,"web/contact.html",context)


def updates(request):
    updates= Updates.objects.all()
    context={
        'updates': updates,
    }
    return render(request,"web/updates.html",context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    other_products = Product.objects.exclude(slug=slug)
    
    
    context ={
         'product': product,
         "other_products":other_products,
    }
    return render(request, "web/product-details.html",context)


def update_details(request,slug):
    updates = get_object_or_404(Updates, slug=slug)
    other_updates = Updates.objects.exclude(slug=slug)
    context = {
        "updates":updates,
        "other_updates":other_updates
    }
    return render(request,'web/updates-details.html',context)

def dealership(request):
    if request.method == "POST":
        form = DealershipForm(request.POST)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
            return JsonResponse(response_data)
        else:
            print(form.errors)
            response_data = {"status": "false", "title": "Form validation error"}
            return JsonResponse(response_data)
    else:
        initial_data = {'interest': 'dealership'}  # Define your initial data here
        form = DealershipForm(initial=initial_data) # Pass initial data to the form
            
        context = {
            "form": form,
        }
        return render(request, "web/dealership.html", context)
