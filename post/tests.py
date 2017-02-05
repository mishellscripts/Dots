from django.test import TestCase
from django.core.urlresolvers import reverse

import unittest
from . import models


# Create your tests here.

class LoginTestCase(TestCase):
    def setUp(self):
        pass

    def test_view_user_requires_login(self):
        resp = self.client.get(reverse("post:user_view"))
        self.assertNotEqual(resp.status_code, 200)
