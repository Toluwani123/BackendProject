from django.shortcuts import render, redirect
from django.views.generic.edit import *
from django.views.generic.list import ListView
# Create your views here.
from .form import *
from .models import Person
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
class CustomLogin(LoginView):
    template_name = 'person/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')

class Register(FormView):
    form_class = SignupForm
    template_name = 'person/index.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('registration')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Register, self).get(*args, **kwargs)

class Registration(CreateView):
    model = Person
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('home')
    template_name = 'person/register.html'
    context_object_name = 'registration'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Registration, self).form_valid(form)
    
def profile(request):
    details = Person.objects.filter(user=request.user)
    args = {'user': details}
    
    return render(request, 'person/home.html', args)