# genqueue.py
#
# Generate a sequence of items that put onto a queue

___ genfrom_queue(thequeue):
    w____ T..
        item = thequeue.get()
        __ item is StopIteration:
            break
        y... item

___ sendto_queue(items, thequeue):
    ___ item __ items:
        thequeue.put(item)
    thequeue.put(StopIteration)

# Example
__ __name__ __ '__main__':
    ______ queue, threading
    ___ consumer(q):
        ___ item __ genfrom_queue(q):
            print("Consumed", item)
        print("done")

    in_q = queue.Queue()
    con_thr = threading.Thread(target=consumer,args=(in_q,))
    con_thr.start()

    # Now, pipe a bunch of data into the queue
    sendto_queue(ra__(100), in_q)


