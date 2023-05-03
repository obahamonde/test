from aiofauna import Api
from aiohttp.web import run_app

app = Api()

@app.get("/")
async def index():
    return {"hello": "world"}


if __name__ == '__main__':
    run_app(app, port=8080)