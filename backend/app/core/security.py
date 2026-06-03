from passlib.context import CryptContext

from jose import JWTError, jwt

from datetime import datetime, timedelta

from fastapi import Depends, HTTPException

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)


# Password hashing
pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"
)


# JWT settings
SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Hash password
def hash_password(password: str):

    return pwd_context.hash(password)


# Verify password
def verify_password(

    plain_password,

    hashed_password
):

    return pwd_context.verify(

        plain_password,

        hashed_password
    )


# Create JWT token
def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(

        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({

        "exp": expire
    })

    encoded_jwt = jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM
    )

    return encoded_jwt


# JWT authentication
security = HTTPBearer()


# Get current user from token
def get_current_user(

    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    try:

        token = credentials.credentials

        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")


        if username is None:

            raise HTTPException(

                status_code=401,

                detail="Invalid token"
            )

        return username


    except JWTError:

        raise HTTPException(

            status_code=401,

            detail="Invalid token"
        )