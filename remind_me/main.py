from logging import debug
import fastapi
import uvicorn
import fastapi_chameleon
from starlette.staticfiles import StaticFiles
from remind_me.views import register

app = fastapi.FastAPI()

def main():
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)


def configure(dev_mode: bool):
    configure_templates()
    configure_routes()


def configure_templates():
    fastapi_chameleon.global_init(template_folder='templates')


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(register.router)


if __name__ == '__main__':
    main()
else:
    configure(dev_mode=False)