# -*- coding: utf-8 -*-
# @Time    : 2023/6/1 1:45
# @Author  : hjxylgogogo
# @File    : learn1.py
# @Software: PyCharm
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None  # 与bool的区别是可以不传，默认是null


@app.get('/')
async def hello_world():
    return {'hello': 'world'}


@app.get('/city/{city}')
async def result(city: str, q: Optional[str] = None):
    return {'city': city, 'query_string': q}

@app.put('/city/{city}')
async def result(city: str, city_info: CityInfo):
    return {'city': city, 'country': city_info.country, 'is_affected': city_info.is_affected}




#启动命令： uvicorn learn1:app --reload