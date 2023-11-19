from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.gzip import GZipMiddleware

from graphql_server.core import api_router

app = FastAPI(
    default_response_class=ORJSONResponse
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.include_router(api_router)
