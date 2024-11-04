def is_perfect_number(n):
    if n <= 1:
        return false

    sum_of_divisors = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            sum_of_divisors += i
            if i !=1 and i !=n // i:
                sum_of_divisors += n // i

    return sum_of_divisors == n

# input
n = int(input())

# output
print(is_perfect_number(n))