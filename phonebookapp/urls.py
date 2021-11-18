from .import views
from django.urls.resolvers import URLPattern
from django.urls import path

urlpatterns=[
    path('',views.data),
    path('add',views.addperson),
    path('dele',views.delete,name='dele'),
    path('del',views.erase),
    path('showcontact',views.displayContact),
    path('update',views.updations,name='update'),
    path('updatename',views.updateName),
    path('updatenumber',views.updateNumber)
    
    
    ]