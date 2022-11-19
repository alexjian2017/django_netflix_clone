from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .form import ProfileForm
from .models import Profile,Movie

class Home(View):
    def get(self, request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:profile_list')
        return render(request, 'index.html',{})

def Test(request):
    return render(request, 'base.html') 

@method_decorator(login_required, name = 'dispatch')
class ProfileList(View):
    def get(self, request,*args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request,'profileList.html',{'profiles':profiles})

@method_decorator(login_required, name = 'dispatch')
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()

        return render(request,'profileCreate.html',{'form':form})
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('core:profile_list')
        return render(request,'profileCreate.html',{'form':form})

@method_decorator(login_required, name = 'dispatch')
class Watch(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid = profile_id)
            if profile.age_limit == 'Kids':
                movies = Movie.objects.filter(age_limit= profile.age_limit)
            else:
                movies = Movie.objects.all
            content = {'movies':movies}
            if profile not in request.user.profiles.all():
                return redirect('core:profile_list')
            return render(request, 'movieList.html',content)
        except Profile.DoesNotExist:
            return redirect('core:profile_list')

@method_decorator(login_required, name = 'dispatch')
class ShowMovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        print(movie_id)
        try:
            movie = Movie.objects.get(uuid=movie_id)
            content ={'movie':movie}
            return render(request,'movieDetail.html',content)
        except Movie.DoesNotExist:
            return redirect('core:profile_list')

@method_decorator(login_required, name = 'dispatch')
class ShowMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.videos.values()
            content={'movie':list(movie)}
            return render(request, 'showMovie.html', content)
        except Movie.DoesNotExist:
            return redirect('core:profile_list')

