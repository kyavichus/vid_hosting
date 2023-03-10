from django.urls import path, include
from . import views


urlpatterns = [
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('<int:pk>/', views.get_video, name='video'),
    path('', views.get_list_video, name='home'),
    path('vote/', views.get_list_video, name='vote'),
    path('rate/', views.rate_image, name='rate-view'),
    path('category/<str:slug>/', views.get_list_video_by_cat, name='category'),
    path('new/', views.VideoCreateView.as_view(), name='video_new'),
    path('update/<int:pk>/', views.VideoUpdateView.as_view(), name='video_update'),
    # path('login/', views.MyLoginView.as_view(), name='login_page'),
]
