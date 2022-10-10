from django.urls import path
from django.conf.urls import url
from example import views
from .views import HomePageView, AboutPageView, DataPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),    
    path('home/', HomePageView.as_view(), name='homepage'),    
    path('about/', AboutPageView.as_view(), name='about'),
    url('data/', DataPageView.as_view(), name='data'),
]
