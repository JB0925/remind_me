import fastapi
from fastapi import requests
from fastapi_chameleon import template
from starlette.requests import Request

from remind_me.viewmodels.shared.viewmodel import ViewModelBase
from remind_me.viewmodels.register.register_viewmodel import RegisterViewModel

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
    print(vm)
    if vm.error:
        return vm.to_dict()
    
    print('FIX THIS')
    return vm.to_dict()