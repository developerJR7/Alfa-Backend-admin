from . import models

def get_admin_user_by_username(db, username: str):
    # Retorna um usuário fake só pra testar
    class User:
        username = "admin"
        hashed_password = "$2b$12$KIXUjV5F6m1OnfSx9x1XLeq4Nq1sblJ2sM4nGvU9kqD/e3b1z5F0W"  # senha: "admin"
    if username == "admin":
        return User()
    return None
