from django.urls import path
from collection import views

urlpatterns = [
    path('', views.api_root),
    path('collections/', views.CollectionList.as_view(), name="all-collections"),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name="collection-detail"),
    path('owner/<int:pk>/collections/', views.UserCollectionList.as_view(), name="owners-collections"),
    path('mycollections/', views.LoggedInCollectionList.as_view(), name="logged-in-collections"),
]