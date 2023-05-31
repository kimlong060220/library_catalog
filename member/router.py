from fastapi import APIRouter
from typing import List

from member.schema import Member, MemberCreate, MemberUpdate
from member.service import MemberService

router = APIRouter()
member_service = MemberService()

@router.get("/members", response_model=List[Member])
def get_members():
    members = member_service.get_members()
    return members

@router.get("/members/{member_id}", response_model=Member)
def get_member(member_id: int):
    member = member_service.get_member(member_id)
    return member

@router.post("/members", response_model=Member)
def create_member(member_data: MemberCreate):
    member = member_service.create_member(member_data)
    return member

@router.put("/members/{member_id}", response_model=Member)
def update_member(member_id: int, member_data: MemberUpdate):
    member = member_service.update_member(member_id, member_data)
    return member

@router.delete("/members/{member_id}")
def delete_member(member_id: int):
    member_service.delete_member(member_id)
    return {"message": "Member deleted successfully"}
