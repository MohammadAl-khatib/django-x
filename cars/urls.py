from django.urls import path
from django.urls import path
from .views import Car_Listview, Car_Detailview, Car_Createview, Car_Updateview, Car_deleteview

urlpatterns = [
    path('', Car_Listview.as_view(), name = 'car_list'),
    path("<int:pk>", Car_Detailview.as_view(), name = 'car_detail'),
    path("create/", Car_Createview.as_view(), name = 'car_create'),
    path("<int:pk>/update/", Car_Updateview.as_view(), name = 'car_update'),
    path("<int:pk>/delete/", Car_deleteview.as_view(), name = 'car_delete')
]