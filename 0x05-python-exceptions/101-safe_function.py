#!/usr/bin/python3

def safe_function(function, *args):
    try:
        result = function(*args)
        return result
    except Exception as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return None
