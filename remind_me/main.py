from logging import debug
import fastapi
import uvicorn
import fastapi_chameleon
from starlette.staticfiles import StaticFiles
from remind_me.views import register
from remind_me.data.db_session import global_init

app = fastapi.FastAPI()

def main():
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)


def configure(dev_mode: bool):
    configure_templates()
    configure_routes()
    configure_db(dev_mode)


def configure_templates():
    fastapi_chameleon.global_init(template_folder='remind_me/templates')


def configure_db(dev_mode: bool):
    global_init()


def configure_routes():
    app.mount('remind_me/static', StaticFiles(directory='/remind_me/remind_me/static'), name='static')
    app.include_router(register.router)


if __name__ == '__main__':
    main()
else:
    configure(dev_mode=False)
