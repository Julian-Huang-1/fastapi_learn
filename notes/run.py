# -*- coding: utf-8 -*-
# @Time    : 2023/6/1 2:12
# @Author  : hjxylgogogo
# @File    : run.py.py
# @Software: PyCharm

import uvicorn
from fastapi import FastAPI
from tutorial import app03,app04,app05

app = FastAPI()

app.include_router(app03,prefix="/ch03",tags=["no3"])
app.include_router(app04,prefix="/ch04",tags=["no4"])
app.include_router(app05,prefix="/ch05",tags=["no5"])

if __name__ == "__main__":
    uvicorn.run("run:app",host="0.0.0.0",port=8000,reload=True,\
                debug=True,workers=1)