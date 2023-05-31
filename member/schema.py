from pydantic import BaseModel
from datetime import date

class Member(BaseModel):
    name: str
    membership_id: int
    email: str
    join_date: date


class MemberCreate(Member):
    pass


class MemberUpdate(Member):
    pass
