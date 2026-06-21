import pytest
from product.serializers.category_serializer import CategorySerializer

@pytest.mark.django_db
def test_category_serializer_valid():
    serializer_data = {
        "title": "Electronics",
        "slug": "electronics",
        "description": "Electronic items",
        "active": True
    }
    serializer = CategorySerializer(data=serializer_data)
    assert serializer.is_valid() is True
    assert serializer.validated_data["title"] == "Electronics"
    assert serializer.validated_data["slug"] == "electronics"
    assert serializer.validated_data["description"] == "Electronic items"
    assert serializer.validated_data["active"] is True

@pytest.mark.django_db
def test_category_serializer_invalid_missing_title():
    serializer_data = {
        "slug": "electronics"
    }
    serializer = CategorySerializer(data=serializer_data)
    assert serializer.is_valid() is False
    assert "title" in serializer.errors
