from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request, *arg, **kwargs):
        return render(request, 'index.html',{})
