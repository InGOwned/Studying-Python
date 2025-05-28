import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Генерация данных
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
MSE = X**2 + Y**2  # Простая MSE функция

# Создание фигуры с двумя подграфиками
fig = plt.figure(figsize=(14, 6))

# Первый график (линейный масштаб)
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, MSE, cmap='viridis')
ax1.set_title('MSE в линейном масштабе')
ax1.set_xlabel('w0')
ax1.set_ylabel('w1')
ax1.set_zlabel('MSE')

# Второй график (логарифмический масштаб)
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X, Y, np.log10(MSE + 1e-10), cmap='plasma')
ax2.set_title('MSE в логарифмическом масштабе')
ax2.set_xlabel('w0')
ax2.set_ylabel('w1')
ax2.set_zlabel('log(MSE)')

plt.tight_layout()
plt.show()
