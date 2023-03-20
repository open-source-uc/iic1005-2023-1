def is_prime(number):
    "Verifica si el número es primo."
    prime = True
    for i in range(number):
        if i != 0:
            if number % i == 0:
                prime = False

    return prime


def find_prime_number(lower=0, upper=5_000):
    "Obtiene el primer número primo entre lower y upper."
    prime_number = -1
    for i in range(lower, upper):
        if is_prime(i):
            prime_number = i
    return prime_number


def find_first_n_prime_numbers(n: int):
    "Obtiene los primeros n números primos."
    prime_numbers = []
    last_prime_number = 1
    while len(prime_numbers) < n:
        prime_number = find_prime_number(last_prime_number + 1)
        last_prime_number = prime_number
        prime_numbers.append(prime_number)
    return prime_numbers


n = int(input("Cuántos números primos quieres? "))
print(find_first_n_prime_numbers(n))
