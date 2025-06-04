from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
from calculator import Calculator

app = FastAPI()
calc = Calculator()


@app.get("/health", include_in_schema=False)
def health():
    return {"status": "ok"}

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# About page route
@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}


@app.get("/add")
def add(a: float = Query(...), b: float = Query(...)):
    return {"result": calc.add(a, b)}


@app.get("/subtract")
def subtract(a: float = Query(...), b: float = Query(...)):
    return {"result": calc.subtract(a, b)}


@app.get("/multiply")
def multiply(a: float = Query(...), b: float = Query(...)):
    return {"result": calc.multiply(a, b)}


@app.get("/divide")
def divide(a: float = Query(...), b: float = Query(...)):
    try:
        result = calc.divide(a, b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/power")
def power(a: float = Query(...), b: float = Query(...)):
    return {"result": calc.power(a, b)}


import os

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
import eval

# Code Smell 1: Método demasiado largo
def overly_long_function(a, b, c, d, e, f, g, h, i, j, k, l):
    # Más de 100 líneas para activar regla S138 (método demasiado largo)
    print("Inicio del cálculo complejo")
    result = a + b
    result *= c
    if d > 0:
        result += d
    else:
        result -= d
    for i in range(100):
        result += i * e
    if f == "test":
        result *= 2
    # ... (imaginemos 80 líneas más de lógica similar)
    print(f"Parámetros: {a}, {b}, {c}, {d}, {e}, {f}, {g}, {h}, {i}, {j}, {k}, {l}")
    print("Cálculo intermedio 1")
    print("Cálculo intermedio 2")
    # Simulamos un método largo con comentarios
    # ... (líneas adicionales)
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
def insecure_command_execution(user_input):
    # Activa regla S2076 (OS command injection)
    os.system(f"echo {user_input}")  # Vulnerabilidad: entrada no sanitizada

# Seguridad 2: Uso de subprocess con shell=True
def insecure_subprocess(user_input):
    # Activa regla S2076 o S5144 (inyección de comandos)
    subprocess.run(f"ls {user_input}", shell=True)  # Vulnerabilidad: entrada no sanitizada

# Seguridad 3: Deserialización insegura
def insecure_deserialization(data):
    # Activa regla S4960 (deserialización insegura)
    return pickle.loads(data)  # Vulnerabilidad: deserialización sin validar