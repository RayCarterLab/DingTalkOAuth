from starlette.middleware.base import BaseHTTPMiddleware

from dingding.middleware.deploy import DISPATCH


class DBSessionMiddleware(BaseHTTPMiddleware):
    dispatch = DISPATCH
