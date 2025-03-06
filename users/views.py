from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from .forms import CustomUserCreationForm
from .models import CustomUser


class UserLoginView(LoginView):
    model = CustomUser
    template_name = 'users/login.html'
    success_url = reverse_lazy('users:login')


class UserLogoutView(LogoutView):
    model = CustomUser
    # next_page = 'catalog:product_list'
    template_name = 'users/logout.html'
    success_url = reverse_lazy('catalog:product_list')


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/user_register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_email(user.email)
        return super().form_valid(form)

    def send_email(self, user_email):
        subject = 'Добро пожаловать в наш магазин'
        message = 'Спасибо, что зарегистрировались в нашем магазине!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)
