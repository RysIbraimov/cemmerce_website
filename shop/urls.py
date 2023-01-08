
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()
# router.register('category',CategoryViewSet)


urlpatterns = [
    path('category/',views.CategoryCreateListView.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryRetrieveUpdateDestroyApiView.as_view(), name='category_detail'),

    path('category/<int:pk>/item/',views.ItemCreateListApiView.as_view(), name='item'),
    path('category/<int:pk>/item/<int:id>/',views.ItemRetrieveUpdateDestroyApiView.as_view(), name='item_detail'),

    path('category/<int:pk>/item/<int:id>/order/',views.OrderCreateApiView.as_view(), name='order'),
    path('category/<int:pk>/item/<int:id>/order/<int:order_id>/',views.OrderRetrieveUpdateDestroyApiView.as_view(), name='order_detail'),
]