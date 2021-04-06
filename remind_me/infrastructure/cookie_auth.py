from typing import Optional
from starlette.requests import Request
from starlette.responses import Response

from remind_me.services.user_service import hash_string, check_string


auth_key = 'remind_me_account'

def set_auth(response: Response, user_id: int):
    hashed_id = hash_string(str(user_id))
    response.set_cookie(auth_key, hashed_id, secure=False, httponly=True) #secure = False for development


def get_user_id_from_auth_cookie(request: Request) -> Optional[int]:
    if auth_key not in request.cookies:
        return None
    
    val = request.cookies[auth_key]
    print(val)
    parts = val.split(':')
    if len(parts) != 2:
        return None
    
    user_id = parts[0]
    print(user_id)
    hash_val = parts[1]
    print(hash_val)
    # hash_val_check = hash_string(user_id)
    # print(hash_val_check)
    # if hash_val != hash_val_check:
    if not check_string(val, user_id):
        print('no, they aren\'t equal.')
        return None
    else:
        print('equal!!!')
    try:
        return int(user_id)
    except:
        return 0