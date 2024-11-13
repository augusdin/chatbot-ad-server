from openai import OpenAI
from httpx import URL

# 创建客户端实例
BASE_URL = URL("https://aihubmix.com")
client = OpenAI(api_key="sk-fGpATxGXaxUL9EcaB2Fa9580662841De9bB2E9FfB5323dCc",base_url="https://aihubmix.com/v1")
# client.api_key = 'sk-fGpATxGXaxUL9EcaB2Fa9580662841De9bB2E9FfB5323dCc'
# client.base_url = URL('https://aihubmix.com')

# 测试调用
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response)
except Exception as e:
    print(f"错误类型: {type(e)}")
    print(f"错误信息: {str(e)}")