from django.urls import path
from real_estate.views import home_view, news_view, contact_view

urlpatterns = [
    path('', home_view, name='home'),
    path('news/', news_view, name='news'),
    path('contact/', contact_view, name='contact'),
]
