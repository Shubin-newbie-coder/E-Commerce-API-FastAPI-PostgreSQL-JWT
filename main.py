from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models as models, schemas as schemas, auth as auth, database as database

app = FastAPI(
    title="Junior E-Commerce API",
    description="Backend API for E-commerce system with JWT and PostgreSQL",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

try:
    models.Base.metadata.create_all(bind=database.engine)
    print("✅ [Database] Connection successful and tables are ready.")
except Exception as e:
    print("❌ [Database] Connection failed!")
    print(f"Error details: {e}")

@app.post("/register", response_model=schemas.Token, tags=["Auth"])
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_pwd = auth.get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    
    access_token = auth.create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/login", tags=["Auth"])
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    access_token = auth.create_access_token(data={"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/products", response_model=schemas.ProductResponse, tags=["Products"])
def create_product(
    product: schemas.ProductCreate, 
    db: Session = Depends(database.get_db), 
    current_user: models.User = Depends(auth.get_current_user)
):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/products", response_model=List[schemas.ProductResponse], tags=["Products"])
def get_products(db: Session = Depends(database.get_db)):
    return db.query(models.Product).all()

@app.post("/order/{product_id}", tags=["Orders"])
def create_order(
    product_id: int, 
    db: Session = Depends(database.get_db), 
    current_user: models.User = Depends(auth.get_current_user)
):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    if product.stock <= 0:
        raise HTTPException(status_code=400, detail="Product out of stock")
    
    # --- Business Logic: Transaction ---
    try:
        product.stock -= 1 
        new_order = models.Order(
            user_id=current_user.id, 
            product_id=product.id, 
            total_price=product.price
        )
        db.add(new_order)
        db.commit() 
        db.refresh(new_order)
        return {"message": "Order completed", "order_id": new_order.id, "remaining_stock": product.stock}
    
    except Exception as e:
        db.rollback() 
        raise HTTPException(status_code=500, detail="Could not process order")

