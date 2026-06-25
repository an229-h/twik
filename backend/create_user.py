from app.database import SessionLocal
from app.models import User
from app.security import hash_password

db = SessionLocal()

username = input("Username: ")
password = input("Password: ")

existing = db.query(User).filter(User.username == username).first()

if existing:
    print("User already exists.")
    exit()

user = User(
    username=username,
    password_hash=hash_password(password)
)

db.add(user)
db.commit()

print("User created successfully.")