from django.urls import path
from .views import LoginWithFingerprintView

urlpatterns = [
    path('login/', LoginWithFingerprintView.as_view(), name='login'),
]