import pytest

from framework.models import FrameworkModel
from framework.serializers import FrameworkSerializer
from tests.factories import FrameworkFactory


@pytest.mark.django_db
def test_framework_create(client):
    data = {
        "name": "name",
        "language": "language"
    }

    response = client.post(
        path='/create/',
        data=data
    )

    assert response.status_code == 201
    assert response.data["name"] == data["name"]
    assert response.data["language"] == data["language"]


@pytest.mark.django_db
def test_framework_list(client):
    frameworks = FrameworkFactory.create_batch(5)

    response = client.get(
        path="/frameworks/"
    )

    assert response.status_code == 200
    assert response.data == FrameworkSerializer(frameworks, many=True).data
    assert response.data != []
