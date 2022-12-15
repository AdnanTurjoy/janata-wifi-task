from django.urls import path
from . import views
from .views import ItemList,itemCreate,itemUpdate,itemDelete, ItemDetail,UploadFileView

urlpatterns = [
   
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
    path('item-create/', views.itemCreate),
    path('item-update/<int:pk>/', views.itemUpdate,),
    path('item-delete/<int:pk>/', views.itemDelete,),
    path('upload/', UploadFileView.as_view())
]