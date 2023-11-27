

from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="homepage"),
   path('about/', views.about, name="aboutpage"),
   path('contact/', views.contact, name="contactpage"),
   path('signup/', views.signup, name="signuppage"),
   path('eucc/', views.eucc, name="euccpage"),
   path('vac/', views.vac, name="vacpage"),
   path('debate/', views.debate, name="debatepage"),
   path('culture/', views.culture, name="culturepage"),
   path('bsec/', views.bsec, name="bsecpage"),
   path('member/', views.member, name="memberpage"),
   path('payment/', views.payment, name="paymentpage")
   
] 