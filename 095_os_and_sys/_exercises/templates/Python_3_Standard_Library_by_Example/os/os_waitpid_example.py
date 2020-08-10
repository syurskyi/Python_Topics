#!/usr/bin/env python3
"""Wait for a worker process.
"""

#end_pymotw_header
______ __
______ ___
______ ti__

workers _ []
___ i __ range(2):
    print('PARENT @: Forking @'.f..(__.g_p_, i))
    worker_pid _ __.f..
    __ no. worker_pid:
        print('WORKER @: Starting'.f..(i))
        ti__.sleep(2 + i)
        print('WORKER @: Finishing'.f..(i))
        ___.exit(i)
    workers.append(worker_pid)

___ pid __ workers:
    print('PARENT: Waiting for @'.f..(pid))
    done _ __.waitpid(pid, 0)
    print('PARENT: Child done:', done)
