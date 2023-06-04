# -*- coding: utf-8 -*-
# @Time    : 2023/6/1 2:22
# @Author  : hjxylgogogo
# @File    : ch03.py
# @Software: PyCharm
#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from datetime import date
from enum import Enum
from typing import Optional, List,Union

from fastapi import APIRouter, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field

app03 = APIRouter()

"""Path Parameters and Number Validations 路径参数和数字验证"""

# @app03.get("/path/parameters")
# def path_params01():
#     return {"message":"no path parameters"}
#
# @app03.get("/path/{parameters}")
# def path_params01(parameters:str):
#     return {"message":" path parameters is"+parameters}

class CityName(str,Enum):
    Beijing = "Beijing China"
    Shanghai = "Shanghai China"

@app03.get("/enum/{city}")
def latest(city:CityName):
    if city == CityName.Beijing:
        return {"city_name":city,"confirmed":1492,"death":7}
    if city == CityName.Shanghai:
        return {"city_name":city,"confirmed":971,"death":7}
    return {"city_name":city,"confirmed":None,"death":None}

@app03.get("/files/{file_path:path}")
def filepath(file_path:str):
    return f"the file path is {file_path}"

@app03.get("/path/{num}")
def path_params_validate(
        num:int = Path(...,title="you number",description="test",ge=1,le=10)
):
    return num

@app03.get("/query")
def page_limit(page:int=1,limit:Optional[int]=None):
    if limit:
        return {"page":page,"limit":limit}
    return {"page":page}

@app03.get("/query/bool/conversion")
def type_conversion(param:bool=False):
    return param

@app03.get("/query/validations")
def query_params_validate(
        value:str=Query(min_length=8,max_length=16,regex="^a"),
        values:List[str] = Query(default=["v1","v2"],alias="alias_name")
):
    return value,values

class CityInfo(BaseModel):
    name:str = Field(...,example= "Beijing")
    country:str
    country_code:str = None
    country_population:int = Field(800,title="人口数量",description="国家人数",ge=800)
    class Config:
        schema_extra = {
            "example":{
                "name":"Shanghai",
                "country":"China",
                "country_code":"CN",
                "country_population":14000000
            }
        }

@app03.post(("/request_body/city"))
def city_info(city:CityInfo):
    return city

@app03.put("/request_body/city/{name}")
def mix_city_info(
    name:str,
    city01:CityInfo,
    city02:CityInfo,
    confirmed:int=Query(ge=0,description="确证数",default=0),
    death:int = Query(ge=0,description="死亡数",default=0)
):
    if name == "Shanghai":
        return {"Shanghai":{"confirmed":confirmed,"death":death}}
    return city01,city02

class Data(BaseModel):
    city:List[CityInfo]=None
    data:date
    confirmed: int = Field(ge=0, description="确证数", default=0)
    death: int = Field(ge=0, description="死亡数", default=0)
    recovered: int = Field(ge=0, description="痊愈数", default=0)

@app03.put("/request_body/nested")
def nested_models(data:Data):
    return data

@app03.get("/cookie")
def cookie(cook:Optional[str]=Cookie(None)):
    return {"cookie_id":cook}

@app03.get("/header")
def header(user_agent: Optional[str] = Header(None, convert_underscores=True), x_token: List[str] = Header(None)):
    """
    有些HTTP代理和服务器是不允许在请求头中带有下划线的，所以Header提供convert_underscores属性让设置
    :param user_agent: convert_underscores=True 会把 user_agent 变成 user-agent
    :param x_token: x_token是包含多个值的列表
    :return:
    """
    return {"User-Agent": user_agent, "x_token": x_token}