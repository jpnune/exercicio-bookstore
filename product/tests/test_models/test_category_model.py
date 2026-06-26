import pytest
from product.factories import CategoryFactory


@pytest.mark.django_db
def test_create_category():
    category = CategoryFactory(
        title="Books",
        slug="books",
        description="Book category description",
        active=True,
    )
    assert category.title == "Books"
    assert category.slug == "books"
    assert category.description == "Book category description"
    assert category.active is True
    assert category.__unicode__() == "Books"
