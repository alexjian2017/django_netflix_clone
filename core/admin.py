from django.contrib import admin
from .models import Profile,CustomUser,Movie,Videos

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_limit','uuid',)
    search_fields = ('name', )
    ordering = ('name', )

class MovieModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created','type','age_limit')
    search_fields = ('title', )
    ordering = ('title', )   
    
admin.site.register(CustomUser)
admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(Movie, MovieModelAdmin)
admin.site.register(Videos)
