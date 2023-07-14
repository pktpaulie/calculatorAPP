import logging
from django.shortcuts import render
from .models import Computation
from .forms import CalculatorForm

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def index(request):
    """
    Renders the index.html template.

    :param request: The HTTP request object.
    :return: The rendered index.html template.
    """
    return render(request, "index.html")


def calculate(request):
    """
    Performs the calculation based on the user input and saves the computation.

    :param request: The HTTP request object.
    :return: The rendered index.html template with the calculation result and computations history.
    """
    answer = ""
    computations = Computation.objects.order_by("-id")[:5]

    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            first_number = request.POST.get("first_number")
            operand = request.POST.get("operation")
            second_number = request.POST.get("second_number")
            if operand == "+":
                answer = int(first_number) + int(second_number)
                logging.info("Using the addition logic of calculator Gp-3")
            elif operand == "-":
                answer = int(first_number) - int(second_number)
                logging.info("Using the subtraction logic of calculator Gp-3")
            elif operand == "/":
                try:
                    answer = int(first_number) / int(second_number)
                    logging.info("Using the division logic of calculator Gp-3")
                except ZeroDivisionError:
                    answer = "Error: Cannot divide by zero"
            elif operand == "*":
                answer = int(first_number) * int(second_number)
                logging.info("Using the multiply logic of calculator Gp-3")
            elif operand == "^":
                answer = int(first_number) ** int(second_number)
                logging.info("Using the modulus logic of calculator Gp-3")
            else:
                answer = "invalid operator"
            data = Computation(
                first_number=first_number,
                operation=operand,
                second_number=second_number,
                answer=answer,
            )
            data.save()

    return render(
        request, "index.html", {"answer": answer, "computations": computations}
    )


def read_history(request):
    """
    Retrieves the latest computations from the database and renders the index.html template.

    :param request: The HTTP request object.
    :return: The rendered index.html template with the computations history.
    """
    my_computations = Computation.objects.order_by("-id")[:5]
    return render(request, "index.html", {"computations": my_computations})
