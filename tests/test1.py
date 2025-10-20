

from datetime import date, timedelta

def checkio(d1: date, d2: date) -> int:
    # гарантія правильного порядку дат
    if d1 > d2:
        d1, d2 = d2, d1

    total_days = (d2 - d1).days + 1          # включно з обома межами
    full_weeks, rem = divmod(total_days, 7)  # повні тижні і залишок

    weekends = full_weeks * 2                # у кожному повному тижні 2 вихідних (сб, нд)

    # рахуємо вихідні в «хвості» (rem днів, починаючи з d1.weekday())
    start_wd = d1.weekday()                  # Пн=0, …, Сб=5, Нд=6
    for i in range(rem):
        wd = (start_wd + i) % 7
        if wd >= 5:                          # 5=Субота, 6=Неділя
            weekends += 1

    return weekends

assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2
assert checkio(date(2013, 1, 1),  date(2013, 2, 1))  == 8
assert checkio(date(2013, 2, 2),  date(2013, 2, 3))  == 2

print(checkio(date(2013, 1, 1), date(2013, 2, 1)))

            