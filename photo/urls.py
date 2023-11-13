from django.urls import path
from .import views

# URLパターンを逆引きできるように名前付け
app_name = 'photo'

# URLを登録する変数
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('post/' , views.CreatePhotoView.as_view() , name = 'post'),#P446
    path('post_done/', views.PostSuccessView.as_view(), name= 'post_done'),

    path('photos/<int:category>', views.CategoryView.as_view(), name= 'photos_cat'), #475
    
    path('user-list/<int:user>', views.UserView.as_view(), name= 'user_list'), #482

    path('photo-detail/<int:pk>', views.DetailView.as_view(), name='photos_detail'),

    path('mypage/', views.MypageView.as_view(), name = 'mypage'),
    
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),#505




]