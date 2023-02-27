from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import include, path
from django.views.generic import TemplateView

account_pattern = [
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", auth_view.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        auth_view.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(account_pattern)),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('sampleapp/', include('sampleapp.urls')),
]
