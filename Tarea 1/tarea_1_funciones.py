
import math

#DEFINIMOS TODO
# Se definen constantes para los códigos de error y éxito para hacer el
# código más legible y mantenible, evitando el uso de "números mágicos".

# Código de éxito universal
SUCCESS_CODE = 0

# Códigos de error para la función count_char
ERROR_CADENA_NO_STRING = -1
ERROR_CADENA_NO_ALPHANUM = -2
ERROR_CARACTER_INVALIDO = -3

# Códigos de error para la función multiplo_2
ERROR_TIPO_O_SIGNO_INVALIDO = -4
ERROR_MULTIPLO_INVALIDO = -5

# IMPLEMENTACIÓN DE FUNCIONES


def count_char(cadena, caracter):
  
    # Verificar que el parámetro cadena sea un string.
    if not isinstance(cadena, str):
        return (ERROR_CADENA_NO_STRING, None)

    # Verificar que la cadena solo contenga letras y números.
    #    Una cadena vacía se considera válida, ya que no contiene
    #    caracteres NO permitidos.
    if not cadena.isalnum() and cadena != "":
        return (ERROR_CADENA_NO_ALPHANUM, None)

    # Verificar que el parámetro carácter sea un único carácter alfanumérico.
    if not (isinstance(caracter, str) and len(caracter) == 1 and
            caracter.isalnum()):
        return (ERROR_CARACTER_INVALIDO, None)

    # Contar la cantidad de veces que el carácter aparece.
    count = cadena.count(caracter)

    # Retornar el código de éxito y el resultado.
    return (SUCCESS_CODE, count)


def multiplo_2(base, multiplo):
   
    # Verificar que los parámetros sean enteros positivos (o cero para la base).
    if not (isinstance(base, int) and isinstance(multiplo, int) and
            base >= 0 and multiplo > 0):
        return (ERROR_TIPO_O_SIGNO_INVALIDO, None)

    # Verificar que el múltiplo esté en la lista permitida.
    allowed_multiplos = [1, 2, 4, 8, 16]
    if multiplo not in allowed_multiplos:
        return (ERROR_MULTIPLO_INVALIDO, None)

    # Calcula la operación multiple * base sin usar `*`, `+` o `for`.
    #    La multiplicación por una potencia de 2 (2^n) es equivalente a
    #    desplazar los bits del número `n` posiciones a la izquierda.
    #    Para encontrar `n`, usamos el logaritmo en base 2.
    #    Ej: log2(8) = 3, entonces base * 8 es equivalente a base << 3.
    shift_amount = int(math.log2(multiplo))
    resultado = base << shift_amount

    # Devolver el código de éxito y el resultado.
    return (SUCCESS_CODE, resultado)