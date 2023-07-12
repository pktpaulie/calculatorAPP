# # importing the logging module to use
# import logging 

# logging.basicConfig(level=logging.DEBUG,
# 					format='%(asctime)s - %(levelname)s - %(message)s')


# def calculate1(value):
# 	if value < 0:
# 		raise ValueError("Invalid value: Value cannot be negative.")
# 	else:
# 		# Continue with normal execution
# 		logging.info("Operation performed successfully.")



# def calculate(request):
#     answer = ''
#     data = Computation.objects.all()

#     form = CalculatorForm(request.POST)
#     if request.method == "POST":
#         if form.is_valid():
#             first_number = request.POST.get("first_number")
#             operand = request.POST.get("operation")
#             second_number = request.POST.get("second_number")
#             if operand == "+":
#                 answer = int(first_number) + int(second_number)
#             elif operand == "-":
#                 answer = int(first_number) - int(second_number)
#                 logger.info("Subtraction numbers")
#             elif operand == "/":
#                 try:
#                     answer = int(first_number) / int(second_number)
#                     logger.info("Dividing numbers")
#                 except ZeroDivisionError:
#                     # refactoring with logger
#                     # answer = "Error: Cannot divide by zero"
#                     logger.warning("Division by zero is not allowed.")
#             elif operand == "*":
#                 answer = int(first_number) * int(second_number)
#             elif operand == "^":
#                 answer = int(first_number) ** int(second_number)
#             else:
#                 answer = "invalid operator"

# try:
# 	input_value = int(input("Enter a value: "))
# 	perform_operation(input_value)
# except ValueError as ve:
# 	logging.exception("Exception occurred: %s", str(ve))



# ####
import logging

# Set the logging configuration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='log1s.txt')

logger = logging.getLogger(__name__)

def calculate1(value):
    if value < 0:
        raise ValueError("Invalid value: Value cannot be negative.")
    else:
        # Continue with normal execution
        logging.info("Operation performed successfully.")


def calculate(request):
    answer = ''
    data = Computation.objects.all()

    form = CalculatorForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            first_number = request.POST.get("first_number")
            operand = request.POST.get("operation")
            second_number = request.POST.get("second_number")
            if operand == "+":
                answer = int(first_number) + int(second_number)
                logger.info("Addition numbers")
            elif operand == "-":
                answer = int(first_number) - int(second_number)
                logger.info("Subtraction numbers")
            elif operand == "/":
                try:
                    answer = int(first_number) / int(second_number)
                    logger.info("Dividing numbers")
                except ZeroDivisionError:
                    logger.warning("Division by zero is not allowed.")
            elif operand == "*":
                answer = int(first_number) * int(second_number)
                logger.info("Multiplication numbers")
            elif operand == "^":
                answer = int(first_number) ** int(second_number)
                logger.info("Exponentiation numbers")
            else:
                answer = "invalid operator"
