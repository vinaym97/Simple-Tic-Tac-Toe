prime_numbers = int(input())
# list_ = [ True for i in range(prime_numbers) if prime_numbers > 1 and prime_numbers % (i-1)  else False  ]
list_ = all([i for i in range(prime_numbers) True if prime_number > 1 and prime_number % (i-1) else False])