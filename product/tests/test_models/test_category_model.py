import pytest
from product.factories import CategoryFactory


@pytest.fixture
def category_created():
    return CategoryFactory(title="pytest Category")


@pytest.mark.django_db
def test_create_category(category_created):
    assert category_created == "pytest Category"
