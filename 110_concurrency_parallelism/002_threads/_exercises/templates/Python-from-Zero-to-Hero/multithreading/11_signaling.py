_______ random
_______ _
_______ t___
____ enum _______ Enum


c_ Event:
    ___  -
        __handlers = []

    ___ __call__( *args, **kwargs):
        ___ f __ __handlers:
            f(*args, **kwargs)

    ___ __iadd__( handler):
        __handlers.a..(handler)
        r_ self

    ___ __isub__( handler):
        __handlers.remove(handler)
        r_ self


c_ OperationStatus(Enum):
    FINISHED = 0
    FAULTED = 1


c_ Protocol:

    ___ __init__( port, ip_address):
        ip_address = ip_address
        port = port

        message_received = Event()

        set_ip_port()

    ___ set_ip_port(self):
        # calling 3rd party lib passing port and ip
        print('set ip and port once')
        t___.s(0.2)
        r_

    ___ send( op_code, param):
        ___ process_sending():
            print(f'Operation is in action with param={param}')
            result = process(op_code, param)
            message_received(result)

        t = _.T..(t.._process_sending)
        t.s..

    ___ process( op_code, param):
        print(f'processing operation={op_code} with param={param}')
        t___.s(3)

        # 3rd party lib response:
        finished = random.randint(0, 1) == 1
        r_ OperationStatus.FINISHED __ finished else OperationStatus.FAULTED



c_ BankTerminal:
    ___ __init__( port, ip_address):
        ip_address = ip_address
        port = port
        protocol = Protocol(port, ip_address)
        protocol.message_received += on_message_received

        operation_signal = _.Event()

    ___ on_message_received( status):
        print(f'Signaling for event:{status}')
        operation_signal.set()

    ___ purchase( amount):
        ___ process_purchase():
            purchase_op_code = 1
            protocol.send(purchase_op_code, amount)

            operation_signal.clear()
            print('\nWaiting for signal')
            operation_signal.wait()
            print('Purchase finished')

        t = _.T..(t.._process_purchase)
        t.s..

        r_ t


__ _____ __ _____
    bt = BankTerminal(10, '192.168.0.1')
    t = bt.purchase(20)
    print('Main decided to wait for purchase 1')
    t.j...
    t = bt.purchase(30)
    print('Main decided to wait for purchase 2')
    t.j...
    print('End of Main')
