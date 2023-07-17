from django.urls import path
from .views import HomeViews, SnacksListViews, SnacksDetailsViews, SnacksCreateViews, SnacksUpdateViews,SnacksDeleteViews

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('snack/', SnacksListViews.as_view(), name='snacklist'),
    path('snack/<int:pk>/', SnacksDetailsViews.as_view(), name='details'),
    path('create/', SnacksCreateViews.as_view(), name='snack_create'),
    path('update/<int:pk>/', SnacksUpdateViews.as_view(), name='sna_updates'),
    path('delete/<int:pk>/', SnacksDeleteViews.as_view(), name='sna_delete'),

]
