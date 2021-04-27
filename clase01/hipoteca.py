# Ejercicio 1.7: La Hipoteca
# hipoteca.py


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))

total = 'Total pagado: '
pagado = round(total_pagado, 2)
print('Utilizando f-strings: ', f'{total}{pagado}')