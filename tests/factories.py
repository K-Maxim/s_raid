import factory.django

from framework.models import FrameworkModel


class FrameworkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FrameworkModel

    name = "test_name"
    language = "test_language"