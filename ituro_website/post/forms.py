from django import forms
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(
        attrs={
            "class": "contact_textline",
	    "placeholder": _("Enter your email here.")
	}
    ), label=_("Sender Email"), required=True)
    subject = forms.CharField(widget=forms.TextInput(
	attrs={
	    "class": "contact_textline",
	    "placeholder": _("Enter your name here.")
	}
    ), label=_("Sender Name"), required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={
	    "class": "contact_textarea",
	    "placeholder": _("Enter your message here.")
	}
    ), label=_("Message"), required=True)
    captcha = CaptchaField()
