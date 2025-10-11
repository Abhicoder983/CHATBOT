import jwt
import datetime
from django.conf import settings

def generate_token(user):
    payload={
        'user':user,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=int(settings.JWT_EXPIRY)),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None