from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView,CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import  reverse,reverse_lazy
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def dashboard(request):
    return render(request,'users/dashboard.html')


class LogOutView(LoginRequiredMixin,FormView):
    template_name = 'users/logout.html'
    form_class = forms.LogOutForm

    def form_valid(self,form):
        logout(self.request)
        return HttpResponseRedirect(reverse('home'))

class  signUpView(CreateView):
    form_class = UserCreationForm
    template_name = "users/signUpVIew.html"
    success_url = reverse_lazy('users:dashboard')
