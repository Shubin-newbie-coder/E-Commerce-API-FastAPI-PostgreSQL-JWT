## E-Commerce-API-FastAPI-PostgreSQL-JWT
ລະບົບທົດລອງ Backend ພັດທະນາໂດຍ FastAPI ແລະ PostgreSQL ໂດຍທົດສອບໃຊ້ JWT Authentication ເພື່ອເນັ້ນຄວາມປອດໄພຂອງລະບົບແລະຈັດການສິນຄ້າທີ່ມີປະສິດທິພາບ

# E-Commerce API (FastAPI + PostgreSQL + JWT)

---
## 🚀 Features
- User Registration & Login (JWT Authentication)
- Role-based Access (Admin / User)
- Product Management
- Order Management
- Secure API ด้วย JWT Token
- PostgreSQL Database
---
## 🛠 Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (JSON Web Token)
- Uvicorn
---
## 📂 Project Structure
/ecommerce_api
- main.py        
- auth.py        
- models.py      
- schemas.py    
- database.py    
## 🚀 Installation & Setup
### Clone Project
- git clone https://github.com/Shubin-newbie-coder/E-Commerce-API-FastAPI-PostgreSQL-JWT.git
### Create Virtual Environment
- python -m venv venv
- venv\Scripts\activate
### Install Dependencies
- pip install -r requirements.txt
### Setup Environment Variables
- DATABASE_URL=postgresql://username:password@localhost:5432/ecommerce_db
- SECRET_KEY=your_secret_key
- ALGORITHM=HS256
- ACCESS_TOKEN_EXPIRE_MINUTES=30
### Run Server
- uvicorn app.main:app --reload
- or
- uvicorn main:app --reload


## 🔐 Authentication Flow
- Register User
- Login → Receive JWT Token
- Use Token in Header

## ຈຸດປະສົງ 

- ຝຶກອອກແບບ REST API
- ຝຶກການໃຊ້ແລະເຂົ້າໃຈ JWT Authentication: ມີຄວາມເຂົ້າໃຈ ແລະ ສາມາດນຳໃຊ້ລະບົບຢືນຢັນຕົວຕົນດ້ວຍ JWT (JSON Web Token) ເພື່ອຄວາມປອດໄພຂອງຂໍ້ມູນ.
- ຝຶກອອກແບບໂຄງສ້າງ Backend ສຳລັບລະບົບຈິງ



## ຮູບພາບຕົວຢ່າງ 
Products
Key token login
<img width="1360" height="471" alt="image" src="https://github.com/user-attachments/assets/81c8d5ad-47b8-4cb0-87a8-f25be5975d9b" />
Products
<img width="1917" height="1031" alt="image" src="https://github.com/user-attachments/assets/20cc2548-84af-4279-8c94-763368b800d7" />
Orders
<img width="1911" height="1028" alt="image" src="https://github.com/user-attachments/assets/37952e7a-d429-4c48-912d-3219acfa90ac" />
Stock
<img width="1638" height="971" alt="image" src="https://github.com/user-attachments/assets/2a6ea7fc-31e4-4c27-82e4-35c6beb2689f" />


