import fastapi
from fastapi import requests
from fastapi_chameleon import template
from remind_me.viewmodels.shared.viewmodel import ViewModelBase
from starlette.requests import Request

#from remind_me.viewmodels.home.indexviewmodel import IndexViewModel

router = fastapi.APIRouter()

@router.get('/')
@template()
def home(request: Request): 
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get('/register')
@template()
def about(request: Request):
    vm = ViewModelBase(request)
    return {}