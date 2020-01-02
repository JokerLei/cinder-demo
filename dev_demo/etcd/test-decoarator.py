#!/usr/bin/env python

import functools


class DecoratorTest(object):

    def __init__(self):
        super(DecoratorTest, self).__init__()

    def _decorator(func):
        @functools.wraps(func)
        def _handler(self, *args, **kargs):
            print("Hello World")
            return func(self, *args, **kargs)

        return _handler

    @_decorator
    def try_decorated_func(self):
        print("I am try decrorated func")


def _outside_decorator(func):
    @functools.wraps(func)
    def _handler(self, *args, **kargs):
        print("Hello World")
        return func(self, *args, **kargs)

    return _handler


class DecoratorOutside(object):

    def __init__(self):
        super(DecoratorOutside, self).__init__()

    @_outside_decorator
    def try_decorator_outisde(self):
        print("I am try decorator outside")


if __name__ == '__main__':
    obj = DecoratorTest()
    obj.try_decorated_func()

    obj2 = DecoratorOutside()
    obj2.try_decorator_outisde()
