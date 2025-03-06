from django.urls import path
from users.views import RegisterView, UserLoginView, UserLogoutView

app_name = "users"

urlpatterns = [
    path(
        "login/", UserLoginView.as_view(template_name="users/login.html"), name="login"
    ),
    path(
        "logout/",
        UserLogoutView.as_view(http_method_names=["post", "get", "options"]),
        name="logout",
    ),
    path("user_register/", RegisterView.as_view(), name="user_register"),
]
