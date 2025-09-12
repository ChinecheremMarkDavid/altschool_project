def check_prime_numbers(num):
    number = int(num)
    condition = 0
    count = 2
    iteration = 0


# go throught a number of iterations where the iterations is less than or equal to our initial number


    while iteration <= number /2:
        if number % count == 0:
            condition =1
            break
        iteration += 1

    if condition == 0:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number ")


check_prime_numbers(35)