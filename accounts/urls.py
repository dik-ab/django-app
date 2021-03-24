from django.urls import path
from .views import UserLoginView, HomeView, SignUpView



app_name = 'accounts'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]


