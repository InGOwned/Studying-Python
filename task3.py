import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

dates = []
passengers = []
with open('air_passengers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        dates.append(datetime.strptime(row[0], '%Y-%m'))
        passengers.append(int(row[1]))

# Линейный график за все время
plt.figure(figsize=(12, 6))
plt.plot(dates, passengers, 'b-')
plt.title('Пассажиропоток (1949-1960)')
plt.xlabel('Дата')
plt.ylabel('Количество пассажиров')
plt.grid(True)

plt.savefig('task3_1.png')

# Фильтрация данных за 1951-1955 годы
filtered_dates = []
filtered_passengers = []
for date, count in zip(dates, passengers):
    if 1951 <= date.year <= 1955:
        filtered_dates.append(date)
        filtered_passengers.append(count)

# Группировка
monthly_avg = [0] * 12
month_counts = [0] * 12
for date, count in zip(filtered_dates, filtered_passengers):
    month_idx = date.month - 1
    monthly_avg[month_idx] += count
    month_counts[month_idx] += 1

# Среднее знаение
for i in range(12):
    if month_counts[i] > 0:
        monthly_avg[i] /= month_counts[i]

# Гистограмма
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.figure(figsize=(10, 5))
plt.bar(months, monthly_avg, color='orange', alpha=0.7)
plt.title('Среднее количество пассажиров по месяцам (1951-1955)')
plt.xlabel('Месяц')
plt.ylabel('Количество пассажиров')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('task3_2.png')