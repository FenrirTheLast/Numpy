import numpy as np

# Zad.1
# tablica = np.arange(3, 3 * 15 + 1, 3)
#
# print(tablica)

# Zad.2
# lista_zmiennoprzecinkowa = [1.5, 2.8, 3.3, 4.7, 5.9]
# tablica_int64 = np.array(lista_zmiennoprzecinkowa, dtype=np.int64)
# print("Oryginalna lista zmiennoprzecinkowa:", lista_zmiennoprzecinkowa)
# print("Tablica przekonwertowana na int64:", tablica_int64)

# Zad.3
# def create_sequential_array(n):
#
#     sequential_array = np.arange(1, n * n + 1).reshape(n, n)
#     return sequential_array
#
# n = 4
# result = create_sequential_array(n)
# print(result)

# Zad.4
# def generate_powers(base, num_powers):
#
#     powers = np.logspace(0, num_powers - 1, num=num_powers, base=base, dtype=int)
#     return powers
#
# result = generate_powers(2, 4)
# print(result)

# Zad.5
# def generate_diagonal_matrix(length):
#
#     vector = np.arange(length, 0, -1)
#     diagonal_matrix = np.diag(vector)
#     return diagonal_matrix
#
# length = 5
# result = generate_diagonal_matrix(length)
# print(result)

# Zad.6
# def create_word_search(words):
#
#     assert len(words) == 3, "Należy podać dokładnie trzy słowa."
#
#     max_length = max(len(word) for word in words)
#
#     matrix = np.full((max_length, max_length), ' ', dtype='<U1')
#
#     for i, char in enumerate(words[0]):
#         matrix[i, 0] = char
#
#     for i, char in enumerate(words[1][::-1]):
#         matrix[0, i] = char
#
#     for i, char in enumerate(words[2]):
#         matrix[i, i] = char
#
#     return matrix
#
# words = ["RTG", "EEG", "EMG"]
# word_search_matrix = create_word_search(words)
#
# for row in word_search_matrix:
#     print(" ".join(row))

# Zad.7
# def generate_diagonal_matrix(n):
#
#     matrix = np.zeros((n, n), dtype=int)
#
#     for k in range(n):
#         value = 2 * (k + 1)
#         np.fill_diagonal(matrix[:, k:], value)
#         np.fill_diagonal(matrix[k:, :], value)
#
#     return matrix
#
# n = 3
# result = generate_diagonal_matrix(n)
# print(result)

# Zad.8
# def divide_array(array, kierunek):
#
#     if kierunek == 'pion':
#         if array.shape[1] % 2 != 0:
#             return "Ilość kolumn nie pozwala na operację podziału w pionie."
#         mid_col = array.shape[1] // 2
#         left_half = array[:, :mid_col]
#         right_half = array[:, mid_col:]
#         return left_half, right_half
#
#     elif kierunek == 'poziom':
#         if array.shape[0] % 2 != 0:
#             return "Ilość wierszy nie pozwala na operację podziału w poziomie."
#         mid_row = array.shape[0] // 2
#         top_half = array[:mid_row, :]
#         bottom_half = array[mid_row:, :]
#         return top_half, bottom_half
#
#     else:
#         return "Nieprawidłowy kierunek. Użyj 'pion' lub 'poziom'."
#
# array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#
# result_pion = divide_array(array, 'pion')
# print("Podział w pionie:")
# print(result_pion[0])
# print(result_pion[1])
#
# result_poziom = divide_array(array, 'poziom')
# print("Podział w poziomie:")
# print(result_poziom[0])
# print(result_poziom[1])

# Zad.9
def fibonacci_sequence(n):
    fib_seq = np.zeros(n, dtype=int)
    fib_seq[0] = 1
    if n > 1:
        fib_seq[1] = 1
        for i in range(2, n):
            fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2]
    return fib_seq


def create_fibonacci_matrix(size):
    num_elements = size * size

    fib_sequence = fibonacci_sequence(num_elements)

    fib_matrix = fib_sequence.reshape((size, size))

    return fib_matrix

result = create_fibonacci_matrix(5)
print(result)
