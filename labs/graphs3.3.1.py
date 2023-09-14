import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def graph(x, y, x_name, y_name, function='none'):
    aprox = 0
    if function == 'exp':
        model = np.poly1d(np.polyfit(x, np.log(y), deg = 1))
        aprox = f'{str(np.exp(model[0]))[:8]}*exp({str(model[1])[:8]}x)'

    if function == 'linear':
        model = np.poly1d(np.polyfit(x, y, deg = 1))
        aprox = f'{str(model[1])[:8]}x+({str(model[0])[:8]})'
        k = float(model[1])
        b = float(model[0])
        minx = min(x)
        maxx = max(x)
        v = [minx + i*(maxx - minx)/100 for i in range(1, 101)]
        u = [k*t + b for t in v]
        plt.plot(v, u, '--', color = 'orange', label = 'linear aproximation')

    if aprox:
        plt.plot(x, y, label = y_name + '(' + x_name +')' + f'\n aproximation: \n {aprox}', color = 'green')
    else:
        plt.plot(x, y, label = y_name + '(' + x_name +')', color = 'green')

    plt.grid()
    plt.title(y_name + '(' + x_name +')')
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    '''plt.xlim(min(x)*0.95, max(x)*1.05)
    plt.ylim(min(y)*0.95, max(y)*1.05)'''
    plt.show()
    '''plt.savefig(f'{y_name}({x_name}).png')'''

fileb = "3.3.1б.xlsx"
xlb = pd.ExcelFile(fileb)
df = xlb.parse("Лист1")

ua = [70, 80, 90, 100, 110]
ic1 = (df["Ic1, мА"].dropna()).tolist()
ia1 = (df["Ia1, мА"].dropna()).tolist()
ic2 = (df["Ic2, мА"].dropna()).tolist()
ia2 = (df["Ia2, мА"].dropna()).tolist()
ic3 = (df["Ic3, мА"].dropna()).tolist()
ia3 = (df["Ia3, мА"].dropna()).tolist()
ic4 = (df["Ic4, мА"].dropna()).tolist()
ia4 = (df["Ia4, мА"].dropna()).tolist()
ic5 = (df["Ic5, мА"].dropna()).tolist()
ia5 = (df["Ia5, мА"].dropna()).tolist()
ia = list()
ic = list()
ia = [ia1, ia2, ia3, ia4, ia5]
ic = [ic1, ic2, ic3, ic4, ic5]
B = [[round(ic[i][j]*2.8*10**(-2), 6) for j in range(len(ic[i]))] for i in range(len(ic))]

for i in range(len(B)):
    model = np.poly1d(np.polyfit(B[i], ia[i], 4))
    polyline = np.linspace(B[i][0], B[i][len(B[i]) - 1], 50)
    plt.scatter(B[i], ia[i], marker="+", color = "blue")
    plt.xlabel("B, мТл")
    plt.ylabel("Ia, мА")
    plt.title(f"График зависимости тока на аноде\nот напряженности магнитного поля соляноида\nпри напряжении на аноде {ua[i]}В")
    # plt.plot(polyline, model(polyline), color = "green", ls = "-")
    plt.plot(B[i], ia[i], color = "orange", ls = "--")
    plt.show()


