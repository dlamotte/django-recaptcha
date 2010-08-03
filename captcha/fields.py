from django.conf import settings
from django import forms
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

from captcha.widgets import ReCaptcha

from recaptcha.client import captcha

class ReCaptchaField(forms.CharField):
    default_error_messages = {
        'captcha_invalid': _(u'Incorrect, please try again.')
    }

    def __init__(self, *args, **kwargs):
        self.widget = ReCaptcha
        self.required = True
        super(ReCaptchaField, self).__init__(*args, **kwargs)
