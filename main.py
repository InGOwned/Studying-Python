import numpy as np
from scipy.stats import multivariate_normal

# Задача 1
matrix_text = \
'''3, 4, 17, -3
5, 11, -1, 6
0, 2, -5, 8'''

with open('matrix.txt', 'w') as f:
    f.write(matrix_text)

matrix = np.genfromtxt('matrix.txt', delimiter=',')

total_sum = np.sum(matrix)

max_element = np.max(matrix)

min_element = np.min(matrix)

# Задача 2
def rle(x):
    values = []
    counts = []
    current = x[0]
    count = 1
    for val in x[1:]:
        if val == current:
            count +=1
        else:
            values.append(current)
            counts.append(count)
            current = val
            count = 1
    values.append(current)
    counts.append(count)
    return (np.array(values), np.array(counts))

# Задача 3
data = np.random.normal(size=(10,4))
stats = {
    'min': np.min(data),
    'max': np.max(data),
    'mean': np.mean(data),
    'std': np.std(data)
}
first_five = data[:5]

# Задача 4
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zero_indices = np.where(x == 0)[0]

next_indices = zero_indices + 1

valid = next_indices < len(x)

elements_after_zero = x[next_indices[valid]]
max_after_zero = np.max(elements_after_zero)

# Задача 5
def log_pdf(X, m, C):
    D = C.shape[0]
    det = np.linalg.det(C)
    inv = np.linalg.inv(C)
    diff = X - m
    exponent = -0.5 * np.sum(diff @ inv * diff, axis=1)
    log_term = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det)
    return log_term + exponent

# Сравнение с scipy (пример)
m = np.array([0, 0])
C = np.array([[1, 0.5], [0.5, 1]])
X_sample = np.random.multivariate_normal(m, C, 10)
log_pdf_custom = log_pdf(X_sample, m, C)
log_pdf_scipy = multivariate_normal(m, C).logpdf(X_sample)

# Задача 6
a = np.arange(16).reshape(4,4)
a[[1,3]] = a[[3,1]]

# Задача 7
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
species = iris[:, -1]
unique_species, counts = np.unique(species, return_counts=True)

# Задача 8
arr = np.array([0,1,2,0,0,4,0,6,9])
nonzero_indices = np.nonzero(arr)[0]

# Вывод результатов
if __name__ == "__main__":
    print("Задача 1:")

    print(f"Сумма: {total_sum}, Максимум: {max_element}, Минимум: {min_element}")

    print("\nЗадача 2:", rle(np.array([2,2,2,3,3,3,5])))

    print("\nЗадача 3:", stats)

    print("\nЗадача 4:", max_after_zero)

    print("\nЗадача 6:\n", a)

    print("\nЗадача 7:", list(zip(unique_species, counts)))

    print("\nЗадача 8:", nonzero_indices)
