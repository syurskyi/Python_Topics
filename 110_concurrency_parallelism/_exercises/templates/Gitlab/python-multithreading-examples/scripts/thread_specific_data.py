
______ random
______ _
______ logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

___ show_value(data):
    try:
        val = data.value
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)


___ worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

local_data = _.local()
show_value(local_data)
local_data.value = 1000
show_value(local_data)

___ i __ range(2):
    t = _.? ?_worker,  ?_(local_data,))
    t.s..
    
