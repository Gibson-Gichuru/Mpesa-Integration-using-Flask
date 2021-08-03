from app import db
from datetime import datetime


class MpesaCalls(db.Model):

    __tablename__ = "mpesacalls"

    id = db.Columns(db.Integer, primary_key=True)
    timestamp = db.Column(db.Datetime, default=datetime.utcnow)
    ip_address = db.Column(db.String(64))
    caller = db.Column(db.String(64))
    conversation_id = db.Column(db.String(54))
    content = db.Column(db.String(64))


class MpesaCallBacks(db.Model):

    __tablename__ = "mpesacallback"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Datetime, default=datetime.utcnow)
    ip_address = db.Column(db.String(64))
    caller = db.Column(db.String(64))
    conversation = db.Column(db.String(64))
    content = db.Column(db.String(64))


class MpesaPayment(db.Model):

    __tablename__ = "mpesapayment"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2))
    description = db.Column(db.Text)
    reference = db.Column(db.TextField)
    first_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    phone_number = db.Column(db.String(64))
    organization_balance = db.Column(db.Numeric(10, 2))

    def __str__(self):

        return f"<payment PhoneNumber: {self.phone_number} by : {self.first_name}, {self.middle_name}, {self.last_name}>"


