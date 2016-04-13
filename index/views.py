from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from .models import Home
from .form import UserForm

class IndexView(generic.ListView):
    template_name = 'index/index.html'

    def get_queryset(self):
        return Home.objects.all()

class DetailView(generic.DetailView):
    model = Home
    template_name = 'index/detail.html'

class HomeCreate(CreateView):
    model = Home
    fields = ['street', 'city', 'price']

class HomeUpdate(UpdateView):
    model = Home
    fields = ['street', 'city', 'price']

class HomeDelete(DeleteView):
    model = Home
    success_url = reverse_lazy('index:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'index/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned(normalize) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user object if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_activ:
                    login(request, user)
                    return redirect('index:index')

        return render(request, self.template_name, {'form': form})




















'''
from django.shortcuts import render, get_object_or_404
from .models import Home

# Create your views here.

def index(request):
    all_homes = Home.objects.all()
    return render(request, 'index/index.html', {'all_homes': all_homes})

def detail(request, home_id):
    home = get_object_or_404(Home, pk=home_id)
    return render(request, 'index/detail.html', {'home': home})
'''
