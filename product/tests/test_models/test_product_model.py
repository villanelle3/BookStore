import pytest
from product.factories import ProductFactory


@pytest.fixture
def product_created():
    return ProductFactory(title="pytest Product")


@pytest.mark.django_db
def test_create_category(category_created):
    assert category_created == "pytest Product"
