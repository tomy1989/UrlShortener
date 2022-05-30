from django.urls import path
from . import views
#setting some urls
urlpatterns = [

        #route to create a new short link
        path('create', views.create_short),
        #route to use short link
        path('s/<str:code>', views.create_redirect, name='code')

]