import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

# Генерация временной оси
t = np.linspace(0, 2 * np.pi, 1000, endpoint=True)

# Создание прямоугольного сигнала (меандр)
signal = square(t)

# Построение графика
plt.figure(figsize=(10, 4))
plt.plot(t, signal)
plt.title('Прямоугольный сигнал (меандр)')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.ylim(-1.5, 1.5)
plt.grid(True)
plt.savefig('task1.png')
