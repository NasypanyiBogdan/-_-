import numpy as np

eps = 1e-3

x_old = np.array([0.0, 0.0, 0.0])

iteration = 0

print("Ітерація |    x1    |    x2    |    x3")
print("-----------------------------------------")

while True:
    iteration += 1

    x1 = (30.24 - 2.42 * x_old[1] - 3.85 * x_old[2]) / 24.51
    x2 = (40.47 - 2.31 * x_old[0] - 1.52 * x_old[2]) / 31.49
    x3 = (42.81 - 3.49 * x_old[0] - 4.84 * x_old[1]) / 29.02

    x_new = np.array([x1, x2, x3])

    print(f"{iteration:^8} | {x1:7.3f} | {x2:7.3f} | {x3:7.3f}")

    if np.max(np.abs(x_new - x_old)) < eps:
        break

    x_old = x_new

print("\nРозв’язок системи:")
print(f"x1 = {x_new[0]:.3f}")
print(f"x2 = {x_new[1]:.3f}")
print(f"x3 = {x_new[2]:.3f}")
print(f"Кількість ітерацій: {iteration}")
import numpy as np

def f1(x1, x2):
    return 4 * x1**2 + x2**2 - 4

def f2(x1, x2):
    return x1 - x2**2 + 2

def F(X):
    return np.array([f1(X[0], X[1]), f2(X[0], X[1])])

def get_jacobian_finite_diff(X, h=1e-5):
    """Обчислення матриці Якобі через скінченні різниці"""
    J = np.zeros((2, 2))
    fx = F(X)
    for j in range(len(X)):
        X_h = np.copy(X)
        X_h[j] += h
        J[:, j] = (F(X_h) - fx) / h
    return J

def gauss_inverse(matrix):
    """Пошук оберненої матриці методом Гаусса з вибором головного по рядку"""
    n = len(matrix)
    A = np.hstack((matrix, np.eye(n)))
    
    for i in range(n):
        max_row = i + np.argmax(np.abs(A[i:, i]))
        A[[i, max_row]] = A[[max_row, i]]
        
        A[i] = A[i] / A[i, i]
        
        for j in range(n):
            if i != j:
                A[j] -= A[j, i] * A[i]
                
    return A[:, n:]

def newton_method_system(X0, eps=1e-5, max_iter=50):
    X = np.array(X0, dtype=float)
    print(f"{'Ітерація':<10} | {'x1':<10} | {'x2':<10} | {'Невязка':<10}")
    print("-" * 50)
    
    for i in range(max_iter):
        fx = F(X)
        norm_f = np.linalg.norm(fx)
        print(f"{i:<10} | {X[0]:.6f} | {X[1]:.6f} | {norm_f:.6e}")
        
        if norm_f < eps:
            return X
        
        J = get_jacobian_finite_diff(X)
        J_inv = gauss_inverse(J)
        
        X = X - np.dot(J_inv, fx)
        
    return X

X0 = [1.5, -1.5]
result = newton_method_system(X0)

print("-" * 50)
print(f"Фінальний результат: x1 = {result[0]:.6f}, x2 = {result[1]:.6f}")