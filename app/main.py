from fastapi import FastAPI
from app.api.v1.endpoints import check_ad
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许跨域请求的来源
origins = [
    "http://localhost:3000",  # 允许的前端应用地址
    "https://chatnext4ad.vercel.app",  # 如果有其他前端域名，可以在这里添加
]

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许的 HTTP 方法
    allow_headers=["*"],  # 允许的 HTTP 请求头
)

# 注册路由
app.include_router(check_ad.router, prefix="/api/v1")