# Ejercicio 1.9: Calculadora de alelantos
# calculadoraAdelantos.py


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000
total_meses= 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:
    if total_meses < pago_extra_mes_comienzo:
        saldo = (saldo * (1+tasa/12)) - pago_mensual
        total_meses = total_meses + 1
        total_pagado = total_pagado + pago_mensual

    elif pago_extra_mes_comienzo <= total_meses <= pago_extra_mes_fin:
        saldo = (saldo * (1 + tasa / 12)) - (pago_mensual + adelanto)
        total_meses = total_meses + 1
        total_pagado = total_pagado + pago_mensual + adelanto

    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_meses = total_meses + 1
        total_pagado = total_pagado + pago_mensual


print('Total pagado', round(total_pagado, 2), 'Meses totales', total_meses)

