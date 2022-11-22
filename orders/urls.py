from django.urls import path
from . import views

urlpatterns = [
    path('', views.orderCreateListView.as_view(), name='order_create_list' ),
    path('<int:order_id>/', views.orderDetailView.as_view(), name='order_detail' ),
    path('update-status/<int:order_id>/', views.orderUpdateStatusView.as_view(), name='order_status_update' ),
    path('user/<int:user_id>/orders/', views.UserOrderView.as_view(), name='user_orders' ),
    path('user/<int:user_id>/orders/<int:order_id>/', views.UserOrderDetailView.as_view(), name='user_order_detail' ),
]
