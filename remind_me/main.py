import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template

app = fastapi.FastAPI()
fastapi_chameleon.global_init(template_folder='templates')

@app.get('/')
@template(template_file='base.html')
def index():
    return {
        'username': 'jesse'
    }


if __name__ == '__main__':
    uvicorn.run(app)