from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def index():
    return {
        "data": "Testando FastAPI!"
    }

@app.get("/hello")
def hello():
    return {
        "data" :"Hello!"
    }

@app.get("/hello/{name}")
def hello(name):
    return{"data" : f"Hello {name}!"
    }

@app.get("/quadrado/")
def quadrado(max: Optional[int]=5):
    data =[]
    for i in range (1,max+1):
            i2 = i*i
            data.append(i2)
    return{
        "max" :max,
        "quadrados" : data 
    }

@app.get("/tabuada/{num}")
def tabuada(num: int, start: Optional[int] = 1, end: Optional[int] = 5 ):
    data =[]
    if(start <= end):
        for i in range (start,end+1):
            result = num*i
            data.append(result)
        return{
            "num" : num,
            "start" : start,
            "end": end,
            "tabuada" : data
        }
    else:
        return{
            "erro":"Start não pode ser maior que end padrão"
        }

@app.get("/pares")
def listaPares(limit : Optional[int] = 30, minimo: Optional[int] = 5):
   pares = []
   for i in range(0, limit+1):
       pares.append(i)
  
   return {
       "limit" : limit,
       "pares" : pares
   }

class PessoaModel(BaseModel):
   primeiro_nome : str
   ultimo_nome : str
   idade : int



@app.post("/hello")
def helloPost(pessoa : PessoaModel):
   return {
       "data" : f'Hello {pessoa.primeiro_nome} {pessoa.ultimo_nome}, you are {pessoa.idade}!'
   }

