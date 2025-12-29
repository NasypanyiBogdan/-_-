import math
def f(x):
    return x * (2**(2*x))

def F_exact(x):
    return (x * 2**(2*x)) / (2 * math.log(2)) - (2**(2*x)) / (4 * (math.log(2))**2)

def solve():
    a = 1.0  
    b = 2.0  
    n = 30   
    h = (b - a) / n
    
    sum_mid = 0
    for i in range(n):
        sum_mid += f(a + h/2 + i*h)
    res_mid = h * sum_mid
    
    sum_right = 0
    for i in range(1, n + 1):
        sum_right += f(a + i*h)
    res_right = h * sum_right
    
    sum_left = 0
    for i in range(n):
        sum_left += f(a + i*h)
    res_left = h * sum_left

    print(f"Результати для n={n}:")
    print(f"Метод середніх прямокутників: {res_mid:.6f}")
    print(f"Метод правих прямокутників:   {res_right:.6f}")
    print(f"Метод лівих прямокутників:    {res_left:.6f}")
    
    exact_val = F_exact(b) - F_exact(a)
    print(f"\nТочне значення (Ньютона-Лейбніца): {exact_val:.6f}")

solve()