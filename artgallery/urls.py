from django.urls import path
# from artgallery.views import registerPage, loginPage, logoutUser
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(r'gallery/', views.gallery, name='gallery'),
    path('about_us/', views.aboutus, name='aboutus'),
    path('publications/', views.publications, name='publications'),
    # path('logout/', logoutUser, name='logout'),
    path(r'contact/', views.contact, name='contact'),
    path(r'shop/', views.shop, name='shop'),
    path(r'services/', views.services, name='services'),
    path(r'exhibitions/', views.exhibitions, name='exhibitions'),
    path(r'workshop/', views.workshop, name='workshop1'),
    path(r'gallery2/', views.gallery2, name= 'gallery2'),
]
