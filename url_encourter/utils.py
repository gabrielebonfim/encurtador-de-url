import imp
from url_encourter.models import Url


def get_url_by_token(token):
    token_search = Url.objects.filter(token=token, ativo=True)
    if token_search.exists():
        instance = Url.objects.get(token=token)
        instance.check_expiration()
        if instance.token:
            return instance.url