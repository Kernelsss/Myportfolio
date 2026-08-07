from django import forms
from .models import ContactMessage
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.ModelForm):
    if settings.USE_CAPTCHA:
        captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
        
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тема сообщения'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст сообщения', 'rows': 5}),
        }
        