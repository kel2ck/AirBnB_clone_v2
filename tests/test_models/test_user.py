#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from datetime import datetime
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def setUp(self):
        """ """
        self.user_dict = {'email': 'test@example.com',
                          'password': 'password',
                          'first_name': 'John',
                          'last_name': 'Doe',
                          'created_at': datetime.now().isoformat(),
                          'updated_at': datetime.now().isoformat(),
                          '__class__': ""
                          }
    def test_first_name(self):
        """ """
        breakpoint()
        new = self.value(**self.user_dict)
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value(**self.user_dict)
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value(**self.user_dict)
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value(**self.user_dict)
        self.assertEqual(type(new.password), str)
