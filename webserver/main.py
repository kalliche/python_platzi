import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Creamos una instancia de la libreria
app = FastAPI()

# agragamos un decorador o especificamos la ruta
@app.get('/')   # ruta principal
def get_list():
    return [1,2,3,4,5]

@app.get('/contact', response_class=HTMLResponse)    # ruta de contqcto
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>Soy un parerafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()