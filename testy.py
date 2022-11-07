def dodawanie1(x):
    return x+1
def potegadwojki(x):
    2**x
def wiekszamniejszaod0(x):
    if x > 0:
        return 1
    else:
        return -1
def test_answer():
    assert potegadwojki(2)==4
    assert wiekszamniejszaod0(2137)==1
    assert dodawanie1(5)==7
