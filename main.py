#!/bin/python3

import sys
from cedula import Cedula


def print_result(nro_cedula):
    """_summary_

    Args:
        nro_cedula (_type_): _description_
    """
    print(f"=" * 40)
    obj = Cedula(nro_cedula)
    print(f"Verifier digit: {obj.getVerifierDigit()}")
    print(f"Document number: {obj.numero}")
    print(f"Full document number: {obj.formatCedula()}")
    print()


def main():
    """_summary_
    """
    _n = len(sys.argv)
    if _n == 2:
        print_result(sys.argv[1])
    else:
        ciudadanos = [{'nombre': 'papa', 'cedula': '935.450'},
                      {'nombre': 'monica', 'cedula': 1756964},
                      {'nombre': 'wilbert', 'cedula': 1756866},
                      {'nombre': 'la bruja', 'cedula': "3.315.714"},
                      {'nombre': 'romina', 'cedula': 5128957},
                      {'nombre': 'juan pablo', 'cedula': 5694280},
                      {'nombre': 'geronimo', 'cedula': 5664247},
                      {'nombre': 'fede', 'cedula': 1868178},
                      {'nombre': 'hermana fede', 'cedula': 1713676}]

        for people in ciudadanos:
            print(f"{people['nombre']}")
            print_result(people['cedula'])


if __name__ == "__main__":
    sys.exit(main())
