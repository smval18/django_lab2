from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status, filters, viewsets, permissions
from django.core.exceptions import ValidationError

# Create your views here.


class AuthorViewSetReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSetReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__name', 'author__lastName', 'author__middle_name']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            if Book.objects.get(title=request.data['title']).publisher != request.data['publisher'] and request.data['caterogy'] == 'Художественное произведение, переведенное с другого языка':
                serializer.is_valid()
            if Book.objects.get(title=request.data['title']).yearofRel != request.data['yearofRel'] and request.data['category'] == 'Учебник':
                serializer.is_valid()
            else:
                raise ValidationError(self.errors)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



