"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError("Number is less than or equal zero!")
    else:
        number = 2

        while len(list) < number_of_primes:
            check = False
            i = 2
            while i < number:
                if number % i == 0:
                    check = True
                    break
                i += 1
            if check == False:
                list.append(number)
            number +=1
        return list
