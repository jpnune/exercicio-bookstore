import pytest
from product.factories import CategoryFactory
from product.serializers.product_serializer import ProductSerializer
from product.models import Product


@pytest.mark.django_db
def test_product_serializer_valid():
    category = CategoryFactory(title="Books")
    serializer_data = {
        "title": "Django Book",
        "description": "Learn Django fast",
        "price": 50,
        "active": True,
        "categories_id": [category.id],
    }
    serializer = ProductSerializer(data=serializer_data)
    assert serializer.is_valid() is True
    assert serializer.validated_data["title"] == "Django Book"
    assert serializer.validated_data["description"] == "Learn Django fast"
    assert serializer.validated_data["price"] == 50
    assert serializer.validated_data["active"] is True
    assert category in serializer.validated_data["categories_id"]


@pytest.mark.django_db
def test_product_serializer_create():
    category = CategoryFactory(title="Books")
    serializer_data = {
        "title": "Django Book",
        "description": "Learn Django fast",
        "price": 50,
        "active": True,
        "categories_id": [category.id],
    }
    serializer = ProductSerializer(data=serializer_data)
    assert serializer.is_valid() is True
    product = serializer.save()

    assert isinstance(product, Product)
    assert product.title == "Django Book"
    assert product.description == "Learn Django fast"
    assert product.price == 50
    assert product.active is True
    assert product.category.count() == 1
    assert product.category.first() == category
