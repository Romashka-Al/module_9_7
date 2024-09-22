def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res < 2:
            print('Простое')
        else:
            for i in range(2, res):
                if res % i == 0:
                    print('Составное')
                    return res
            print('Простое')
        return res
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

result = sum_three(3, 3, 6)
print(result)
