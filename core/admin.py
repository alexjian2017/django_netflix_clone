from django.contrib import admin
from .models import Profile,CustomUser,Movie,Videos

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Videos)


# Register your models here.
