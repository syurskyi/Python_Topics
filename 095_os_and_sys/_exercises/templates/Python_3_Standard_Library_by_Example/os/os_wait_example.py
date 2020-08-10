#!/usr/bin/env python3
"""Wait for a worker process.
"""

#end_pymotw_header
______ __
______ sys
______ time

___ i __ range(2):
    print('PARENT {}: Forking {}'.f..(__.getpid(), i))
    worker_pid = __.fork()
    __ not worker_pid:
        print('WORKER {}: Starting'.f..(i))
        time.sleep(2 + i)
        print('WORKER {}: Finishing'.f..(i))
        sys.exit(i)

___ i __ range(2):
    print('PARENT: Waiting for {}'.f..(i))
    done = __.wait()
    print('PARENT: Child done:', done)
