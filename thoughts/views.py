from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import ThoughtForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class CreateThought(LoginRequiredMixin, CreateView):
    form_class = ThoughtForm
    success_url = reverse_lazy('users:dashboard')

    def get_object(self, queryset=None):
        select_related =['thoughts']
        return self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

