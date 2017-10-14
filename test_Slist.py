import Slist
def list_Check(x):
    li = Slist(x)
    return li

def test_answer():
    assert list_Check([1,1.2,3]) == [1,3,1.2]
