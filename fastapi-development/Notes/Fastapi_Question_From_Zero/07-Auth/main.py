from jose import jwt ,JWTError
from datetime import datetime,timedelta
from fastapi import HTTPException
from passlib.context import CryptContext

SECRET_KEY="My-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60
def create_access_token(username:str) ->str:
    expire=datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    #payload data
    payload= {
        "sub":username,
        "exp":expire
    }

    #generate jwt token
    access_token=jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return access_token
token=create_access_token("admin")
print(f"Token is --> {token} \n")


#decode
def decode_token(token:str):
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        username=payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="invaid"
            )
        return username
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="expired"
        )
    

decode=decode_token(token)
print(f"username is {decode}")


#create hashing context
pwd_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

#hash Password
def hash_password(password:str):
    return pwd_context.hash(password)
hashing=hash_password(token)
print(f"hashed password is {hashing}")

# verify password
def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

verify :bool=verify_password(token,hashing)
print(f"password is verified {verify}")