from typing import Optional
import hashlib

from starlette.requests import Request
from starlette.responses import Response


auth_key = 'remind_me_account'

def set_auth(response: Response, user_id: int):
    hashed_id = _hash_text(str(user_id))
    val = '{}:{}'.format(user_id, hashed_id)
    response.set_cookie(auth_key, val, secure=False, httponly=True) #secure = False for development


def _hash_text(text: str) -> str:
    text = 'salty__' + text + '__text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_user_id_from_auth_cookie(request: Request) -> Optional[int]:
    if auth_key not in request.cookies:
        return None
    
    val = request.cookies[auth_key]
    parts = val.split(':')
    if len(parts) != 2:
        return None
    
    user_id = parts[0]
    hash_val = parts[1]
    hash_val_check = _hash_text(user_id)

    if hash_val != hash_val_check:
        print('hash values do not match; invalid cookie value.')
        return None
    
    try:
        return int(user_id)
    except:
        return 0


def logout(response: Response):
    response.delete_cookie(auth_key)