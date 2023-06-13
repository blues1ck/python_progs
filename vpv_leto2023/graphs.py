import pandas as pd
file = '232.xlsx'

s_kollectora = 23.6 * 10**(-4)
xl = pd.ExcelFile(file)
df = xl.parse('ртшники эксперимент после нас')
print(df)
timestr = (df['t.1'].tolist())[:-2]
time = [float(i) for i in timestr]
temperaturestr = (df['T1'].tolist())[:-2]
temperature = [float(i) for i in temperaturestr]
tokstr = (df['I, mkA'].tolist())[:-2]
tok_mkA = [float(i) for i in tokstr]
rev_tempstr = (df['100/T'].tolist())[:-2]
rev_temp = [float(i) for i in rev_tempstr]
lnI2str = (df['lnI^2'].tolist())[:-2]
lnI2 = [float(i) for i in lnI2str]
tok_emissii = 0.5
po_toka = [i/1000/s_kollectora for i in tok_mkA]

import matplotlib.pyplot as plt
import numpy as np

def graph(x, y, x_name, y_name, function):
    time = x
    tok_mkA = y
    if function == 'exp':
        model = np.poly1d(np.polyfit(time, np.log(tok_mkA), deg = 1))
        aprox = f'{str(np.exp(model[0]))[:8]}*exp({str(model[1])[:8]}x)'

    if function == 'linear':
        model = np.poly1d(np.polyfit(time, tok_mkA, deg = 1))
        aprox = f'{str(model[1])[:8]}x+({str(model[0])[:8]})'
        k = float(model[1])
        b = float(model[0])
        minx = min(time)
        maxx = max(time)
        v = [minx + i*(maxx - minx)/100 for i in range(1, 101)]
        u = [k*t + b for t in v]
        plt.plot(v, u, '--', color = 'orange', label = 'linear aproximation')

    plt.plot(time, tok_mkA, label = y_name + '(' + x_name +')' + f'\n aproximation: \n {aprox}', color = 'green')

    plt.grid()
    plt.title(y_name + '(' + x_name +')')
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.legend()
    '''plt.xlim(min(time)*0.95, max(time)*1.05)
    plt.ylim(min(tok_mkA)*0.95, max(tok_mkA)*1.05)'''
    plt.show()
    '''plt.savefig(f'{y_name}({x_name}).png')'''

graph(time, tok_mkA, 'время,с', 'ток,мкА', 'exp')
graph(temperature, tok_mkA, 'температура,C', 'ток,мкА', 'exp')
graph(rev_tempstr[:-2], lnI2[:-2], '100/T', 'ln(I^2)', 'linear')
graph(rev_temp[260:450], lnI2[260:450], '100/T', 'лучший участок ln(I^2)', 'linear')
graph(temperature, po_toka, 'температура', 'плотность тока', 'exp')
