import pytest
from django.test import RequestFactory  # RequestFactory allows creating mock HTTP requests for testing views in Django
from  calculator_app.views import calculate 

# This decorator helps use Django database for testing. 
# to allows the test to access the database and perform database-related operations.
@pytest.mark.django_db
def test_calculate_view():
    factory = RequestFactory()
    request = factory.post('/calculate/', {'first_number': '5', 'operation': '+', 'second_number': '3'})
    response = calculate(request)

    assert response.status_code == 200
    # Assert verifies that the view correctly calculated the answer based on the provided form data, in context_data
    assert response.context_data['answer'] == 8
    # assert response.decode == '8'
