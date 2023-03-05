import sys

"""
Sample temperature conversions:

import convert_temp
convert_temp.c2f(212)
Out[2]: 413.6
convert_temp.f2k(212)
Out[3]: 373.15
convert_temp.k2c(212)
Out[4]: -61.14999999999998
"""


def c2f(c):
    return (9/5) * c + 32


def c2k(c):
    return c + 273.15


def f2c(f):
    return (5/9) * (f - 32)


def f2k(f):
    return 273.15 + (5/9) * (f - 32)


def k2c(k):
    return k - 273.15


def k2f(k):
    return (9/5) * (k - 273.15) + 32


def test_conversion():
    try:
        assert round(c2f(f2c(123))) == 123
        assert round(k2c(c2k(123))) == 123
        assert round(k2f(f2k(123))) == 123
    except Exception:
        raise Exception("Conversions not converting properly.")

    return True


def user_interface():
    input_temp = None
    input_scale = None

    try:
        input_temp = float(sys.argv[1])
    except Exception:
        raise Exception("Temperature parameter must be an integer or float. Ex: 10 or 25.7 .")

    if len(str(sys.argv[2])) == 1 and str(sys.argv[2]) in ('C', 'F', 'K'):
        input_scale = str(sys.argv[2])
    else:
        raise Exception("Scale parameter must be C, F, or K.")

    if input_scale == 'C':
        print(c2f(input_temp), 'F', c2k(input_temp), 'K')
    elif input_scale == 'F':
        print(f2c(input_temp), 'C', f2k(input_temp), 'K')
    else:  # 'K'
        print(k2c(input_temp), 'C', k2f(input_temp), 'F')


if __name__ == '__main__':
    if sys.argv[1] == 'verify':
        print(test_conversion())
    elif len(sys.argv) == 3:
        user_interface()
