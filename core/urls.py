from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('contact-us/',views.contact_us,name="contact_us"),
    path('about-us/',views.about_us,name="about_us"),
    path('allergy-advice/',views.allergy_advice,name='allergy_advice'),
    path('our-services/',views.our_services,name="our_services"),
    path('our-menu/',views.our_menu,name="our_menu"),
    
    
]