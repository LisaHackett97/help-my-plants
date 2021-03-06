""" User Profile Form """
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ User Profile form """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """Will add placeholders and classes, remove auto-generated
           labels and set autofocus on first field"""

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_email': 'Your Email',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-black profile-form-input')
            self.fields[field].label = False
