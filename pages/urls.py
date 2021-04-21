from django.urls import path
from .views import HomePageView, AboutPageView, Home2PageView, BlogPageView, BlogDetailsPageView, ContactPageView, UpdatesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home2', Home2PageView.as_view(), name='home2'),
    path('about', AboutPageView.as_view(), name='about'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('blog-details', BlogDetailsPageView.as_view(), name='blog-details'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('updates', UpdatesPageView.as_view(), name='updates')
]
