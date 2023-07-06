from django.test import TestCase
from .models import Computation


class PostTestCase(TestCase):
    def testPost(self):
        compute = Computation(first_number="Number 1", operation="operation", second_number="Number 2", answer="answer")
        self.assertEqual(compute.first_number, "Number 1")
        self.assertEqual(compute.operation, "operation")
        self.assertEqual(compute.second_number, "Number 2")
        self.assertEqual(compute.answer, "answer")
