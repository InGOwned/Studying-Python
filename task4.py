import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig = plt.figure(figsize=(10, 8))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.25, top=0.95, hspace=0.5)

# Сетка для графиков
ax1 = plt.subplot(311)  # Первая волна
ax2 = plt.subplot(312)  # Вторая волна
ax3 = plt.subplot(313)  # Результирующая волна

init_amp1 = 1.0
init_freq1 = 1.0
init_amp2 = 1.0
init_freq2 = 1.0

# Временная ось
t = np.linspace(0, 2, 1000)

wave1, = ax1.plot(t, init_amp1 * np.sin(2 * np.pi * init_freq1 * t), 'r-')
wave2, = ax2.plot(t, init_amp2 * np.sin(2 * np.pi * init_freq2 * t), 'g-')
result_wave, = ax3.plot(t, 
                        init_amp1 * np.sin(2 * np.pi * init_freq1 * t) + 
                        init_amp2 * np.sin(2 * np.pi * init_freq2 * t), 
                        'b-')

# Настройка оформления графиков
ax1.set_title('Волна 1: $A \cdot \sin(2\pi f t)$')
ax1.set_ylabel('Амплитуда')
ax1.set_ylim(-3, 3)
ax1.grid(True)

ax2.set_title('Волна 2: $A \cdot \sin(2\pi f t)$')
ax2.set_ylabel('Амплитуда')
ax2.set_ylim(-3, 3)
ax2.grid(True)

ax3.set_title('Результат сложения волн')
ax3.set_xlabel('Время (с)')
ax3.set_ylabel('Амплитуда')
ax3.set_ylim(-3, 3)
ax3.grid(True)

slider_ax1 = plt.axes([0.25, 0.15, 0.65, 0.03])
slider_ax2 = plt.axes([0.25, 0.10, 0.65, 0.03])
slider_ax3 = plt.axes([0.25, 0.05, 0.65, 0.03])
slider_ax4 = plt.axes([0.25, 0.00, 0.65, 0.03])

amp1_slider = Slider(slider_ax1, 'Амплитуда 1', 0.1, 2.0, valinit=init_amp1)
freq1_slider = Slider(slider_ax2, 'Частота 1 (Гц)', 0.5, 5.0, valinit=init_freq1)
amp2_slider = Slider(slider_ax3, 'Амплитуда 2', 0.1, 2.0, valinit=init_amp2)
freq2_slider = Slider(slider_ax4, 'Частота 2 (Гц)', 0.5, 5.0, valinit=init_freq2)

# Функция обновления графиков
def update(val):
    # Получаем текущие значения слайдеров
    amp1 = amp1_slider.val
    freq1 = freq1_slider.val
    amp2 = amp2_slider.val
    freq2 = freq2_slider.val
    
    # Обновляем данные волн
    wave1.set_ydata(amp1 * np.sin(2 * np.pi * freq1 * t))
    wave2.set_ydata(amp2 * np.sin(2 * np.pi * freq2 * t))
    result_wave.set_ydata(
        amp1 * np.sin(2 * np.pi * freq1 * t) + 
        amp2 * np.sin(2 * np.pi * freq2 * t)
    )
    
    fig.canvas.draw_idle()

# Обработчики изменений
amp1_slider.on_changed(update)
freq1_slider.on_changed(update)
amp2_slider.on_changed(update)
freq2_slider.on_changed(update)

plt.show()