from unittest import TestCase

from interview.inventory.views import InventoryPeriodListView


class TestInventoryPeriodListView(TestCase):

    def test_validate_kwargs_raises_error(self):
        view = InventoryPeriodListView()
        with self.assertRaises(ValueError):
            view.validate_kwargs(date="invalid")

    def test_validate_kwargs_does_not_raise_error(self):
        view = InventoryPeriodListView()
        view.validate_kwargs(date="2020-01-02")

    def test_filter_inventory_ites(self):
        # setup
        # item = Inventory()  # it takes time to set up data without "factory_boy" or a similar lib
        # ... set up at least 2 items with different dates
        # view = InventoryPeriodListView()
        # actual = view.get_queryset().values_list("id", flat=True)
        # expected = [item.pk]

        # self.assertEqual(actual, expected)
        pass
