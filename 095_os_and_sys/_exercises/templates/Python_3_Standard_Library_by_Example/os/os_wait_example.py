#!/usr/bin/env python3
"""Wait for a worker process.
"""

#end_pymotw_header
______ __
______ ___
______ ti__

___ i __ range(2):
    print('PARENT @: Forking @'.f..(__.g_p_, i))
    worker_pid _ __.f..
    __ no. worker_pid:
        print('WORKER @: Starting'.f..(i))
        ti__.sleep(2 + i)
        print('WORKER @: Finishing'.f..(i))
        ___.exit(i)

___ i __ range(2):
    print('PARENT: Waiting for @'.f..(i))
    done _ __.wait()
    print('PARENT: Child done:', done)
