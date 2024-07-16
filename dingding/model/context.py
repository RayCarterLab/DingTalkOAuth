from pydantic import BaseModel

from dingding.persistence.abstract import Repository
from dingding.service.dingding import DingDingService
from dingding.service.iam import IAMService


class Context(BaseModel):
    repo: Repository
    dingding_srv: DingDingService
    iam_srv: IAMService
    suite_key: str

    class Config:
        arbitrary_types_allowed = True
