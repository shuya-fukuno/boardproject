from django.urls import path

from boardapp.models import BoardModel
from .views import logoutfunc, signupfunc, loginfunc, listfunc, logoutfunc,\
     detailfunc, goodfunc, readfunc, BoardCreate, BoardUpdate, BoardDelete

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('update/<int:pk>', BoardUpdate.as_view(), name='update'),
    path('delete/<int:pk>', BoardDelete.as_view(), name='delete')
]
