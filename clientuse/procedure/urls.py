from django.urls import path

from procedure.views import *
urlpatterns=[
    path('',index,name='main'),
    path('clients/',show,name='show'),
    path('update/',up,name='update'),
    path('submitdt/',send,name='send')
]