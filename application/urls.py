from django.urls import path,include
from .import views

from .views import (
    Home,
    Security_Page,
    Security_AJAXView,
)

urlpatterns = [
    path('', Home.as_view(), name = 'dashboard'),
    path('security/', Security_Page.as_view(), name = 'security'),
    path('api/security', Security_AJAXView.as_view(), name = 'api_security'),
]
