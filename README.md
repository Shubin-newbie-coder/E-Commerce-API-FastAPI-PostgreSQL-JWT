E-Commerce API (FastAPI + PostgreSQL)
ລະບົບທົດລອງ Backend ພັດທະນາໂດຍ FastAPI ແລະ PostgreSQL ໂດຍທົດສອບໃຊ້ JWT Authentication ເພື່ອເນັ້ນຄວາມປອດໄພຂອງລະບົບແລະຈັດການສິນຄ້າທີ່ມີປະສິດທິພາບ

## 🌟 Key Features
User Authentication: ລະບົບສະຫມັກສະມາຊິກແລະເຂົ້າສູ່ລະບົບໂດຍ JWT Token.
Security: ເຂົ້າລະຫັດຜ່ານໂດຍ bcrypt 
Product Management: ລະບົບ CRUD ສຳຫລັບຈັດການສິນຄ້າ (ຊື່,ລາຄາ,ສະຕ໋ອກ).
Order System: ລະບົບການສັ່ງຊື້ພ້ອມ Logic ການຫັກຈຳນວນອັດຕະໂນມັດ. (Inventory Control).
API Documentation:API ແບບໂຕ້ຕອບຜ່ານ Swagger UI.

## 🛠 Tech Stack
Framework: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy
Security: JWT (Jose), Bcrypt
Environment: Python 3.14+.

## 📂 Project Structure
/ecommerce_api
├── main.py        
├── auth.py        
├── models.py      
├── schemas.py    
└── database.py    

## 🚀 Installation & Setup
Clone Project
Bash
git clone <your-repo-url>
cd ecommerce_api

Install Dependencies
Bash
pip install fastapi uvicorn sqlalchemy psycopg2 bcrypt python-jose[cryptography]


Run Server

Bash

python -m uvicorn main:app --reload
http://127.0.0.1:8000/docs.


ຮູບພາບຕົວຢ່າງ 
Products
<img width="1917" height="1031" alt="image" src="https://github.com/user-attachments/assets/20cc2548-84af-4279-8c94-763368b800d7" />
Orders
<img width="1911" height="1028" alt="image" src="https://github.com/user-attachments/assets/37952e7a-d429-4c48-912d-3219acfa90ac" />
Stock
<img width="1638" height="971" alt="image" src="https://github.com/user-attachments/assets/2a6ea7fc-31e4-4c27-82e4-35c6beb2689f" />


