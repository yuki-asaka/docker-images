import logging

from fastapi import FastAPI

from api import ping

log = logging.getLogger('uvicorn')


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info('Starting up...')


@app.on_event('shutdown')
async def shutdown_event():
    log.info('Shutting down...')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
