
___ smooth_weather(values):
    result = [0]*l..(values)
    result[0] = values[0]
    result[-1] = values[-1]

    ___ i __ r..(l..(values)-2):
        smoothed_weather = round((values[i]+values[i+1]+values[i+2])/3, 7)
        result[i+1] = smoothed_weather

    r.. result

values = l..(map(float, input().split()))
print(*smooth_weather(values))