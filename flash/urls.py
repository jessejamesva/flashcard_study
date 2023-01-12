from django.urls import path
from .views import (
    CardListView, 
    CardDetailView, 
    CardCreateView,
    CardUpdateView,
    CardDeleteView,
    UserCardListView,
    UserSelectCardListView,
)
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [#from main urls file with 'flash/' removed (already processed)
    path('', views.home, name='flash-home'), #directs to views file for function(what to do)
    path('create/', CardCreateView.as_view(), name='flash-create'),
    #path('study/', CardListView.as_view(), name='flash-study'),
    path('flash/<int:pk>/', CardDetailView.as_view(), name='flash-detail'),
    path('flash/<int:pk>/update', CardUpdateView.as_view(), name='flash-update'),
    path('flash/<int:pk>/delete', CardDeleteView.as_view(), name='flash-delete'),
    path('study/user/<str:username>', UserCardListView.as_view(), name='flash-study1'),
    path('study/user/<str:username>/<str:subject>', UserSelectCardListView.as_view(), name='flash-study'),
]

urlpatterns += staticfiles_urlpatterns()
