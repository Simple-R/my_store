from django.test import TestCase
import market.models


class TestValidModel(TestCase):

	def test_one_plus_one_equals_two(self):
		print("Method: test_one_plus_one_equals_two.")
		self.assertEqual(1 + 1, 2)

"""
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)"""


