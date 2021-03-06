from django.views.generic.edit import CreateView

from accounts.forms import CustomUserCreationForm
from django import reverse_lazy
from .form import CustomUserCreationForm


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')