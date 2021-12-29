___ handle_error_by_throwing_exception():
    raise Exception("Meaningful message describing the source of the error")


___ handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except ValueError:
        return None


___ handle_error_by_returning_tuple(input_data):
    try:
        return (True, int(input_data))
    except ValueError:
        return (False, None)


___ filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object as fobj:
        fobj.do_something()
