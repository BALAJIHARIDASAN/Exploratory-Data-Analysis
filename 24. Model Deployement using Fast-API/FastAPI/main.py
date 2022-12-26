

import uvicorn ##ASGI
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To FAST API': f'{name}'}




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)




