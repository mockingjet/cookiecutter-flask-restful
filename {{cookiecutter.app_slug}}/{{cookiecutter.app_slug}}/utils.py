from functools import wraps


def print_exception(targeted_exception: Exception):
    """Decorate functions that will raise the targeted exception 
    and catch its error, print its error message

    :param targeted_exception: The targeted exception that you want to print
    :type exception: Exception
    """

    def decorator(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            try:
                fn(*args, **kwargs)
            except targeted_exception as e:
                print(str(e))
        return wrap
    return decorator


def wrap_response(api_version=0.0):
    """Wrap API response with API version and evelope data

    :param api_version: the api version, defaults to 0.0
    :type api_version: float, optional
    """

    def decorator(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            resp = fn(*args, **kwargs)
            return {
                "apiVersion": api_version,
                "data": resp
            }
        return wrap
    return decorator
