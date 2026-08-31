from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell me about your project or opportunity", "rows": 5}),
        }
