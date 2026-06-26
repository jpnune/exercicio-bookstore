import pytest
from order.factories import UserFactory
from product.factories import ProductFactory
from order.serializers.order_serializer import OrderSerializer
from order.models import Order


@pytest.mark.django_db
def test_order_serializer_valid():
    user = UserFactory(username="customer2")
    product1 = ProductFactory(title="Book 1", price=100)
    product2 = ProductFactory(title="Book 2", price=150)

    serializer_data = {"user": user.id, "products_id": [product1.id, product2.id]}

    serializer = OrderSerializer(data=serializer_data)
    assert serializer.is_valid() is True
    assert serializer.validated_data["user"] == user
    assert product1 in serializer.validated_data["products_id"]
    assert product2 in serializer.validated_data["products_id"]


@pytest.mark.django_db
def test_order_serializer_create_and_total():
    user = UserFactory(username="customer3")
    product1 = ProductFactory(title="Book 1", price=100)
    product2 = ProductFactory(title="Book 2", price=150)

    serializer_data = {"user": user.id, "products_id": [product1.id, product2.id]}

    serializer = OrderSerializer(data=serializer_data)
    assert serializer.is_valid() is True
    order = serializer.save()

    assert isinstance(order, Order)
    assert order.user == user
    assert order.product.count() == 2

    # Verify representation (includes total field)
    data = serializer.data
    assert data["total"] == 250
