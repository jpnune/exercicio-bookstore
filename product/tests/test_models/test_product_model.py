import pytest
from product.factories import ProductFactory, CategoryFactory


@pytest.mark.django_db
def test_create_product():
    category = CategoryFactory(title="Electronics")
    product = ProductFactory(title="Laptop", price=1500, active=True, category=[category])
    assert product.title == "Laptop"
    assert product.price == 1500
    assert product.active is True
    assert product.category.count() == 1
    assert product.category.first() == category
    assert str(product) == "Laptop"
