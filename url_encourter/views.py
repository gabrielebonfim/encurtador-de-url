from email import message
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
from url_encourter.forms import UrlForm
from url_encourter.models import Url
from url_encourter.utils import get_url_by_token


def index(request):
    return render(request, 'index.html')


def load_url(request, token):
    url = get_url_by_token(token)
    if url:
        return redirect(url)
    else:
        return HttpResponse(status=404)


@require_POST
def new_url(request):
    form = UrlForm(request.POST)
    if form.is_valid():
        form.save()
        instance = Url.objects.all().last()
        url = f'{settings.HOST}/{instance.token}'
        messages.success(request, f'Url Encurtada: <a href="{url}" target="_blank">{url}</a>', extra_tags='alert-success')
    else:
        messages.error(request, 'Tente novamente', extra_tags='alert-danger')
    return redirect('index')

