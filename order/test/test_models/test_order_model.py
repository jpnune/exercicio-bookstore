import pytest
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory
from order.models import Order

@pytest.mark.django_db
def test_create_order():
    user = UserFactory(username="customer1")
    product = ProductFactory(title="Book A", price=100)
    order = OrderFactory(user=user, product=[product])
    
    assert order.user == user
    assert order.product.count() == 1
    assert order.product.first() == product
