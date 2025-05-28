import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

t = np.linspace(0, 4 * np.pi, 1000)

# Создание фигуры и осей
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid((3, 2), (0, 0))
ax2 = plt.subplot2grid((3, 2), (1, 0))
ax3 = plt.subplot2grid((3, 2), (2, 0), colspan=2)

# Настройка слайдеров
ax_amp1 = plt.axes([0.55, 0.75, 0.35, 0.03])
ax_freq1 = plt.axes([0.55, 0.70, 0.35, 0.03])
ax_amp2 = plt.axes([0.55, 0.55, 0.35, 0.03])
ax_freq2 = plt.axes([0.55, 0.50, 0.35, 0.03])

slider_amp1 = Slider(ax_amp1, 'Амплитуда 1', 0.1, 2.0, valinit=1)
slider_freq1 = Slider(ax_freq1, 'Частота 1', 0.5, 5.0, valinit=1)
slider_amp2 = Slider(ax_amp2, 'Амплитуда 2', 0.1, 2.0, valinit=1)
slider_freq2 = Slider(ax_freq2, 'Частота 2', 0.5, 5.0, valinit=1)

# Инициализация графиков
wave1, = ax1.plot(t, np.sin(t), 'r')
wave2, = ax2.plot(t, np.sin(t), 'g')
result, = ax3.plot(t, np.sin(t) + np.sin(t), 'b')

def update(val):
    amp1 = slider_amp1.val
    freq1 = slider_freq1.val
    amp2 = slider_amp2.val
    freq2 = slider_freq2.val
    
    y1 = amp1 * np.sin(freq1 * t)
    y2 = amp2 * np.sin(freq2 * t)
    
    wave1.set_ydata(y1)
    wave2.set_ydata(y2)
    result.set_ydata(y1 + y2)
    
    ax1.set_ylim(-amp1*1.2, amp1*1.2)
    ax2.set_ylim(-amp2*1.2, amp2*1.2)
    ax3.set_ylim(-(amp1+amp2)*1.2, (amp1+amp2)*1.2)
    
    fig.canvas.draw_idle()

slider_amp1.on_changed(update)
slider_freq1.on_changed(update)
slider_amp2.on_changed(update)
slider_freq2.on_changed(update)

ax1.set_title('Волна 1: $y = A_1 \cdot \sin(\omega_1 t)$')
ax2.set_title('Волна 2: $y = A_2 \cdot \sin(\omega_2 t)$')
ax3.set_title('Результат сложения: $y_1 + y_2$')
plt.tight_layout()
plt.show()
