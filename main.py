from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
from calculator import Calculator

app = FastAPI()
calc = Calculator()


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
