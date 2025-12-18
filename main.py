import math

def f(x):
    return x**2 - math.cos(x)

def df(x):
    return 2*x + math.sin(x)

def newton_method(x0, eps=1e-6, max_iter=100):
    print("\n--- Метод Ньютона ---")
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            break
        x_new = x - fx / dfx
        print(f"Ітерація {i+1}: x = {x_new:.8f}")
        if abs(x_new - x) < eps:
            return x_new
        x = x_new
    return x

def chord_method(a, b, eps=1e-6, max_iter=100):
    print(f"\n--- Метод хорд на [{a}, {b}] ---")
    if f(a) * f(b) > 0:
        print("Помилка: на кінцях відрізка функція має однакові знаки.")
        return None
    
    x = a
    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        x_new = a - (fa * (b - a)) / (fb - fa)
        print(f"Ітерація {i+1}: x = {x_new:.8f}")
        
        if abs(x_new - x) < eps:
            return x_new
        
        if f(a) * f(x_new) < 0:
            b = x_new
        else:
            a = x_new
        x = x_new
    return x

def find_localization(start, end, step=0.1):
    print(f"\n--- Пошук ділянки локалізації на [{start}, {end}] ---")
    current = start
    while current + step <= end:
        if f(current) * f(current + step) <= 0:
            print(f"Знайдено відрізок: [{current:.2f}, {current+step:.2f}]")
            return current, current + step
        current += step
    return None, None

root_newton = newton_method(-2.5)

root_chord = chord_method(-2.5, 0)

a_loc, b_loc = find_localization(-2.5, 0)
if a_loc is not None:
    root_loc = chord_method(a_loc, b_loc)

print("\n" + "="*30)
print(f"Результат (Ньютон): {root_newton:.6f}")
print(f"Результат (Хорди):  {root_chord:.6f}")