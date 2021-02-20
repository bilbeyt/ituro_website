from django import forms
from django.utils.translation import ugettext_lazy as _

TEAM_TO_MESSAGES = [('Teknik Destek', 'Teknik Destek'), ('Sponsorluk', 'Sponsorluk')]

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
    send = forms.ChoiceField(
        required=False,
		widget=forms.Select(
		attrs={
        "class": "contact_textline",
        "placeholder": _("Enter your message here.")
    }
	),
        choices=TEAM_TO_MESSAGES,
    )


