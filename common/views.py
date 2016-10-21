from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserLogin(APIView):
    """
    User Login
    """
    result = {}

    @staticmethod
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except IntegrityError:
            return Http404


class UserRegister(APIView):
    """
    User Register
    """


class UserLogout(APIView):
    """
    User Logout
    """
