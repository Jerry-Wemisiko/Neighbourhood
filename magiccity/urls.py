from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns =[

    url(r'^',views.homepage,name='home'),
    url('register/',views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('allhouses/',views.locations,name='locations'),
    url('newhouse/',views.new_neighbourhood, name='newhouse'),
    url('profile/',views.profile,name='profile'),
    url('connect/<id>',views.bepartof_neighbourhood,name='connect'),
    url('viewneighbourhood/<id>',views.visit_neighbourhood,name='viewneighbourhood'),
    url('exitneighbourhood/<id>',views.exit_neighbourhood,name='exitneighbourhood')
 ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)