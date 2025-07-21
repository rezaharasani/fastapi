from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """hash the given password"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """verify the given password against the given hashed password"""
    return pwd_context.verify(plain_password, hashed_password)


def reformat_phone_number(phone_number: str | None) -> str | None:
    """reformat the phone number"""
    return phone_number[:4] + "***" + phone_number[7:]
