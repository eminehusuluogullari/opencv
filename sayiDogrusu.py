import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Başlangıç parametrelerini tanımla
offset = 0  # Kaydırma başlangıç değeri
zoom_level = 10  # Başlangıç zoom seviyesi
step_size = 1  # İlk başta tam sayı adımları

# X ekseni değerlerini başlangıçta ayarla
x = np.arange(-zoom_level + offset, zoom_level + offset + step_size, step_size)
y = np.zeros_like(x)

# Grafik oluştur
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)
line, = ax.plot(x, y, 'bo', markersize=5)
ax.set_xlim(-zoom_level, zoom_level)
ax.set_ylim(-1, 1)
ax.set_xlabel("Sayı Doğrusu")
ax.set_yticks([])

# Kaydırma Slider'ı
ax_offset_slider = plt.axes([0.2, 0.15, 0.6, 0.03], facecolor="lightgoldenrodyellow")
offset_slider = Slider(ax_offset_slider, 'Kaydır', -100, 100, valinit=0)

# Zoom Slider'ı
ax_zoom_slider = plt.axes([0.2, 0.05, 0.6, 0.03], facecolor="lightblue")
zoom_slider = Slider(ax_zoom_slider, 'Zoom', 1, 50, valinit=zoom_level)

# Kaydırma Slider'ı güncelleme fonksiyonu
def update_offset(val):
    global offset
    offset = offset_slider.val
    new_x = np.arange(-zoom_level + offset, zoom_level + offset + step_size, step_size)
    line.set_xdata(new_x)
    ax.set_xlim(new_x[0], new_x[-1])
    fig.canvas.draw_idle()

# Zoom Slider'ı güncelleme fonksiyonu
def update_zoom(val):
    global zoom_level, step_size
    zoom_level = zoom_slider.val
    
    # Zoom seviyesine göre adım boyutunu küçült (daha fazla detay)
    if zoom_level <= 5:
        step_size = 0.1  # Yakınlaştırınca küçük adımlar
    elif zoom_level <= 10:
        step_size = 0.5
    else:
        step_size = 1  # Uzaklaştıkça tam sayılara geç
    
    new_x = np.arange(-zoom_level + offset, zoom_level + offset + step_size, step_size)
    line.set_xdata(new_x)
    ax.set_xlim(new_x[0], new_x[-1])
    fig.canvas.draw_idle()

# Slider olaylarını güncellemelerle ilişkilendir
offset_slider.on_changed(update_offset)
zoom_slider.on_changed(update_zoom)

plt.show()
