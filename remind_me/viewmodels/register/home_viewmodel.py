from starlette.requests import Request

from remind_me.viewmodels.shared.viewmodel import ViewModelBase


class HomeViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

        self.name = ''
        self.number = ''
        self.task = ''
        self.date_and_time = ''
        self.carrier = ''
        self.timezone = ''
    

    async def load(self):
        form = await self.request.form()
        print(form)
        self.name = form.get('name')
        self.number = form.get('number')
        self.date_and_time = form.get('date_and_time')
        self.task = form.get('task')
        self.carrier = form.get('carrier')
        self.timezone = form.get('timezone')

        if not self.name or not self.name.strip():
            self.error = 'You must enter a name.'
        elif not self.number or len(self.number) != 10:
            self.error = 'You must enter a phone number, and it must be 10 digits - no spaces or hyphens.'
        elif not self.date_and_time or not self.date_and_time.strip():
            self.error = 'You must enter a date and time to be reminded at.'
        elif not self.task or len(self.task) > 50:
            self.error = 'You need to enter a task, and it must be less than 50 characters in length.'
        elif not self.carrier or not self.carrier.strip():
            self.error = 'You need to enter a phone service carrier.'
        elif not self.timezone or not self.timezone.strip():
            self.error = 'Please enter a timezone'