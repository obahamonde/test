from aiofauna import Api, FaunaModel, Field


class Product(FaunaModel):
    name: str = Field(...)
    price: float = Field(...)

    
app = Api()

@app.get("/")
async def index():
    return {
        "message": "Hello World!"
    }
    
@app.post("/api/product")
async def create_product(product: Product):
    return await product.save()

@app.get("/api/product")
async def get_products():
    return await Product.all()

@app.on_event("startup")
async def on_startup(_):
    await Product.provision()