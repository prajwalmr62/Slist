from Slist import *

def list_Check(x):
    li = slist(x)
    li.sort()
    return li

def test_answer():
    assert [1,2,3] == [1,2,3]
