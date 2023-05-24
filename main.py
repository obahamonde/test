from aiofauna import Api

app = Api()

@app.get("/")
async def index():
    return {"hello": "world"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"hello": name}

if __name__ == "__main__":
    app.run()