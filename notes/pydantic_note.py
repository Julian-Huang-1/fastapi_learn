# -*- coding: utf-8 -*-
# @Time    : 2023/5/31 0:49
# @Author  : hjxylgogogo
# @File    : pydantic_note.py
# @Software: PyCharm

from pydantic import BaseModel ,ValidationError
from datetime import datetime, date
from typing import List,Optional
from pathlib import Path
from sqlalchemy import Column,Integer,String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

class User(BaseModel):
    id:int #必填
    name:str = "am" #选填
    signup_ts:Optional[datetime] = None #选填
    friends:List[int] = [] #列表中元素是int或者可以直接转int的



a = {
    "id":123,
    "signup_ts":"2022-12-22 12:22",
    "friends":[1,2,3]
}
user = User(**a)
try:
    User(id=123, name="am", signup_ts=datetime.today(),\
         friends=["asd", 2, 3])
except ValidationError as e:
    print(e.json())

print(user)
print(user.dict())
print(type(user.json()))
print(user.copy())
print(User.parse_obj(obj=a))#解析字典类型数据
print(User.parse_raw('{"id": 123, "signup_ts": "2022-12-22 12:22", "friends": [1, 2, 3]}'))

path = Path("hhh.json")
path.write_text('{"id": 123, "signup_ts": "2022-12-22 12:22", "friends": [1, 2, 3]}')
print(User.parse_file(path))

print(type(user.schema()))
print(type(user.schema_json()))

a2 = {"id": 123, "signup_ts": "2022-12-22 12:22", "friends": ["as", 2, 3]}
print(User.construct(**a2)) #取消校验数据
print(User.__fields__.keys())#定义模型类时，所有字段都注明类型，字段顺序不会乱
class Sound(BaseModel):
    sound:str
class Dog(BaseModel):
    birthday:date
    weight:float = Optional[None]
    sound:List[Sound]
dog1 = Dog(birthday=date.today(),weight=6.66,sound=[Sound(sound="wang")])


B = declarative_base()
class CompanyORM(B)
    __table__ = "companies"
    id = Column(Integer,primary_key=True,)

pass