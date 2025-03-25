sub_var = "sub_var"


def sub_func():
    print("sub_func")


class Sub:
    pass


__all__ = [
    "sub_var",
    "sub_func",
]  # Sub class는 "from 모듈 import *" 할때 포함되지 않도록 빼줌
