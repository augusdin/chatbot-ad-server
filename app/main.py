from fastapi import FastAPI
from app.api.v1.endpoints import check_ad

app = FastAPI()

# 注册路由
app.include_router(check_ad.router, prefix="/api/v1")