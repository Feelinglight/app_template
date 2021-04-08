import traceback
import logging


def get_decorator(errors=(Exception, ), default_value=None, log_out_foo=print):
    def decorator(func):
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors:
                log_out_foo(traceback.format_exc())
                return default_value
        return new_func
    return decorator


on_exception_to_logging = get_decorator(log_out_foo=logging.critical)
on_exception_to_print = get_decorator(log_out_foo=print)
on_assertion_to_logging = get_decorator(errors=(AssertionError, ), log_out_foo=logging.critical)
