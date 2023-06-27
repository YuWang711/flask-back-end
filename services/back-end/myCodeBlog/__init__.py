
from ApiCore import APIFlaskWrapper

from HelloWorld import HelloWorld

def create_app():
    MyApp = APIFlaskWrapper("__name__")

    MyApp.addBlueprints(HelloWorld)
    return MyApp

app = create_app().app


if __name__ == '__main__':
    app.runServer()
