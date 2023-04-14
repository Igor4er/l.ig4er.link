from django.db import models

protocols = (
    ('S', 'https://'),
    ('H')
)

class RedirectLink(models.Model):
    redirect = models.CharField(name='redirect', verbose_name='Звідки', max_length=6)
    to = models.URLField(name='to', verbose_name='Куди', max_length=254)

    def __str__(self) -> str:
        return f"{self.redirect} -> {self.to}"
