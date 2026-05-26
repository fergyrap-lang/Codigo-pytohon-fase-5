# ============================================
# PROBLEMA 1 - CLASIFICACIÓN DE COMPROMISO
# ============================================

# Matriz de sesiones
# Formato:
# [ID Cliente, Duración(segundos), Eventos Clics]

sesiones = [
    [101, 250, 12],
    [102, 45, 2],
    [103, 120, 5],
    [104, 300, 15],
    [105, 70, 1]
]

# ============================================
# FUNCIÓN PARA CLASIFICAR EL COMPROMISO
# ============================================

def clasificar_compromiso(duracion, clics):

    # Clasificación ALTO
    if duracion > 180 and clics > 8:
        return "Alto"

    # Clasificación BAJO
    elif duracion < 60 or clics < 3:
        return "Bajo"

    # Clasificación MEDIO
    else:
        return "Medio"


# ============================================
# INFORME FINAL
# ============================================

print("===================================")
print(" INFORME DE COMPROMISO DE SESIONES ")
print("===================================\n")

# Recorrer la matriz
for sesion in sesiones:

    # Extraer datos
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    # Llamar la función
    clasificacion = clasificar_compromiso(duracion, clics)

    # Mostrar resultados
    print("ID Cliente:", id_cliente)
    print("Duración:", duracion, "segundos")
    print("Clics:", clics)
    print("Clasificación:", clasificacion)
    print("-----------------------------------")