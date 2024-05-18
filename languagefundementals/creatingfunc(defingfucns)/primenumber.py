def is_prime(num):
    for n in range(2, num):
      result =   f'{num} is a prime number' if num%n!=0 else f'{num} is not a prime number'
      return result

print(is_prime(14))