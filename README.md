Start Run
python -m uvicorn main:app --reload


🛒 Junior E-Commerce API (FastAPI + PostgreSQL)
ระบบ Backend สำหรับร้านค้าออนไลน์เบื้องต้น พัฒนาด้วย FastAPI และ PostgreSQL โดยเน้นความปลอดภัยด้วยระบบ JWT Authentication และการจัดการสต็อกสินค้าที่มีประสิทธิภาพ

🌟 Key Features
User Authentication: ระบบสมัครสมาชิกและเข้าสู่ระบบด้วย JWT Token.

Security: เข้ารหัสรหัสผ่านด้วย bcrypt ซึ่งรองรับมาตรฐานล่าสุดบน Python 3.14.

Product Management: ระบบ CRUD สำหรับจัดการข้อมูลสินค้า (ชื่อ, ราคา, สต็อก).

Order System: ระบบสั่งซื้อสินค้าพร้อม Logic การตัดสต็อกอัตโนมัติ (Inventory Control).

API Documentation: เอกสาร API แบบโต้ตอบได้ทันทีผ่าน Swagger UI.

🛠 Tech Stack
Framework: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy

Security: JWT (Jose), Bcrypt

Environment: Python 3.14+.

📂 Project Structure
Plaintext

/ecommerce_api
├── main.py        # จุดเริ่มต้นของแอปพลิเคชันและ API Endpoints
├── auth.py        # ระบบรักษาความปลอดภัย (Hashing & JWT Logic)
├── models.py      # โครงสร้างตารางฐานข้อมูล (SQLAlchemy Models)
├── schemas.py     # กำหนดรูปแบบรับ-ส่งข้อมูล (Pydantic Schemas)
└── database.py    # การตั้งค่าการเชื่อมต่อ PostgreSQL
🚀 Installation & Setup
Clone Project

Bash

git clone <your-repo-url>
cd ecommerce_api
Install Dependencies

Bash

pip install fastapi uvicorn sqlalchemy psycopg2 bcrypt python-jose[cryptography]
Database Configuration แก้ไขไฟล์ database.py โดยใส่ URL ของ PostgreSQL ของคุณ:

Python

SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/db_name"
Run Server

Bash

python -m uvicorn main:app --reload
เข้าใช้งานได้ที่: http://127.0.0.1:8000/docs.

💡 Lessons Learned (Highlight สำหรับ Portfolio)
ในโปรเจ็กต์นี้ ผมได้เรียนรู้วิธีการแก้ไขปัญหาเชิงลึก (Troubleshooting) ดังนี้:

Python 3.14 Compatibility: แก้ไขปัญหา ValueError จากการใช้ passlib บน Python เวอร์ชันใหม่ โดยการปรับเปลี่ยนมาใช้ bcrypt โดยตรง ทำให้ระบบมีความเสถียรและทันสมัยมากขึ้น.

Database Synchronization: การออกแบบให้ระบบตรวจสอบสต็อกสินค้าก่อนสร้าง Order เพื่อป้องกันปัญหาสินค้าติดลบ.




Products
<img width="1917" height="1031" alt="image" src="https://github.com/user-attachments/assets/20cc2548-84af-4279-8c94-763368b800d7" />
Orders
<img width="1911" height="1028" alt="image" src="https://github.com/user-attachments/assets/37952e7a-d429-4c48-912d-3219acfa90ac" />

