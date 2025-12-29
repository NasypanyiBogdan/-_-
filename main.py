import numpy as np

U_max = 100
f = 50
R1, R2, R3, R4 = 5, 4, 7, 2
L1 = 0.01
C1 = 300e-6
h = 0.00001 
t_end = 0.2  

def get_U1(t):
    """Вхідна синусоїдальна напруга """
    return U_max * np.sin(2 * np.pi * f * t)

def system_derivs(t, x):
    """Система диференціальних рівнянь для схеми №15 [cite: 493, 497-514]"""
    u_c1, i_l1 = x[0], x[1]
    u1 = get_U1(t)
    
    i1 = (u1 - u_c1 + i_l1 * R2) / (R1 + R2)
    u_node = u1 - u_c1 - i1 * R1
    
    du_c1 = i1 / C1
    di_l1 = (u_node - i_l1 * (R3 + R4)) / L1
    
    return np.array([du_c1, di_l1])

def solve():
    t = 0.0
    x = np.array([0.0, 0.0]) 
    
    print(f"{'Час (t)':<10} | {'U1 (Вхід)':<12} | {'U2 (Вихід)':<12}")
    print("-" * 42)

    step_count = 0
    
    while t <= t_end:
        f_n = system_derivs(t, x)
        x_predict = x + h * f_n
        
        f_next = system_derivs(t + h, x_predict)
        x = x + (h / 2) * (f_n + f_next)
        
        u2 = x[1] * R4
        
        if step_count % 500 == 0:
            u1 = get_U1(t)
            print(f"{t:<10.4f} | {u1:<12.4f} | {u2:<12.4f}")
        
        t += h
        step_count += 1

if __name__ == "__main__":
    solve()