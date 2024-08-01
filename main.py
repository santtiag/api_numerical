from fastapi import FastAPI, HTTPException, Query 
import requests
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.title = 'Numerical Project'

origins = [
    "https://api-numerical.onrender.com",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["Content-Type", "Authorization"],
    max_age=3600,  # tiempo de vida de la configuración CORS (en segundos)
)

URL = '/home/'

# INFO: The path that u need to change to the ulr -> 'url_ngrok/engine/'
# URL_ENGINE = 'http://localhost:5000/engine/'
URL_ENGINE = 'https://572f-181-130-217-21.ngrok-free.app/engine/'

@app.get('/home', tags=['Home'])
def print():
    return 'HelloWorld, All Nice'

@app.get(f'{URL}interpolation/quadratic_segm/calculate', tags=['Calculate'])
def calculate_i_quadratic_segm(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(f'{URL_ENGINE}interpolation/quadratic_segm', json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')

@app.get(f'{URL}interpolation/cubic_segm/calculate', tags=['Calculate'])
def calculate_i_cubic_segm(x: str = Query(...), y: str = Query(...)):
    x_values = [float(val) for val in x.split(',')]
    y_values = [float(val) for val in y.split(',')]

    playload = {'x': x_values, 'y': y_values}

    response = requests.post(f'{URL_ENGINE}interpolation/cubic_segm', json=playload)

    if response.status_code == 200:
        result = response.json()
        return JSONResponse(content=jsonable_encoder(result))
    else:
        raise HTTPException(status_code=500, detail='Error processing data')
