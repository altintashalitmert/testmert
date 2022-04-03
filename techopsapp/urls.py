from django.urls import path
from . import views
from . views import Another


urlpatterns = [
    path('1', views.first),
    path('another', Another.as_view()),
]
