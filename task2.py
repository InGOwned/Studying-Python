import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1  # Среднее и стандартное отклонение
data = np.random.normal(mu, sigma, 10000)

# Построение гистограммы
plt.figure(figsize=(10, 4))
plt.hist(data, bins=50, density=True, alpha=0.7, color='g')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.grid(True)
plt.savefig('task2.png')
