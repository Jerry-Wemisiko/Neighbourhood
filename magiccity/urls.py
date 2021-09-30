from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns =[

    url(r'^$',views.homepage,name='homepage'),
    url('register/',views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('allhouses/',views.locations,name='locations'),
    url('newhouse/',views.new_neighbourhood, name='newhouse'),
    url('profile/',views.profile,name='profile'),
    path('connect/<id>',views.bepartof_neighbourhood,name='connect'),
    path('viewneighbourhood/<id>',views.visit_neighbourhood,name='viewneighbourhood'),
    path('exitneighbourhood/<id>',views.exit_neighbourhood,name='exitneighbourhood'),
    path('<hood_id>/post/', views.new_post, name='post'),
    url(r'^searched/', views.search_business, name='search'),

 ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)