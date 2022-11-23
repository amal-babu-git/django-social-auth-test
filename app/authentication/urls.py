from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',view=views.hello),
    # drf-social-auth
    re_path(r'^oauth/', include('drf_social_oauth2.urls', namespace='drf'))
    
]
