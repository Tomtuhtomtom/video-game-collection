from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import CustomUser, Collection
from .serializers import CollectionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'collections/': reverse('all-collections', request=request, format=format),
    })


class CollectionList(generics.ListAPIView):
    queryset = Collection.objects.all().order_by('-name')
    serializer_class = CollectionSerializer
    permission_classes = []


class UserCollectionList(generics.ListCreateAPIView):
    queryset = Collection.objects.all().order_by('-name')
    serializer_class = CollectionSerializer
    permission_classes = []

    def get_queryset(self):
        owner = get_object_or_404(CustomUser, pk=self.kwargs['pk'])
        queryset = owner.collections.all().order_by('-name')
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LoggedInCollectionList(generics.ListCreateAPIView):
    queryset = Collection.objects.all().order_by('-name')
    serializer_class = CollectionSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = self.request.user.collections.all().order_by('-name')
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all().order_by('-name')
    serializer_class = CollectionSerializer
    permission_classes = []
