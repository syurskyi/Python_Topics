___ handle_error_by_throwing_exception(
    raise Exception("Meaningful message describing the source of the error")


___ handle_error_by_returning_none(input_data
    try:
        r_ int(input_data)
    except ValueError:
        r_ None


___ handle_error_by_returning_tuple(input_data
    try:
        r_ (True, int(input_data))
    except ValueError:
        r_ (False, None)


___ filelike_objects_are_closed_on_exception(filelike_object
    with filelike_object as fobj:
        fobj.do_something()
