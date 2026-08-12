import bcrypt
from database import SessionLocal, User

db = SessionLocal()

def register(username, email, password):

    existing = db.query(User).filter(
        (User.username == username) |
        (User.email == email)
    ).first()

    if existing:
        return False

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    user = User(
        username=username,
        email=email,
        password=hashed
    )

    db.add(user)
    db.commit()

    return True


def login(username, password):

    user = db.query(User).filter(
        User.username == username
    ).first()

    if user:

        if bcrypt.checkpw(
            password.encode(),
            user.password.encode()
        ):
            return True

    return False