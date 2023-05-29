from romannumbers import Romano_a_Entero, RomanNumberError
import pytest

def test_uno_es_palito():
    assert Romano_a_Entero('I') == 1

def test_4_es_IV():
    assert Romano_a_Entero('IV') == 4

def test_9_es_IX():
    assert Romano_a_Entero('IX') == 9

def test_40_es_XL():
    assert Romano_a_Entero('XL') == 40

def test_decenas():
    assert Romano_a_Entero("L") == 50

def test_2345_es_MMCCCXLV():
    assert Romano_a_Entero("CXXIII") == 123

def test_composicion():
    assert Romano_a_Entero('MMCMXLIX') == 2949

def test_no_mas_3_repeticiones():
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("CCCC") 

def test_no_repetir_VLD():
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("VV")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("LL")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("DD")

def test_restas_no_permitidas():
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("IC")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("IL")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("XM")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("XD")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("VX")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("LM")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("LC")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("DM")
    
def test_no_repeticiones_restas():
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("IIX")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("IVX")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("IVIV")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("IXIV")
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("IXIX")  
    with pytest.raises(RomanNumberError):
        Romano_a_Entero("VIX")   

def test_punyeteros():
        Romano_a_Entero("MCMXCIX") == 1999 