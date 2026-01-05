# Calculadora de Dígito Verificador de Cédula Uruguaya

Este proyecto implementa el algoritmo para calcular el dígito verificador de las cédulas de identidad uruguayas.

## Descripción

En Uruguay, las cédulas de identidad tienen exactamente 7 dígitos más un dígito verificador que sigue el formato:

```
a.bcd.efg-h
```

Donde `h` es el dígito verificador calculado mediante un algoritmo específico.

## Algoritmo

Para calcular el dígito verificador:

1. Multiplicar cada dígito por las constantes: `(2, 9, 8, 7, 6, 3, 4)`
2. Sumar todos los productos: `s = 2*a + 9*b + 8*c + 7*d + 6*e + 3*f + 4*g`
3. Calcular el módulo 10: `M = s % 10`
4. El dígito verificador es: `h = (10 - M) % 10`

### Ejemplo

Para la cédula `1.234.567`:
- `s = 2*1 + 9*2 + 8*3 + 7*4 + 6*5 + 3*6 + 4*7 = 148`
- `M = 148 % 10 = 8`
- `h = (10 - 8) % 10 = 2`
- Resultado: `1.234.567-2`

## Uso

### Desde línea de comandos

```bash
python main.py 1234567
```

### Sin argumentos

Ejecuta ejemplos predefinidos:

```bash
python main.py
```

### Como módulo

```python
from cedula import Cedula

# Crear instancia
cedula = Cedula("1234567")

# Obtener dígito verificador
digito = cedula.getVerifierDigit()

# Formatear cédula completa
cedula_completa = cedula.formatCedula()
```

## Estructura del Proyecto

```
digito_cedula/
├── cedula.py           # Clase principal con la lógica del algoritmo
├── main.py             # Script principal para ejecución
├── dummy_cedulas.txt   # Datos de prueba
├── test/
│   └── test_cedula.py  # Tests unitarios
├── requirements.txt    # Dependencias (vacío)
└── README.md          # Este archivo
```

## Ejecutar Tests

```bash
cd test
python test_cedula.py
```

## Características

- Acepta números de cédula como string o entero
- Maneja formatos con y sin puntos/guiones
- Valida longitud (6-7 dígitos)
- Formatea la salida correctamente
- Incluye tests unitarios

## Autor

Wilbert