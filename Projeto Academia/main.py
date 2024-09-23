from gui import Application
from db import Database

DATABASE_URL = "postgresql://postgres:Benedito21@localhost/postgres"

def main():
    db = Database(DATABASE_URL)
    db.create_table()

    app = Application(db)
    app.mainloop()

    db.close()

if __name__ == "__main__":
    main()

# Testando Sprint 1