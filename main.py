import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.special import eval_legendre
from matplotlib.animation import FuncAnimation, PillowWriter
import matplotlib.gridspec as gridspec

# 1. Полиномы Лежандра
plt.figure(figsize=(10, 6))
x = np.linspace(-1, 1, 500)
for n in range(1, 8):
    plt.plot(x, eval_legendre(n, x), label=f'n = {n}')
plt.title('Полиномы Лежандра', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('P_n(x)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('legendre_polynomials.png', dpi=100)
plt.close()

# 2. Фигуры Лиссажу
plt.figure(figsize=(10, 8))
t = np.linspace(0, 2 * np.pi, 1000)
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]
for i, (a, b) in enumerate(ratios, 1):
    plt.subplot(2, 2, i)
    plt.plot(np.sin(a * t), np.sin(b * t), 'b')
    plt.title(f'Соотношение {a}:{b}')
    plt.axis('equal')
    plt.axis('off')
plt.tight_layout()
plt.savefig('lissajous_figures.png', dpi=100)
plt.close()

# 3. Анимация фигур Лиссажу
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Анимация фигур Лиссажу')
line, = ax.plot([], [], lw=2)
t = np.linspace(0, 4 * np.pi, 1000)

def animate(ratio):
    a = ratio
    b = 1
    x = np.sin(a * t)
    y = np.sin(b * t + np.pi/2)
    line.set_data(x, y)
    ax.set_title(f'Соотношение частот: {a:.2f}:{b}')
    return line,

ani = FuncAnimation(fig, animate, frames=np.linspace(0.1, 3, 60), 
                    interval=50, blit=True)
ani.save('lissajous_animation.gif', writer=PillowWriter(fps=15))
plt.close()

# 4. Сложение двух волн
t = np.linspace(0, 4 * np.pi, 500)
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 2, width_ratios=[1, 1], height_ratios=[1, 1, 2])

ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[1, 0])
ax3 = plt.subplot(gs[2, :])

# По умолчанию
amp1, freq1 = 1.0, 1.0
amp2, freq2 = 1.0, 2.0

y1 = amp1 * np.sin(freq1 * t)
y2 = amp2 * np.sin(freq2 * t)
y_sum = y1 + y2

ax1.plot(t, y1, 'r')
ax2.plot(t, y2, 'g')
ax3.plot(t, y_sum, 'b')

ax1.set_title(f'Волна 1: A={amp1}, ω={freq1}')
ax2.set_title(f'Волна 2: A={amp2}, ω={freq2}')
ax3.set_title('Результат сложения волн')
ax1.set_ylim(-2.5, 2.5)
ax2.set_ylim(-2.5, 2.5)
ax3.set_ylim(-3.5, 3.5)


plt.tight_layout()
plt.savefig('wave_addition.png', dpi=100)
plt.close()

# 5. 3D графики MSE
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
MSE = X**2 + Y**2

fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, MSE, cmap='viridis', alpha=0.8)
ax1.set_title('MSE в линейном масштабе')
ax1.set_xlabel('w0')
ax1.set_ylabel('w1')
ax1.set_zlabel('MSE')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, np.log10(MSE + 1e-10), cmap='plasma', alpha=0.8)
ax2.set_title('MSE в логарифмическом масштабе')
ax2.set_xlabel('w0')
ax2.set_ylabel('w1')
ax2.set_zlabel('log(MSE)')

plt.tight_layout()
plt.savefig('mse_plots.png', dpi=100)
plt.close()
