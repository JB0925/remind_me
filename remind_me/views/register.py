import fastapi
from fastapi import requests
from fastapi_chameleon import template
from starlette.requests import Request
from starlette import status

from remind_me.viewmodels.shared.viewmodel import ViewModelBase
from remind_me.viewmodels.register.register_viewmodel import RegisterViewModel
from remind_me.services import user_service
from remind_me.infrastructure import cookie_auth

router = fastapi.APIRouter()

@router.get('/')
@template()
def home(request: Request): 
    # vm = IndexViewModel(request)
    # return vm.to_dict()
    return {}


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
    
    account = user_service.create_account(vm.name, vm.email, vm.password)
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)
    return response


@router.get('/login')
@template()
def login(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


# @router.post('/login')
# @template()
# async def register(request: Request):
#     vm = RegisterViewModel(request)
#     await vm.load()
    
#     if vm.error:
#         return vm.to_dict()
    
#     account = user_service.create_account(vm.name, vm.email, vm.password)
#     return fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)