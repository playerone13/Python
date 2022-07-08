while True:
    days = 1
    start_km = float(input('начальный результат - '))
    target_km = float(input('финальный результат - '))
    if start_km <= 0 or target_km < 0:
        print('результат должен быть больше нуля! стартовое значение = 0')
    else:
        while start_km < target_km:
            start_km *= 1.1
            days += 1
        print(f'спортсмен добьетс результата за {days} дней')
