from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#from django.conf.urls import url
from example import views
from .views import HomePageView, AboutPageView, DataPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),    
    path('home/', HomePageView.as_view(), name='homepage'),    
    path('about/', AboutPageView.as_view(), name='about'),
    path('data/', DataPageView.as_view(), name='data'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
