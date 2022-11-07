def dodawanie1(x):
    return x+1
def mnozeniedwojki(x):
    2*x
def wiekszamniejszaod0(x):
    if x > 0:
        return 1
    else:
        return -1
def test_answer1():
    assert wiekszamniejszaod0(2137)==1
def test_answer2():
    assert dodawanie1(5)==6
def test_answer3():
    assert mnozeniedwojki(3)==6
