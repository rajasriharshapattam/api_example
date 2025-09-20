from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")
def add(a, b):
    """Add two numbers and return the result."""
    result = float(a) + float(b)
    # result = a+b
    return {"operation": "add", "a": a, "b": b, "result": result}

@app.get("/subtract")
def subtract(a, b):
    """Subtract b from a and return the result."""
    result = float(a) - float(b)
    # result = a-b
    return {"operation": "subtract", "a": a, "b": b, "result": result}

@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Calculator API is running. Use /add or /subtract endpoints."}


# Main program
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9321)

""" def add(x,y):
    return x + y

x=5
y=10

if __name__ == "__main__":
  x=sys.argv[1]
  y=sys.argv[2]
  print(add(float(x),float(y))) """
