
______ r__
______ _
______ l__

l__.?(?_l__.D..
                    ?_ _threadName)-10s)  _ m.. _,
                    )

___ show_value(data):
    ___
        val = data.value
    except AttributeError:
        l__.d..('No value yet')
    else:
        l__.d..('value=@', val)


___ worker(data):
    show_value(data)
    data.value = r__.randint(1, 100)
    show_value(data)

local_data = _.local()
show_value(local_data)
local_data.value = 1000
show_value(local_data)

___ i __ r.. 2):
    t = _.? ?_worker,  ?_(local_data,))
    t.s..
    
