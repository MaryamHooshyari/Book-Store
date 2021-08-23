from django.urls import path

from .views import SignUpView, login_redirect

urlpatterns = [
    path('login_redirect/', login_redirect, name='login_redirect'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
