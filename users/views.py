from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            subject='Добро пожаловать в Skystore!',
            message='Вы успешно зарегистрировались.',
            from_email='noreply@skystore.local',
            recipient_list=[form.instance.email],
        )
        return response


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserLoginForm
