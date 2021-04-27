# Ejercicio 1.8: Adelantos
# adelantos.py


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses_adelanto = 0
adelanto = 1000
total_meses= 0

while saldo > 0:
    if meses_adelanto < 12:
        meses_adelanto = meses_adelanto + 1
        total_meses = total_meses + 1
        saldo = (saldo * (1 + tasa / 12)) - (pago_mensual + adelanto)
        total_pagado = total_pagado + pago_mensual + adelanto

    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_meses = total_meses + 1
        total_pagado = total_pagado + pago_mensual


print('Total pagado', round(total_pagado, 2), 'Meses totales', total_meses)
