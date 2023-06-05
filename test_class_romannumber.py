from class_romannumbers import RomanNumber, RomanNumberError
import pytest

def test_instanciar_un_numero_romano():
    romano = RomanNumber(23)
    #Lo cambiamos al atributo publico para ser coherentes
    #assert romano._numero == 23 
    #assert romano._simbolo == "XXIII"
    assert romano.numero == 23
    assert romano.simbolo == "XXIII"


def test_instanciar_otro():
    romano = RomanNumber(13)
    assert romano.numero == 13
    assert romano.simbolo == "XIII"

def test_instanciar_otro():
    romano = RomanNumber("XI")
    assert romano.numero == 11
    assert romano.simbolo == "XI"

def test_cambiar_valor_de_romano():
    romano = RomanNumber(1)
    assert romano.numero == 1 #assert romano.num == 1 
    assert romano.simbolo == "I" #assert romano.simbol == "I"

    romano.numero = 2
    assert romano.numero == 2
    assert romano.simbolo == "II"

    romano.simbolo = "III"
    assert romano.numero == 3
    assert romano.simbolo == "III"


def test_sumas():
    romano1 = RomanNumber("X")
    romano2 = RomanNumber(5)

    assert romano1 + romano2 == RomanNumber('XV')
    assert romano1 + 5 == RomanNumber(15)
    assert romano1 + "V" == RomanNumber(15)

    assert 5 + romano1 == RomanNumber('XV')

def test_restas():
    romano1 = RomanNumber("X")
    romano2 = RomanNumber(5)

    assert romano1 - romano2 == RomanNumber('V')
    assert romano1 - 5 == RomanNumber(5)
    assert romano1 - "V" == RomanNumber(5)

    assert 10 - romano2 == RomanNumber('V')
    
    with pytest.raises(RomanNumberError):
        assert 5 - romano1


def test_multiplicacionens():
    romano1 = RomanNumber("X")
    romano2 = RomanNumber(5)

    assert romano1 * romano2 == RomanNumber('L')
    # Podria ser assert romano1 * romano2 == RomanNumber(50)
    assert romano1 * 5 == RomanNumber(50)
    assert romano1 * "V" == RomanNumber(50)

    assert 5 * romano1 == RomanNumber(50)

def test_divisiones():
    romano1 = RomanNumber("X")
    romano2 = RomanNumber(5)

    assert romano1 / romano2 == RomanNumber('II')
    assert romano1 / 5 == RomanNumber(2)
    assert romano1 / "V" == RomanNumber(2)

    assert 10 / romano2 == RomanNumber('II')
    
    with pytest.raises(RomanNumberError):
        assert 5 / romano1

def test_zero():
    with pytest.raises(RomanNumberError):
        assert RomanNumber(0)

def test_operaciones_logicas():
    romano1 = RomanNumber(10)

    assert romano1 == 10

    assert romano1 > 9
    assert romano1 >= 9
    assert romano1 >= 10

    assert romano1 < 11
    assert romano1 <= 11
    assert romano1 <= 10

    assert romano1 != 11


    assert 10 == romano1

    assert 11 > romano1
    assert 11 >= romano1
    assert 10 >= romano1

    assert 9 < romano1
    assert 9 <= romano1
    assert 10 <= romano1

    assert 11 != romano1
