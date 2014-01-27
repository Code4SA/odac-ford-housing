from msg_handler import db
from sqlalchemy.orm import backref


# Create user model. For simplicity, it will store passwords in plain text.
# Obviously that's not right thing to do in real world application.
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username


class Message(db.Model):

    message_id = db.Column(db.Integer, primary_key=True)
    msg_type = db.Column(db.String(4))  # either 'ussd' or 'sms'
    content = db.Column(db.String(180))
    vumi_message_id = db.Column(db.String(100), unique=True)
    conversation_key = db.Column(db.String(100))
    from_addr = db.Column(db.String(100))
    datetime = db.Column(db.DateTime())


class Response(db.Model):

    response_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(180))
    datetime = db.Column(db.DateTime())

    message_id = db.Column(db.Integer, db.ForeignKey('message.message_id'))
    message = db.relationship('Message', backref=backref("responses", order_by=datetime))

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = db.relationship('User')