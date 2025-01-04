from fastapi import FastAPI
from app.routes import auth, products, cart, orders, users
from app.database import engine, Base

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SPL API", version="1.0.0")

# Register routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(cart.router, prefix="/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", summary="Welcome Endpoint")
async def root():
    return {"message": "Welcome to the SPL API!"}
