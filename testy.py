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
    assert dodawanie1(5)==7
    assert potegadwojki(2)==4
    assert wiekszamniejszaod0(2137)==1