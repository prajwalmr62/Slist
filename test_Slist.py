from Slist import *

def list_Check(x):
    li = slist(x)
    return li

def test_answer():
    assert list_Check([1,3,2]) == [1,2,3]
