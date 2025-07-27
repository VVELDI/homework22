from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        user_email = form.instance.email
        subject = 'Добро пожаловать в Skystore!'

        # HTML и текстовая версия письма
        html_message = render_to_string('users/welcome_email.html', {'user': form.instance})
        text_message = strip_tags(html_message)

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user_email]
        )
        email.attach_alternative(html_message, "text/html")
        email.send()

        return response


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm
