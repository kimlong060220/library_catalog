from typing import List, Optional

from data.database import Database
from member.schema import Member, MemberCreate, MemberUpdate

class MemberService:
    def __init__(self):
        self.db = Database()

    def get_members(self) -> List[Member]:
        query = "SELECT * FROM members"
        members = self.db.execute_query(query)
        return members

    def get_member(self, member_id: int) -> Optional[Member]:
        query = "SELECT * FROM members WHERE id = %s"
        params = (member_id,)
        member = self.db.execute_query(query, params)
        return member[0] if member else None

    def create_member(self, member_data: MemberCreate) -> Member:
        query = "INSERT INTO members (name, email, join_date) VALUES (%s, %s, %s)"
        params = (member_data.name, member_data.email, member_data.join_date)
        member_id = self.db.execute_query(query, params)
        member = Member(id=member_id, **member_data.dict())
        return member

    def update_member(self, member_id: int, member_data: MemberUpdate) -> Optional[Member]:
        query = "UPDATE members SET name = %s, email = %s, join_date = %s WHERE id = %s"
        params = (member_data.name, member_data.email, member_data.join_date, member_id)
        rows_affected = self.db.execute_query(query, params)
        if rows_affected > 0:
            member = Member(id=member_id, **member_data.dict())
            return member
        return None

    def delete_member(self, member_id: int) -> bool:
        query = "DELETE FROM members WHERE id = %s"
        params = (member_id,)
        rows_affected = self.db.execute_query(query, params)
        return rows_affected > 0
