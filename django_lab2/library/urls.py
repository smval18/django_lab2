from django.urls import path, include
from .views import *


urlpatterns = [
    path('authors/', AuthorViewSetReadOnly.as_view({'get': 'list'})),
    path('author/<int:pk>', AuthorViewSetReadOnly.as_view({'get': 'retrieve'})),
    path('author/create/', AuthorViewSet.as_view({'post': 'create'})),
    path('books/', BookViewSetReadOnly.as_view({'get': 'list'})),
    path('book/<int:pk>', BookViewSetReadOnly.as_view({'get': 'retrieve'})),
    path('book/create/', BookViewSet.as_view({'post': 'create'}))
]
