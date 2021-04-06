from typing import Optional
from starlette.requests import Request

from remind_me.viewmodels.shared.viewmodel import ViewModelBase

class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)
        self.name: Optional[str] = None
        self.email: Optional[str] = None
        self.password: Optional[str] = None


    async def load(self):
        form = await self.request.form()
        self.name = form.get('name')
        self.email = form.get('email')
        self.password = form.get('password')

        if not self.name or not self.name.strip():
            self.error = 'Your name is a required field.'
        elif not self.email or not self.email.strip():
            self.error = 'Please enter an email address.'
        elif not self.password or len(self.password) < 5:
            self.error = 'Your password is required and must be at least 5 characters long.'
        
        