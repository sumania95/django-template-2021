from django.urls import path,include

urlpatterns = [
    path('', include('application.page_dashboard.urls')),
    path('security/', include('application.page_security.urls')),

]
