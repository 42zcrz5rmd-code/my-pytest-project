import pytest

def calculate(price,discount):
    return price*(1-discount)


@pytest.mark.parametrize('price,discount,excepted',[(100,0.2,80),(200,0.5,100),(0,0.5,0)])


def test_calculate(basic,price,discount,excepted):
    assert calculate(price,discount)==excepted
    

if __name__ == '__main__':
    pytest.main([__file__, '-v'])