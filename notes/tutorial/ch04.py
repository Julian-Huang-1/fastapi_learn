# -*- coding: utf-8 -*-
# @Time    : 2023/6/1 2:22
# @Author  : hjxylgogogo
# @File    : ch04.py
# @Software: PyCharm
from typing import Optional, List, Union

from fastapi import APIRouter, status, Form, File, UploadFile, HTTPException
from pydantic import BaseModel, EmailStr

app04 = APIRouter()

"""Response Model 响应模型"""


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    mobile: str = "10086"
    address: str = None
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr  # 用 EmailStr 需要 pip install pydantic[email]
    mobile: str = "10086"
    address: str = None
    full_name: Optional[str] = None


users = {
    "user01": {"username": "user01", "password": "123123", "email": "user01@example.com"},
    "user02": {"username": "user02", "password": "123456", "email": "user02@example.com", "mobile": "110"}
}


# @app04.post("/response_model/", response_model=UserOut, response_model_exclude_unset=True)
# async def response_model(user: UserIn):
#     """response_model_exclude_unset=True表示默认值不包含在响应中，仅包含实际给的值，如果实际给的值与默认值相同也会包含在响应中"""
#     print(user.password)  # password不会被返回
#     # return user
#     return users["user01"]

@app04.post("/response_model/attr",response_model=UserOut)
async def response_model(user: UserIn):
    """response_model_exclude_unset=True表示默认值不包含在响应中，仅包含实际给的值，如果实际给的值与默认值相同也会包含在响应中"""
    return user

@app04.post("/states_code",status_code=status.HTTP_410_GONE)
def status_code():
    pass