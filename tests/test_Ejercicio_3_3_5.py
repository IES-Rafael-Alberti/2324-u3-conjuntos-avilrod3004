import pytest
from src.Ejercicio_3_3_5 import buscar_pares, buscar_multiplos_de_tres

@pytest.mark.parametrize(
    'input_x, expected',
    [
        ({2, 4, 5, 6, 10, 13, 15}, {2, 4, 6, 10}),
        ({1, 3, 4, 6, 12, 34, 14, 67, 87}, {4, 6, 12, 14, 34}),
        ([89, 100, 23, 4, 34, 67, 78], {4, 34, 78, 100})
    ]
)

def test_buscar_pares_params(input_x, expected):
    assert buscar_pares(input_x) == expected