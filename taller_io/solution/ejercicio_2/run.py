"""
La cafetería XYZ tiene la siguiente lista de bebidas  ‘bebidas.xlsx’ el gerente de la empresa desea hacer un aumento del 15% de cada producto, se debe generar un segundo archivo llamado salida.xlsx con el precio actual y el nuevo precio con el respectivo aumento,
Para agilizar el cambio de dinero se debe aplicar un redondeo superior al precio final. De 1000 o 500.

Ejemplo 1:
Precio inicial: 4.000
$4.000 * 15% = 600
Aumento: 600
Precio final sin redondeo: 4.600
	Precio final: 5000

Ejemplo 1:

Precio inicial: 3.000
$3.000 * 15% = 450
Aumento: 450
Precio final sin redondeo: 3.450
	Precio final: 3500
"""

import pandas as pd

path = './bebidas.xlsx'
df = pd.read_excel(path)
print("show df")
print(df)