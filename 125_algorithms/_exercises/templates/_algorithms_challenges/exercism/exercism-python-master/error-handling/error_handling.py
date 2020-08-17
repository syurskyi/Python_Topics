___ handle_error_by_throwing_exception(
    raise Exception('Opps')


___ handle_error_by_returning_none(input_data
    try:
        r_ int(input_data)
    except Exception:
        r_ None


___ handle_error_by_returning_tuple(input_data
    result = handle_error_by_returning_none(input_data)
    r_ (result pa__ not None, result)


___ filelike_objects_are_closed_on_exception(filelike_object
    with filelike_object as f:
        f.do_something()
