import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title('Анимация фигур Лиссажу')
ax.grid(True)
line, = ax.plot([], [], lw=2)

t = np.linspace(0, 2 * np.pi, 1000)

def animate(ratio):
    a = ratio
    b = 1
    x = np.sin(a * t)
    y = np.sin(b * t)
    line.set_data(x, y)
    ax.set_title(f'Соотношение частот: {a:.2f}:{b}')
    return line,

ani = FuncAnimation(
    fig, animate, 
    frames=np.linspace(0.1, 1, 100),
    interval=50, blit=True
)

plt.tight_layout()
plt.show()
