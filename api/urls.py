from django.urls import path, include

urlpatterns = [
    path('', include('v1.urls')),
]