from django.test import TestCase
from .templatetags.milo_tags import bizzfuzz


class BizzfuzzTestCase(TestCase):
    def test_run(self):
        result = bizzfuzz(30)
        self.assertEquals("BizzFuzz", result)
        result = bizzfuzz(10)
        self.assertEquals("Fuzz", result)
        result = bizzfuzz(9)
        self.assertEquals("Bizz", result)
