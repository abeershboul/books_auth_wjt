from django.urls import path
from .views import BookDetailView,BookListCreateView
urlpatterns = [
    path('',BookListCreateView.as_view(),name='thing_list_create'),
    path('<int:pk>',BookDetailView.as_view(),name='thing_detail'),

]