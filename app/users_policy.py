from flask import current_user

ADMIN_ROLE_ID = 2

def is_admin():
    return current_user.role_id == ADMIN_ROLE_ID

class UsersPolicy:
    def __init__(self, record=None):
        self.record = record
    def edit(self):
        is_edicing_user = current_user.id == self.record.id
        return is_edicing_user