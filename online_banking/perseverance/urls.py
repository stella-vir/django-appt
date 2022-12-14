from django.urls import path

from . import views

app_name = 'perseverance'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:customer_id>/tranx/', views.tranx, name='tranx'),
    # path('<int:customer_id>/transaction/', views.transaction, name='transaction'),
    path('<int:pk>/account/', views.AccountView.as_view(), name='account'),
    path('<int:id>/del', views.delete, name='delete'),
    # path('transfer/', views.transfer, name='transfer'),
    path('transfer/', views.TransferView.as_view(), name='transfer'),
    path('cost/', views.cost, name='cost'),
]
