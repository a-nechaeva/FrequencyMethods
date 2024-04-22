import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import tf2zpk, lsim, freqs_zpk
import datetime


f_filter = lambda _tttt: tf2zpk([0, 1], [_tttt, 1])

def filter_quotes(T):
    date_array = np.array([])
    price_array = np.array([])
    file_path = 'SBER.csv'
    with open(file_path, 'r') as file:
        header = file.readline()
        for line in file:
            DATE, TIME, OPEN, HIGH, LOW, CLOSE, VOL = line.split(';')
            # convert date from ddmmyy to timestamp
            timestamp = datetime.datetime.strptime(DATE, '%d%m%y')
            date_array = np.append(date_array, timestamp)
            price_array = np.append(price_array, float(CLOSE))

    t_arr = np.linspace(0, len(price_array), len(price_array))
    plt.plot(t_arr, price_array, label='исходные данные файла', color='midnightblue')
    ff = f_filter(T)
    filtered_p = lsim(ff, price_array, t_arr, X0=price_array[0] * T)[1]

    plt.plot(date_array, filtered_p, label='фильтрованные данные', color='r')
    plt.grid()
    plt.xlabel('t')
    plt.ylabel('price')
    plt.legend()
    plt.title('График данных о стоимости акций')
    plt.show()

    #plot_func(t_arr, price_array, title=f'./results/third/{n}/source_quotes', caption='Source quotes of SBER')

    #filter = get_first_order_filter(T)
    #filtered_price = lsim(filter, price_array, t_arr, X0=price_array[0] * T)[1]
    #plot_func(date_array, filtered_price, title=f'./results/third/{n}/filtered_quotes', caption='Filtered quotes of SBER', labels=['Date', 'Price'])
    #cmp_func(date_array, funcs=[price_array, filtered_price], caption='Comparison of source and filtered quotes', title=f'./results/third/{n}/quotes_cmp', legend=['Source quotes', 'Filtered quotes'], labels=['Date', 'Price'])


filter_quotes(7)



