
import contextlib
import time


@contextlib.contextmanager
def test_context():
    my_dict = {
        "a": 1,
        "b": 2
    }

    try:
        print "before..."
        yield my_dict
        print "end..."
    finally:
        print "Bye Bye"


if __name__ == "__main__":

    with test_context() as b:
        print b
        print "wait for 5 sec"
        time.sleep(5)
