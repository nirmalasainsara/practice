from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.http import HttpResponse
from .models import Todo
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework import generics
from django.utils.timezone import now
from datetime import timedelta


class TodoView(APIView):
    def get(self, request, *args, **kwargs):
        list = Todo.objects.all()
        serializer = TodoSerializer(list, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            create = serializer.save()
            serializer = TodoSerializer(create)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    lookup_url_kwarg = "id"
    queryset = Todo.objects.all()
