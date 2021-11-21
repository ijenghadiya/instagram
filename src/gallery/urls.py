from django.urls import path
from gallery import views

urlpatterns=[
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:id>/albums/', views.UserAlbumList.as_view()),
    path('albums/', views.AlbumList.as_view()),
    path('albums/<int:pk>', views.AlbumDetail.as_view()),
    path('images/', views.ImageList.as_view()),
    path('images/<int:pk>', views.ImageDetail.as_view()),
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>', views.TagDetail.as_view()),
    path('captions/', views.CaptionList.as_view()),
    path('captions/<int:pk>', views.CaptionDetail.as_view()),
]