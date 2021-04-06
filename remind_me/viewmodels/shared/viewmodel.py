from typing import Optional

from starlette.requests import Request

from remind_me.infrastructure import cookie_auth


class ViewModelBase:
    def __init__(self, request: Request) -> None:
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None
        self.is_logged_in = cookie_auth.get_user_id_from_auth_cookie(self.request)
    

    def to_dict(self) -> dict:
        return self.__dict__