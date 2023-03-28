from index import converte

def test_deve_entender_simbolo_I():
    assert converte('I')==1

def test_deve_entender_simbolo_IV():
    assert converte('IV')==4

def test_deve_entender_simbolo_V():
    assert converte('V')==5

def test_deve_entender_simbolo_X():
    assert converte('X')==10

def test_deve_entender_simbolo_VII():
    assert converte('VII')==7

def test_deve_entender_simbolo_XIII():
    assert converte('VIII')==8   

def test_deveEntenderNumerosComoIX():
    assert converte('IX')== 9

def test_deve_entender_simbolo_X():
    assert converte('X')==10

def test_deve_entender_simbolo_XV():
    assert converte('XV')==15  

def test_deve_entender_simbolo_XX():
    assert converte('XX')==20 

def test_deve_entender_simbolo_XXV():
    assert converte('XXV')==25

def test_deve_entender_simbolo_XXX():
    assert converte('XXX')==30

def test_deve_entender_simbolo_XXXV():
    assert converte('XXXV')==35

def test_deve_entender_simbolo_L():
    assert converte('L')==50

def test_deve_entender_simbolo_C():
    assert converte('C')==100 

def test_deve_entender_simbolo_D():
    assert converte('D')==500   

def test_deve_entender_simbolo_M():
    assert converte('M')==1000

def test_deve_entender_simbolo_LVIII():
    assert converte('LVIII')==58
    
def test_deve_entender_simbolo_MCMXCIV():
    assert converte('MCMXCIV')==1994