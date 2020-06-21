"""Пример использования модуля datetime

Модуль datetime содержит 5 основных типов:
datetime - для отображения даты и время сегодняшнего дня
date - отображает дату между 1 и 9999 годами
time - отображает время внезависимо от даты
timedelta - для отображения разницы между двумя объектами типа date или time
tzinfo - отображает информацию про часовой пояс
"""

import datetime

# Cоздаем объектf datetime
timestamp = datetime.datetime(2015, 7, 17, 12, 30, 45)
print(timestamp)

now = datetime.datetime.now()
print(now)
print (now.year, now.month, now.day)
print (now.hour, now.minute, now.second)
print (now.microsecond)

# Количество дней, прошедших с 01.01.1970
print(now.toordinal())
# Время в секундах с начала эпохи.
print(now.timestamp())
# День недели в виде числа, понедельник - 0, воскресенье - 6.
print(now.weekday())
# День недели в виде числа, понедельник - 1, воскресенье - 7.
print(now.isoweekday())
# Кортеж (year, week number, weekday).
print(now.isocalendar())
# Строка вида "YYYY-MM-DD HH:MM:SS.mmmmmm", если microsecond == 0, "YYYY-MM-DD HH:MM:SS".
# Параметр является разделителем между датой и временем
print(now.isoformat(' '))

day = datetime.date(2015, 7, 18)
for i in day.timetuple():
    # первые три числа в кортеже: год, месяц и число.  Последние 2 (не считая -1) -
    # день недели (понедельник - 0) и номер дня от начала года
    print(i)

print(day.isoformat())
print(day.strftime("%d/%m/%y"))
print(day.strftime("%A %d. %B %Y"))
print('{1} is {0:%d}, {2} is {0:%B}.'.format(day, "day", "month"))


class GMT2(datetime.tzinfo):
    """Описание часового пояса.

    Готовые классы можно установить в виде библиотеки pytz
    """

    def utcoffset(self, dt):
        """Разница во времени с UTC"""
        return datetime.timedelta(hours=2) + self.dst(dt)

    def dst(self, dt):
        """Корректировка с учётом летнего времени"""

        if not hasattr(dt, 'year'):
            return datetime.timedelta(0)

        d = datetime.datetime(dt.year, 4, 1)
        self.dston = d - datetime.timedelta(days=d.weekday() + 1)
        d = datetime.datetime(dt.year, 11, 1)
        self.dstoff = d - datetime.timedelta(days=d.weekday() + 1)
        
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return datetime.timedelta(hours=1)
        else:
            return datetime.timedelta(0)

    def tzname(self,dt):
        """Название часового пояса"""
        return "UTC +2"


time = datetime.time(12, 30, 45, tzinfo=GMT2())
print(time.tzname())
print(time.isoformat())
print(time.strftime("%H:%M:%S %Z"))


year = datetime.timedelta(days=365)
another_year = datetime.timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
print(year.total_seconds())
print(year == another_year)
ten_years = 10 * year
print(ten_years, ten_years.days // 365)

# Операции со временем
nine_years = ten_years - year
print(nine_years, nine_years.days // 365)
three_years = nine_years // 3;
print(three_years, three_years.days // 365)
print(abs(three_years - ten_years) == 2 * three_years + year)
