___ handle_error_by_throwing_exception():
    raise Exception("Meaningful message describing the source of the error")


___ handle_error_by_returning_none(input_data):
    try:
        r.. int(input_data)
    except ValueError:
        r.. N..


___ handle_error_by_returning_tuple(input_data):
    try:
        r.. (True, int(input_data))
    except ValueError:
        r.. (False, N..)


___ filelike_objects_are_closed_on_exception(filelike_object):
    with filelike_object as fobj:
        fobj.do_something()
