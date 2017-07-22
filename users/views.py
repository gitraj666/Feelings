from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import  reverse
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
