import itertools


def foo(l):
    yield from itertools.product(*([l] * 102))


for x in foo('abcdefghijklmnopqrstuvxyz0123456789"!<>$*ùéè?./#~&}{()^:;.,[]@ç-_+¤$£µ§]°%ABCDEFGHIJKLMNOPQRSTUVWXYZ²'):
    print(''.join(x) + "\n")
