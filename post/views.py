from django.shortcuts import render
from rest_framework import serializers
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView

from .models import Post
from .forms import PostForm


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class PostLV(GenericAPIView, ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
