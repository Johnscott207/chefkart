from django.urls import path

from .views import HomePageView, MyOrderList,ProductDetailView,AddCartView,OrderView
app_name = 'home'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('product/detail/<int:pk>/',ProductDetailView.as_view(),name='detail'),
    path('cart/',AddCartView.as_view(),name="cart"),
    path('order/',OrderView.as_view(),name="order"),
    path('myorder/',MyOrderList.as_view(),name="myorder"),
]