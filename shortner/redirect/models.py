from django.db import models
from django.conf import settings

# Create your models here.
class FullLink(models.Model):
    complete_link = models.CharField("لینک کامل", max_length=200, unique=True)

    def __str__(self):
        return self.complete_link
    
    class Meta:
        verbose_name = "لینک کامل"
        verbose_name_plural = "لینک های کامل"
    
class ShortLink(models.Model):
    full_link = models.ForeignKey(FullLink, verbose_name="لینک کامل" ,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="کاربر", on_delete=models.PROTECT)
    short_link = models.CharField("لینک کوتاه شده", max_length=20, unique=True)

    def __str__(self):
        return self.short_link
    
    class Meta:
        verbose_name = "لینک کوتاه"
        verbose_name_plural = "لینک های کوتاه"