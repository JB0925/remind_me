from starlette.requests import Request

from remind_me.viewmodels.shared.viewmodel import ViewModelBase


class LoginViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.name = ''
        self.password = ''
    

    async def load(self):
        form = await self.request.form()
        self.name = form.get('name', '').lower().strip()
        self.password = form.get('password').strip()

        if not self.name or not self.name.strip():
            self.error = 'You must input a name.'
        elif not self.password:
            self.error = 'You must input a password.'