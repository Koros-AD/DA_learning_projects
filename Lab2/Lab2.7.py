#7)  Операции с матрицами: Используя numpy, напишите сценарий, который создает матрицу и выполняет основные математические операции,
# такие как сложение, вычитание, умножение и транспонирование матрицы
import numpy as np
mtrx1 = np.array([[16, 8], [9, 7]])
mtrx2 = np.array([[5, 9], [20, 10]])

sum = mtrx1 + mtrx2
diff= mtrx1 - mtrx2
mult= mtrx1.dot(mtrx2)
transm1 = mtrx1.transpose()
transm2= mtrx2.transpose()

print(f'Matrix 1:{mtrx1}')
print(f"Matrix 2:{mtrx2}")
print(f"Sum of matrices:{sum}")
print(f"Difference of matrices:{diff}")
print(f"Multiplication of matrices:{mult}")
print(f"Transpose of matrix 1:{transm1}")
print(f"Transpose of matrix 1:{transm2}")
