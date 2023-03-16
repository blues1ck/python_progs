def nonlinear_equation(radioactivity, time, N, precision):
    '''ищет decay_time '''

    def f_val(radioactivity, time, N, decay_time):
        ''' вычисляет значение функции, нуль которой мы ищем '''
        f = 0
        for i in range(N):
            f += time[i] * math.exp(-time[i] / decay_time) * (radioactivity[i] - math.exp(-time[i] / decay_time))
        return f

    interval1 = float(input('угадаем корень от = '))
    interval2 = float(input('до = '))

    # решение нелинейного уравнения методом бисекции
    if f_val(radioactivity, time, N, interval1) == 0:
        return interval1
    elif f_val(radioactivity, time, N, interval2) == 0:
        return interval2
    else:
        x = 0
        while interval2 - interval1 > precision:
            x = interval1 + (interval2 - interval1)/ 2
            if f_val(radioactivity, time, N, interval2) * f_val(radioactivity, time, N, x) < 0:
                interval2 = x
            else:
                interval1 = x
    decay_time = x

    return decay_time