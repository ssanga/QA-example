import os
import os
import subprocess
import pickle

def insecure_function():
    user_input = input("Ingresa un comando: ")
    os.system(user_input) # Vulnerabilidad: ejecución de comandos sin sanitizar

def buggy_function():
    x = None
    return x.upper() # Bug: AttributeError

def long_function():
    print("Linea 1")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    print("Linea 2")
    # Añade muchas líneas para generar un code smell



import os
import subprocess
import pickle
import hashlib

# Code Smell 1: Método demasiado largo
def overly_long_function(a, b, c, d, e, f, g, h, input_i, j, k, l):
    # Más de 100 líneas para activar regla S138 (método demasiado largo)
    print("Inicio del cálculo complejo")
    result = a + b
    result *= c
    if d > 0:
        result += d
    else:
        result -= d
    for loop_i in range(100):  # Renombrado para evitar S1481
        result += loop_i * e
    if f == "test":
        result *= 2
    # Simulamos un método largo con comentarios
    print(f"Parámetros: {a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}, {input_i}, {j}, {k}, {l}")
    print("Cálculo intermedio 1")
    print("Cálculo intermedio 2")
    # ... (imaginemos 80 líneas más de lógica similar)
    return result

# Code Smell 2: Demasiados parámetros
def function_with_too_many_parameters(a, b, c, d, e, f, g, h):
    # Activa regla S107 (más de 7 parámetros)
    return a + b + c + d + e + f + g + h

# Code Smell 3: Variable no utilizada
def unused_variable():
    # Activa regla S1854 (variable no utilizada)
    unused_var = 42
    result = 10
    return result

# Code Smell 4: Complejidad ciclomática alta
def high_cyclomatic_complexity(value):
    # Activa regla S1541 (complejidad > 10)
    if value > 0:
        if value < 10:
            result = "Menor a 10"
        elif value < 20:
            result = "Menor a 20"
        elif value < 30:
            result = "Menor a 30"
        else:
            result = "Mayor o igual a 30"
    else:
        if value > -10:
            result = "Mayor a -10"
        elif value > -20:
            result = "Mayor a -20"
        elif value > -30:
            result = "Mayor a -30"
        else:
            result = "Menor o igual a -30"
    return result

# Code Smell 5: Código duplicado
def duplicated_code_1():
    # Activa regla S1192 (código duplicado)
    x = 10
    y = 20
    z = x + y
    print(f"Resultado: {z}")
    return z

def duplicated_code_2():
    # Duplicado intencionalmente
    x = 10
    y = 20
    z = x + y
    print(f"Resultado: {z}")
    return z

# Seguridad 1: Ejecución de comandos inseguros
def insecure_function():
    user_input = input("Ingresa un comando: ")
    os.system(user_input)  # Activa regla S2076 (OS command injection)

# Seguridad 2: Ejecución de comandos inseguros
def insecure_command_execution(user_input):
    os.system(f"echo {user_input}")  # Activa regla S2076 (OS command injection)

# Seguridad 3: Uso de subprocess con shell=True
def insecure_subprocess(user_input):
    subprocess.run(f"ls {user_input}", shell=True)  # Activa regla S2076 o S5144

# Seguridad 4: Deserialización insegura
def insecure_deserialization(data):
    return pickle.loads(data)  # Activa regla S4960 (deserialización insegura)

# Seguridad 5: Bug potencial
def buggy_function():
    x = None
    return x.upper()  # Activa regla S1764 (acceso a atributo en None)

# Seguridad 6: Nueva función para probar S2076
def test_insecure_command():
    user_cmd = "whoami"  # Simula entrada de usuario
    os.system("ping " + user_cmd)  # Activa regla S2076 (OS command injection)

# Seguridad 7: Nueva función para probar S5131
def weak_crypto():
    return hashlib.md5("test".encode()).hexdigest()  # Activa regla S5131 (algoritmo criptográfico débil)