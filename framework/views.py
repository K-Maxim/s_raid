from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from framework.models import FrameworkModel
from framework.serializers import FrameworkSerializer


class AddingData(CreateAPIView):
    """Заполнение базы"""
    serializer_class = FrameworkSerializer


class DataListView(ListAPIView):
    """Список всех языков и фреймворков"""
    serializer_class = FrameworkSerializer

    def get_queryset(self):
        return FrameworkModel.objects.all()


class DataView(ListAPIView):
    """Вывод данных в зависимости от фреймворка"""
    serializer_class = FrameworkSerializer
    lookup_field = ('language')

    def get_queryset(self):
        language = self.kwargs['language']
        return FrameworkModel.objects.filter(language__iexact=language)
