
______ r__
______ _
______ logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

___ show_value(data):
    ___
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=@', val)


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
    
