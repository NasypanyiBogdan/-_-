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
