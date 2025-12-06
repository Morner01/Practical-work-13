def calculate_simple_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    return principal * rate * time / 100

def calculate_compound_interest(principal, rate, time, n=1):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Аргументы должны быть неотрицательными")
    if type(n) != int or n < 0:
        raise ValueError("n должно быть целым положительным числом")
    return principal * (1 + rate/(100*n))**(n*time)

def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Значение tax_rate не между 0 и 100")
    return amount * tax_rate / 100
