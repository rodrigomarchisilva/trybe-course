from decimal import Decimal

# Exercício 1: No terminal, inicialize duas variáveis a e b,
# sendo a = 10 e b = 5. Mostre o resultado das
# 7 operações básicas (soma, subtração, multiplicação, divisão,
# divisão inteira, potenciação e módulo) envolvendo essas variáveis.

a = 10
b = 5

operations = [
    a + b,
    a + b,
    a - b,
    a * b,
    a / b,
    a // b,
    a**b,
    a % b,
]

# Exercício 2: Declare e inicialize uma variável: hours = 6.
# Quantos minutos têm em 6 horas? E quantos segundos?
# Declare e inicialize variáveis minutes e seconds que
# recebem os respectivos resultados das contas. Depois, imprima cada uma delas.

hours = 6
minutes = 60 * hours
seconds = 60 * minutes

# Exercício 3: Teste e verifique o que acontece se você
# colocar um ponto e vírgula no final de uma instrução em Python.

numero_um = 1

# Exercício 4: Suponha que o preço de capa de um livro seja R$ 24,20,
# mas as livrarias recebem um desconto de 40%. O transporte custa 3,00
# para o primeiro exemplar e 75 centavos para cada exemplar adicional.
# Qual é o custo total de atacado para 60 cópias? Escreva uma expressão
# que receba o custo total e a imprima.

book_cover_cost = 24.2
first_shipment_cost = 3.0
additional_shipments_cost = 0.75
discounted_book_cover_cost = book_cover_cost * 0.6
book_cover_order_amount = 60
first_book_cover_cost = discounted_book_cover_cost + first_shipment_cost
additional_book_covers_cost = (
    book_cover_order_amount - 1
) * additional_shipments_cost

print(f"Additional book covers cost: {additional_book_covers_cost}")
print("First book cover cost:", {first_book_cover_cost})


def fill_decimals(splited_value):
    while len(splited_value) < 15:
        splited_value += "0"
    return int(splited_value)


def float_sum(values, precision, round_to):
    splited_values = list(map(lambda value: str(value).split("."), values))
    decimals = sum(
        list(map(lambda value: fill_decimals(value[1]), splited_values))
    )
    integers = sum(list(map(lambda value: int(value[0]), splited_values)))
    if decimals >= 10**precision:
        integers += decimals // 10**precision
        decimals = decimals % 10**precision
    decimals = float(f"{integers}.{decimals}")
    return f"{decimals:.{round_to}f}"


total_cost = float_sum(
    [first_book_cover_cost, additional_book_covers_cost], 15, 2
)

alternative_total_cost = Decimal(str(first_book_cover_cost)) + Decimal(
    str(additional_book_covers_cost)
)

if __name__ == "__main__":
    # Exercício 1
    print(f"Operations: {operations}")
    # Exercício 2
    print(f"Hours: {hours}\nMinutes: {minutes}\nSeconds: {seconds}")
    # Exercício 3
    print(numero_um)
    # Exercício 4
    print(f"Total cost: R$ {total_cost}")
    print(f"Alternative total cost: R$ {alternative_total_cost}")
