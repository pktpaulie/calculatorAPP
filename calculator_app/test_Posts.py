from django.test import TestCase
from django.urls import reverse

from .models import Computation
from .forms import CalculatorForm


class CalculateViewTest(TestCase):
    def setUp(self):
        self.url = reverse('calculate')

    def test_calculate_addition(self):
        form_data = {
            'first_number': '5',
            'operation': '-',
            'second_number': '3',
        }
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['answer'], 2)

        # Check if data is saved in the database
        computation = Computation.objects.last()
        self.assertEqual(computation.first_number, '5')
        self.assertEqual(computation.operation, '-')
        self.assertEqual(computation.second_number, '3')
        self.assertEqual(computation.answer, 2)

    # Add more test cases for other operations and edge cases

    def test_invalid_operator(self):
        form_data = {
            'first_number': '5',
            'operation': '&',
            'second_number': '3',
        }
        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['answer'], 'invalid operator')

        # Check that no data is saved in the database
        self.assertFalse(Computation.objects.exists())




class CalculatorFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'first_number': '5',
            'operation': '+',
            'second_number': '3',
        }
        form = CalculatorForm(data=form_data)
        self.assertTrue(form.is_valid())

