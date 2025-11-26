#task_1.py

import math


class Point_18:
    """Клас моделює точку на координатній площині."""

    # Змінна класу — спільна для всіх створених об'єктів.
    # Використовується для підрахунку кількості екземплярів.
    count = 0

    def __init__(self, x=0.0, y=0.0):
        """
        Конструктор — викликається при створенні нового об'єкта.
        Встановлює координати x та y через сеттери.
        Також збільшує лічильник створених об'єктів.
        """
        self.x = x         # запис через setter (перевірка меж)
        self.y = y
        Point_18.count += 1  # збільшуємо лічильник об'єктів


    @property
    def x(self):
        """Повертає приховану змінну __x."""
        return self.__x

    @property
    def y(self):
        """Повертає приховану змінну __y."""
        return self.__y


    @x.setter
    def x(self, value):
        """
        Встановлює координату x.
        Якщо значення виходить за межі [-100, 100] — автоматично замінюється на 0.
        """
        if -100 <= value <= 100:
            self.__x = value
        else:
            self.__x = 0

    @y.setter
    def y(self, value):
        """
        Встановлює координату y.
        Те саме правило обмеження: дозволяються лише значення [-100; 100].
        """
        if -100 <= value <= 100:
            self.__y = value
        else:
            self.__y = 0


    def __del__(self):
        """
        Деструктор — викликається перед видаленням об'єкта.
        Зменшує лічильник об'єктів і виводить повідомлення.
        """
        Point_18.count -= 1
        print(f"Point_18 object deleted. Now count = {Point_18.count}")


    def move(self, dx, dy):
        """
        Змінює координати точки.
        dx — зміщення по осі X
        dy — зміщення по осі Y
        """
        self.x = self.x + dx
        self.y = self.y + dy

    def distance_to(self, other):
        """
        Обчислює відстань між двома точками за формулою:
            sqrt( (x1 - x2)^2 + (y1 - y2)^2 )
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        """
        Повертає текстове представлення об'єкта.
        Використовується при друку в списках, відладці тощо.
        """
        return f"Point_18({self.x}, {self.y})"

    @classmethod
    def get_count(cls):
        """Повертає кількість створених екземплярів класу."""
        return cls.count



def task_1():
    """Демонстрація роботи класу Point_18 (завдання 1)."""

    print("\n--- Завдання 1: Демонстрація класу Point_18 ---")

    # Створення трьох точок
    p1 = Point_18(10, 20)      # звичайні координати
    p2 = Point_18(-150, 5)     # x виходить за межі → буде замінено на 0
    p3 = Point_18(50, 50)      # коректні значення

    print("Створені точки:", p1, p2, p3)

    # Виведення кількості створених точок
    print("Кількість створених точок:", Point_18.get_count())

    # Перевірка геттерів
    print("Перевірка геттерів:", p1.x, p1.y)

    # Спроба присвоїти некоректне значення x
    print("Спроба встановити x = 150 (поза межами)")
    p1.x = 150
    print("Новий x:", p1.x)  # має стати 0

    # Демонстрація роботи move()
    print("Переміщаємо третю точку на (10, -20)")
    p3.move(10, -20)
    print("p3 після зміни:", p3)

    print("--- Кінець демонстрації завдання 1 ---")




# task_2.py

# Імпорт класу Point_18 з попереднього завдання
from task_1 import Point_18


def task_2():
    print("\n--- Завдання 2: Варіант 18 ---")

    # Створюємо список точок "до змін".
    # Кожен елемент — це окремий об’єкт Point_18 з відповідними координатами.
    points_before = [
        Point_18(10, 10),
        Point_18(-5, -20),
        Point_18(0, 0),
        Point_18(30, -7)
    ]

    # Створюємо список "після змін".
    points_after = [
        Point_18(p.x, p.y) for p in points_before
    ]

    # Виводимо початкові точки
    print("Початкові точки:", points_before)

    # Обчислюємо відстань між другою та четвертою точкою у списку points_after.
    # Індекси: 1 → друга точка, 3 → четверта.
    dist = points_after[1].distance_to(points_after[3])
    # Вивід відстані з округленням до трьох знаків після коми.
    print(f"Відстань між точками 2 і 4: {dist:.3f}")

    # Переміщаємо третю точку (індекс 2) на вектор (0, +47)
    # Тобто змінюється тільки координата y.
    points_after[2].move(0, 47)

    # Виводимо оновлені значення після переміщення
    print("Після зміни:", points_after)

    # Повертаємо обидва списки,
    # щоб інші частини програми могли використати їх
    return points_before, points_after



# task_3.py


import matplotlib.pyplot as plt

def task_3(before, after):
    """
    Малює точки до (before) і після (after) змін.
    - before, after: списки об'єктів Point_18 (або сумісних)
    """

    # Перевірка, чи передані списки точок.
    # Якщо даних немає — графік не будується.
    if before is None or after is None:
        print("Немає даних для побудови графіка.")
        return

    print("\n--- Завдання 3: Графік ---")

    # Витягуємо координати X і Y з початкових точок
    x_before = [p.x for p in before]
    y_before = [p.y for p in before]

    # Витягуємо координати X і Y зі змінених точок
    x_after = [p.x for p in after]
    y_after = [p.y for p in after]

    # Створюємо нову фігуру для графіка з розміром 8×6
    plt.figure(figsize=(8, 6))

    # Малюємо ламані лінії та точки "до змін"
    # marker='o' — точки круглі
    plt.plot(x_before, y_before, marker='o', linestyle='-', label="До змін")

    # Малюємо ламані лінії та точки "після змін"
    # marker='x' — точки хрестики
    plt.plot(x_after, y_after, marker='x', linestyle='-', label="Після змін")

    # Малюємо стрілки між відповідними точками "до" і "після"
    # Це дозволяє наочно побачити, як кожна точка перемістилася.
    # zip(before, after) автоматично обмежує ітерацію
    # до найкоротшого списку (захист від різної довжини).
    for b, a in zip(before, after):
        plt.annotate(
            '',                    # немає тексту
            xy=(a.x, a.y),         # координати нової точки
            xytext=(b.x, b.y),     # координати старої точки
            arrowprops=dict(arrowstyle='->', linewidth=0.8)
        )

    # Включаємо сітку для кращого візуального сприйняття координат
    plt.grid(True)

    # Додаємо легенду ("До змін", "Після змін")
    plt.legend()

    # Підписи осей
    plt.xlabel("X")
    plt.ylabel("Y")

    # Заголовок графіка
    plt.title("Положення точок до і після зміни координат (лінії + стрілки)")

    # Встановлюємо однаковий масштаб по обох осях,
    # щоб стрілки та переміщення не спотворювалися
    plt.axis('equal')

    # Відображаємо графік на екрані
    plt.show()



# task_4.py

def task_4(points, variant_number):
    print("\n--- Завдання 4: Запис у файл ---")

    # Визначаємо, чи є номер варіанта парним.
    # Якщо парний → формат запису один, якщо ні → інший.
    is_even = (variant_number % 2 == 0)

    # Відкриваємо файл task_4_output.txt у режимі запису.
    # encoding="utf-8" — щоб українські символи зберігалися правильно.
    with open("task_4_output.txt", "w", encoding="utf-8") as f:

        # enumerate дає пари (номер_елемента, сам_елемент)
        # start=1 → нумерація починається з 1, а не з 0
        for i, p in enumerate(points, start=1):

            # Якщо варіант парний — один формат
            if is_even:
                # Формат: (1) x: y
                f.write(f"({i}) {p.x}: {p.y}\n")

            # Якщо варіант непарний — інший формат
            else:
                # Формат: 1: x; y
                f.write(f"{i}: {p.x}; {p.y}\n")

    # Після виходу з with файл автоматично закриється
    print("Дані збережено у task_4_output.txt")



#script-file

from task_1 import task_1
from task_2 import task_2
from task_3 import task_3
from task_4 import task_4

points_before = None
points_after = None

while True:
    print("\n==============================")
    print("1 - Демонстрація класу Point_18 (Завдання 1)")
    print("2 - Виконати завдання 2 (Варіант 18)")
    print("3 - Показати графік точок (Завдання 3)")
    print("4 - Зберегти точки у файл (Завдання 4)")
    print("0 - Вийти")
    print("==============================")

    choice = input("Виберіть задачу (0–4): ")

    if choice == "1":
        task_1()

    elif choice == "2":
        points_before, points_after = task_2()

    elif choice == "3":
        if points_before is None or points_after is None:
            print("Спочатку виконайте завдання 2!")
        else:
            task_3(points_before, points_after)

    elif choice == "4":
        if points_after is None:
            print("Спочатку виконайте завдання 2!")
        else:
            task_4(points_after, 18)

    elif choice == "0":
        print("Вихід з програми...")
        break

    else:
        print("Невірний вибір.")
