from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Doc,Viewers,MyConsumer
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from django.utils import timezone
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required

"""
class SignupView(generic.CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    #success_url = reverse('login')
    def form_valid(self,request):
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
            return form
"""
def home_view(request):
    return render(request, 'index.html')


def Signupview(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                next_url = cache.get('next')
                if next_url:
                    cache.delete('next')
                    return HttpResponseRedirect(next_url)

                
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'presence_service/login.html', {})
        

class IndexView(generic.ListView):
    template_name = 'presence_service/index.html'
    context_object_name = 'doc_list'
    def get_queryset(self):
        return Doc.objects.order_by('-mod_date')

class DocDetailView(DetailView):
    #c = MyConsumer.objects.all()
    queryset = Doc.objects.all()
    def get_object(self):
        obj = super().get_object
        obj.last_accessed = timezone.now()
        #if obj returns viewers, modify here to include online
        obj.save()
        return obj

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.title, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'index.html', context)

def read(request, title):
    return HttpResponse("You're reading %s" % title)
"""
def detail(request, title):
    try:
        doc = Doc.objects.get(pk=title)
    except Doc.DoesNotExist:
        raise Http404("Doc does not exist")
    return render(request, 'presernce_service/detail.html', {'doc': title})
"""
