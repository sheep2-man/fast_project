from enum import Enum
from typing import Union
from pydantic import BaseModel, Field
from fastapi import FastAPI, Form, File, UploadFile, Query

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: str
#     is_offer: Union[bool, None] = None


class Item(BaseModel):
    name: str = Field(..., title="Item_name", max_length=50)
    description: str = Field(..., title="Item_description", max_length=50)
    price: float = Field(..., title="Price", gt=0)


class ZygClassName(str, Enum):
    Name = "zyg"
    Year = 18
    Id = "20153201072"
    student = True


# zyg_man固定传参为类属性
@app.get("/zyg/{zyg_man}")
def root(zyg_man: ZygClassName):
    return {"status": zyg_man, "test": ZygClassName.Year}


# 传参路径
@app.get("/files/{file_path:path}")
def file_path(file_path: str):
    return {"file_path": file_path}


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
#
#
# @app.post("/login/")
# async def login(username: str = Form(), password: str = Form()):
#     return {"username": username}
#
#
# # 路由操作函数
# @app.post("/files/")
# async def create_file(file: UploadFile = File(...)):
#     return {"filename": file.filename}

#
# @app.post("/items/")
# async def create_item(
#     name: str = Form(...), description: str = Form(None), price: float = Form(..., gt=0)
# ):
#     return {"name": name, "description": description, "price": price}
@app.post("/items/")
async def create_item(item: Item):
    return item.name


@app.get("/items/")
async def read_items(q: str = Query("hello world", max_length=50)):
    results = {"items": "Big preoject"}
    if q:
        results.update({"q": q})  # 给字典results添加一个健值对{"q": q}
    return results
