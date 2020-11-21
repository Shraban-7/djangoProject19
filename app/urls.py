from django.urls import path
from .views import Home,PostCreateView,PostList,PostDetail

urlpatterns = [

    path('',Home.as_view(),name = 'home'),
    path('create/',PostCreateView.as_view(),name = 'create'),
    path('list/',PostList.as_view(),name = 'list'),
    path('detail/<int:pk>',PostDetail.as_view(),name = 'detail'),
]