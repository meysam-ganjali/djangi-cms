base_url = "http://localhost:8000/"
def format_currency(value):
    return "{:,.0f}".format(value) + 'تومان'

def generate_code(number: int):
    from random import randint
    number = int(number)
    return str(randint(10 ** (number - 1), 10 ** (number)))
