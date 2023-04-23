from django.contrib import admin
from .models import *

admin.site.site_header = "اپلیکیشن کوتاه کننده لینک"

admin.site.register(FullLink)
admin.site.register(ShortLink)