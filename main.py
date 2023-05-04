from aiofauna import Api


app = Api()

@app.get("/")
async def index():
    return {"hello": "world"}
