from msg_handler import db, app
from msg_handler.models import User


def rebuild_db():

    db.drop_all()
    db.create_all()
    test_user = User(email="admin", password=hash(app.config['ADMIN_PASSWORD']))
    db.session.add(test_user)

    db.session.commit()
    return

if __name__ == "__main__":
    rebuild_db()