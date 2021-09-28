from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns =[

    path('',views.homepage,name='home'),
    path('register/',views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('allhouses/',views.locations,name='locations'),
    path('newhouse/',views.new_neighbourhood, name='newhouse'),
    path('profile/',views.profile,name='profile'),
    path('connect/',views.bepartof_neighbourhood,name='connect'),
 ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)