# Ejercicio 1.11: Bonus
# bonus.py


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000
total_meses= 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
tabla_informe = []


while saldo > 0:
    if total_meses < pago_extra_mes_comienzo:
        saldo = (round((saldo * (1+tasa/12)) - pago_mensual, 3))
        total_meses = total_meses + 1
        total_pagado = (round(total_pagado + pago_mensual, 3))
        control = total_meses, total_pagado, saldo
        tabla_informe.append(control)

    elif pago_extra_mes_comienzo <= total_meses <= pago_extra_mes_fin:
        saldo = (round((saldo * (1 + tasa / 12)) - (pago_mensual + adelanto), 3))
        total_meses = total_meses + 1
        total_pagado = (round(total_pagado + pago_mensual + adelanto, 3))
        control = total_meses, total_pagado, saldo
        tabla_informe.append(control)

    else:
        if saldo > pago_mensual:
            saldo = (round(saldo * (1 + tasa / 12) - pago_mensual, 3))
            total_meses = total_meses + 1
            total_pagado = (round(total_pagado + pago_mensual, 3))
            control = total_meses, total_pagado, saldo
            tabla_informe.append(control)
        else:
            pago_mensual = saldo
            saldo = saldo - pago_mensual
            total_meses = total_meses + 1
            total_pagado = (round(total_pagado + pago_mensual, 3))
            control = total_meses, total_pagado, saldo
            tabla_informe.append(control)
            if saldo == 0:
                for x in tabla_informe:
                    print(x)
