# ch13/example3.py

______ th..

___ writer():
    g.. text

    w__ T..:
        w__ service:
            resource.a..

        print(f'Writing being done by {?.current_thread().name}.')
        text +_ f'Writing was done by {?.current_thread().name}. '

        resource.release()

___ reader():
    g.. rcount

    w__ T..:
        w__ service:
            rcounter.a..
            rcount +_ 1
            __ rcount __ 1:
                resource.a..
        rcounter.release()

        print(f'Reading being done by {?.current_thread().name}:')
        #print(text)

        w__ rcounter:
            rcount -_ 1
            __ rcount __ 0:
                resource.release()

text _ 'This is some text. '
rcount _ 0

rcounter _ ?.Lock()
resource _ ?.Lock()
service _ ?.Lock()

threads _ [?.T..(target_reader) ___ i __ ra..(3)] + [?.T..(target_writer) ___ i __ ra..(2)]

___ thread __ threads:
    thread.s..
