from django.contrib import admin

# Register your models here.
from .models import contestant, youtubelink, contact

admin.site.register(contestant)
admin.site.register(youtubelink)
admin.site.register(contact)