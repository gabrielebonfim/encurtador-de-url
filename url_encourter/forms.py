from django.forms import ModelForm
from url_encourter.models import Url


class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['url', 'data_expiracao']
