from django.contrib import admin
from .models import(
					
					Technology,
					Domain,
					Video,
					Playlist,
					Course_link
					)
# Register your models here.

admin.site.register(Technology)

admin.site.register(Domain)

admin.site.register(Video)

admin.site.register(Playlist)

admin.site.register(Course_link)



