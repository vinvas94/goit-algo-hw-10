import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
n_points = 10000  # Кількість випадкових точок для методу Монте-Карло

# Аналітичне обчислення з використанням функції quad
analytical_integral, error = quad(f, a, b)

# Метод Монте-Карло для обчислення інтегралу
random_x = np.random.uniform(a, b, n_points)  # Генеруємо випадкові точки x
random_y = f(random_x)  # Обчислюємо значення функції для цих точок

# Обчислення середнього значення функції на випадкових точках
average_value = np.mean(random_y)
monte_carlo_integral = (b - a) * average_value

# Створення діапазону значень для x
x = np.linspace(-2.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Виведення результатів
print(f"Аналітичне значення інтегралу (quad): {analytical_integral}")
print(f"Обчислений інтеграл методом Монте-Карло: {monte_carlo_integral}")
print(f"Абсолютна похибка між Монте-Карло і аналітичним значенням: {abs(analytical_integral - monte_carlo_integral)}")










