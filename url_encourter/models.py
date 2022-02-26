import string
import random 
from django.utils import timezone
from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=255)
    token = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_expiracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def _generate_token(self):
        if self.token is None:
            size = random.randint(5, 10)
            chars = string.ascii_uppercase + string.digits
            self.token = ''.join(random.choice(chars) for _ in range(size)).lower()

    def save(self):
        self._generate_token()
        super().save()

    def check_expiration(self, now=timezone.now()):
        if self.data_expiracao and now > self.data_expiracao:
            self.ativo = False
            self.token = ''
            return super().save()
