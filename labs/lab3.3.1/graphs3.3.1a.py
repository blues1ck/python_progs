import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as mt

filea = "/home/ilya/Desktop/python_progs/labs/lab3.3.1/3_3_1a.xlsx"
xlb = pd.ExcelFile(filea)
df = xlb.parse("Лист1")

ua = 0.6
k = (8*mt.pi*mt.pi*ua)/(0.265**2)
SN = 0.3

Ik = (df["Ik"].dropna()).tolist()
Fk = (df["Фk"].dropna()).tolist()

Bk = [Fk[i]/SN for i in range(len(Fk))]

plt.scatter(Ik, Bk, color = "green", marker="+")
model = np.poly1d(np.polyfit(Ik, Bk, 1))
polyline = np.linspace(Ik[0], Ik[len(Ik) - 1], 50)
plt.xlabel("Ik, A")
plt.ylabel("Bk, мТл")
plt.plot(polyline, model(polyline), color = "blue", label = model, ls = '--')
plt.title("Калибровочная зависимость индукции\n\
          магнитного поля соленоида Bk, мВб\n\
          от Ik, А тока на нем")
plt.legend()
plt.show()

Bi = (df["I"].dropna()).tolist()
Bi = [i*4.14 for i in Bi]
n = (df["n"].dropna()).tolist()

plt.scatter(n, Bi, color = "green", marker="+")
model = np.poly1d(np.polyfit(n, Bi, 1))
polyline = np.linspace(n[0], n[len(n) - 1], 50)
plt.plot(polyline, model(polyline), color = "blue", label = model, ls = '--')
plt.xlabel("n, ед")
plt.ylabel("B, мТл")
plt.title("В(n)зависимость магнитной индукции\n на соленоиде от номера фокуса")
plt.legend()
plt.show()

print(Bi, n, sep = '\n')

result = 10**9 * k / (1.97**2)
print("{:.2e}".format(result))