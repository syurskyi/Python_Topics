# ch13/example2.py

______ th..

___ writer():
    g.. text
    g.. wcount

    w__ T..:
        w__ wcounter:
            wcount +_ 1
            __ wcount __ 1:
                read_try.a..

        w__ resource:
            print(f'Writing being done by {?.current_thread().name}.')
            text +_ f'Writing was done by {?.current_thread().name}. '

        w__ wcounter:
            wcount -_ 1
            __ wcount __ 0:
                read_try.release()

___ reader():
    g.. rcount

    w__ T..:
        w__ read_try:
            w__ rcounter:
                rcount +_ 1
                __ rcount __ 1:
                    resource.a..

            print(f'Reading being done by {?.current_thread().name}:')
            print(text)

            w__ rcounter:
                rcount -_ 1
                __ rcount __ 0:
                    resource.release()

text _ 'This is some text. '
wcount _ 0
rcount _ 0

wcounter _ ?.Lock()
rcounter _ ?.Lock()
resource _ ?.Lock()
read_try _ ?.Lock()

threads _ [?.T..(target_reader) ___ i __ ra..(3)] + [?.T..(target_writer) ___ i __ ra..(2)]

___ thread __ threads:
    thread.s..
