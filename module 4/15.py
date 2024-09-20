Can one block of except statements handle multiple exceptions?

try:
    # code that might raise an exception
except (TypeError, ValueError):
    # handle both TypeError and ValueError