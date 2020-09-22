from dashboard import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(IdUser):
    return Users.query.get(int(IdUser))



class Hall(db.Model):
    IdHall = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), nullable=False)
    Enabled = db.Column(db.Integer, db.ForeignKey('situation.IdSituation'))
    CreatedAt = db.Column(db.DateTime, nullable=False) 
    situation = db.relationship('Situation', backref='Market')


    def __repr__(self) :
        return f"Hall('{self.IdHall}','{self.Name},'{self.Enabled}','{self.CreatedAt}')"



class Role(db.Model):
    IdRole = db.Column(db.Integer, primary_key=True)
    Role = db.Column(db.String(250), nullable=False)
    CreatedAt = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"Role('{self.IdRole}','{self.Role},'{self.CreatedAt}')"

class Users(db.Model, UserMixin):
    IdUser = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(250), nullable=True)
    LastName = db.Column(db.String(250), nullable=True)
    Email = db.Column(db.String(250), nullable=True)
    PhoneNumber = db.Column(db.String(250), nullable=True)
    Address = db.Column(db.String(250), nullable=True)
    Pasword = db.Column(db.String(250), nullable=True)
    CreatedAt = db.Column(db.DateTime, nullable=False) 
    Enabled = db.Column(db.Integer, db.ForeignKey('situation.IdSituation'))
    situation = db.relationship('Situation', backref='Users')

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.IdUser}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except TypeError :
            print('Type error in verify reset token') 
        except Exception as e :
            print("Error '{0}' occurred. Arguments {1}.".format(e.message, e.args))
        finally :
            if user_id is None :
                user_id = None
        return Users.query.get(user_id)
    def __repr__(self) :
        return f"Users('{self.IdUser}','{self.FirstName}','{self.LastName}','{self.Email}','{self.PhoneNumber}','{self.Address}','{self.Pasword}','{self.CreatedAt}','{self.Enabled}')"        

    def get_id(self):
        return (self.IdUser)



class Booking(db.Model):
    IdBooking = db.Column(db.Integer, primary_key=True)
    BookingNumber = db.Column(db.String(250), nullable=True)
    OrganizationName = db.Column(db.String(250), nullable=True)
    Poc = db.Column(db.String(250), nullable=True)
    PhoneNumber = db.Column(db.String(250), nullable=True)
    IdBookingStatus  = db.Column(db.Integer, db.ForeignKey('booking_status.IdBookingStatus'))
    IdUser = db.Column(db.Integer, db.ForeignKey('users.IdUser'))
    IdHall = db.Column(db.Integer, db.ForeignKey('hall.IdHall'))
    Price  = db.Column(db.String(250), nullable=True)
    Bookingtime = db.Column(db.String(250), nullable=True)
    CreatedAt = db.Column(db.DateTime, nullable=False)
    bookingstatus = db.relationship("BookingStatus", backref="Booking")
    user = db.relationship('Users',  backref="Booking")
    hall = db.relationship('Hall',  backref="Booking")



    def __repr__(self) :
        return f"Booking('{self.IdBooking}',{self.BookingNumber}','{self.OrganizationName}','{self.Poc}','{self.PhoneNumber}','{self.IdBookingStatus}','{self.IdUser}','{self.Price}','{self.Bookingtime}','{self.CreatedAt}')"        

class BookingStatus(db.Model):
    IdBookingStatus = db.Column(db.Integer, primary_key=True)
    BookingStatus  = db.Column(db.String(250), nullable=False)
    CreatedAt  = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"BookingStatus('{self.IdBookingStatus}','{self.BookingStatus}','{self.CreatedAt}')"


class Situation(db.Model):
    IdSituation = db.Column(db.Integer, primary_key=True)
    Situation  = db.Column(db.String(250), nullable=False)
    CreatedAt  = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"Situation('{self.IdSituation}','{self.Situation}','{self.CreatedAt}')"
