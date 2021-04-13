import fastapi
from fastapi import requests
from fastapi_chameleon import template
from starlette.requests import Request
from starlette import status

from remind_me.sms import send
from remind_me.viewmodels.shared.viewmodel import ViewModelBase
from remind_me.viewmodels.register.register_viewmodel import RegisterViewModel
from remind_me.viewmodels.register.login_viewmodel import LoginViewModel
from remind_me.viewmodels.register.home_viewmodel import HomeViewModel
from remind_me.services import user_service
from remind_me.infrastructure import cookie_auth
from remind_me import schedule_jobs

router = fastapi.APIRouter()


@router.get('/')
@template()
def home(request: Request):
    vm = ViewModelBase(request)
    if vm.is_logged_in:
        return vm.to_dict()
    return fastapi.responses.RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)


@router.post('/')
@template()
async def home(request: Request):
    vm = HomeViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    job = user_service.make_job(vm.task, vm.number, vm.carrier, vm.date_and_time)
    schedule_jobs.add_job(job[0])
    user_service.store_events(vm.name, vm.number, vm.carrier, vm.task, vm.date_and_time)
    return fastapi.responses.RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


@router.get('/register')
@template()
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.post('/register')
@template()
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    account = user_service.create_account(vm.name.lower(), vm.email, vm.password)
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)
    return response


@router.get('/login')
@template()
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/login')
@template()
async def login(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = user_service.login_user(vm.name, vm.password)
    if not user:
        vm.error = 'This account does not exist or the password was entered incorrectly.'
        return vm.to_dict()

    response_ = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response_, user.id)
    return response_


@router.get('/logout')
@template()
def logout(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()


@router.post('/logout')
@template()
def logout():
    response = fastapi.responses.RedirectResponse(url='/login', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response




