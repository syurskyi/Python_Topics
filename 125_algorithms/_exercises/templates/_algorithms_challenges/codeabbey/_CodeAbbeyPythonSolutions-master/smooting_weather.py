
___ smooth_weather(values
    result [0]*l.. v..
    result[0] values[0]
    result[-1] values[-1]

    ___ i __ r..(l.. v..-2
        smoothed_weather r..((values[i]+values[i+1]+values[i+2])/3, 7)
        result[i+1] smoothed_weather

    r.. ?

values l.. m..(f__, i.. ).s..()))
print(*smooth_weather(values