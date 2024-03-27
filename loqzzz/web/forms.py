from django import forms
from django.forms import widgets
from .models import Contact,Dealership


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "required", "placeholder": "Your Name *"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "required", "placeholder": "Your Email *"}
            ),
            "subject": widgets.TextInput(
                attrs={"class": "required", "placeholder": "Your Subject *"}
            ),
            "number": widgets.NumberInput(
                attrs={"class": "required", "placeholder": "Your Number *"}
            ),
            "message": widgets.Textarea(
                attrs={"class": "required contact-textarea", "placeholder": "Message", "cols": "40", "rows": "4"}
            ),
        }

class DealershipForm(forms.ModelForm):
    class Meta:
        model = Dealership
        exclude = ("timestamp",)
        widgets = {
            "firm_name": forms.TextInput(attrs={"class": "required", "placeholder": "Firm Name *"}),
            "full_name": forms.TextInput(attrs={"class": "required", "placeholder": "Full Name*"}),
            "email": forms.EmailInput(attrs={"class": "required", "placeholder": "Email *"}),
            "mobile": forms.NumberInput(attrs={"class": "required", "placeholder": "Mobile *"}),
            "address": forms.TextInput(attrs={"class": "required", "placeholder": "Address *"}),
            "pincode": forms.NumberInput(attrs={"class": "required", "placeholder": "Pincode *"}),
            "state": forms.TextInput(attrs={"class": "required", "placeholder": "State *"}),
            "city": forms.TextInput(attrs={"class": "required", "placeholder": "City *"}),
            "business": forms.TextInput(attrs={"class": "required", "placeholder": "Current Business *"}),
            "year_of_experience": forms.TextInput(attrs={"class": "required", "placeholder": "How Long In Business *"}),
            "brand_handled": forms.TextInput(attrs={"class": "required", "placeholder": "Brands Handled *"}),
            "annual_turnover": forms.TextInput(attrs={"class": "required", "placeholder": "Annual Turnover *"}),
            "interest": forms.Select(attrs={"class": "select-form"}),
            "why_loqz": forms.Textarea(attrs={"class": "required", "placeholder": "Reasons To Show Interest In Loqz Brand *"}),
            "whatsapp_number": forms.NumberInput(attrs={"class": "required", "placeholder": "Whatsapp number*"}),
        }