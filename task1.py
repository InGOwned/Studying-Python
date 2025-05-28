import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre

x = np.linspace(-1, 1, 500)
degrees = range(1, 8)

plt.figure(figsize=(10, 6))
for n in degrees:
    y = eval_legendre(n, x)
    plt.plot(x, y, label=f'n = {n}')

plt.title('Полиномы Лежандра', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('P_n(x)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='best')
plt.tight_layout()
plt.show()
