#e)Моделирование простой анимации. Создать данные для x и y (где x это numpy.linspace, а y - математическая функция).
# Запустить объект line, ввести функцию animate(i) c методом line.set_ydata() и создать анимированный объект FuncAnimation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(0, 5, 200)
y = np.sin(x)
z=np.cos(x)
line, = ax.plot(x, y)
line2, = ax.plot(x,z)

def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    line2.set_ydata(np.cos(x + i / 10.0))
    return line,line2
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.title('График y = sin(x)')
plt.legend(['y = sin(x)'],['y=cos(x)'])
plt.show()
