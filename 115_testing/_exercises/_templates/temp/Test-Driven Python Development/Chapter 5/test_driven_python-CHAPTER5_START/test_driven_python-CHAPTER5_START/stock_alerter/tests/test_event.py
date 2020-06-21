_____ u__
____ u__ _____ mock

____ ..event _____ Event


c_ EventTest ?.?
    ___ test_a_listener_is_notified_when_an_event_is_raised
        listener = mock.Mock()
        event = Event()
        event.connect(listener)
        event.fire()
        aT..(listener.called)

    ___ test_a_listener_is_passed_right_parameters
        listener = mock.Mock()
        event = Event()
        event.connect(listener)
        event.fire(5, shape="square")
        listener.assert_has_calls([mock.call(5, shape="square")])
