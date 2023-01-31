from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from framework.serializers import FrameworkSerializer


class AddingData(CreateAPIView):
    serializer_class = FrameworkSerializer
