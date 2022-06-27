from . import strings
from . import _C


MIDDLE_LINE_CHAR = _C.MIDDLE_LINE_CHAR
BAR_SIZE = _C.BAR_SIZE
TOP_SQUARE_CHAR = _C.TOP_SQUARE_CHAR


def print_bar(char=MIDDLE_LINE_CHAR,
              N=BAR_SIZE,
              ):
    print(strings.get_bar(char, N))


def print_big_bar():
    print_bar(TOP_SQUARE_CHAR)


def null_print(x,
               flush=False,
               end='\n',
               ):
    pass


def full_print(x,
               flush=False,
               end='\n',
               ):
    print(x, flush=flush, end=end)


def print_red(txt,
              print_f=full_print,
              ):
    if txt is not None:
        print_f(strings.color_str(txt, 'red'))


def print_yellow(txt,
                 print_f=full_print,
                 ):
    if txt is not None:
        print_f(strings.color_str(txt, 'yellow'))


def print_blue(txt,
               print_f=full_print,
               ):
    if txt is not None:
        print_f(strings.color_str(txt, 'blue'))


def print_green(txt,
                print_f=full_print,
                ):
    if txt is not None:
        print_f(strings.color_str(txt, 'green'))
