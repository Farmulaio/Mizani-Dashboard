from dashboard import db, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(IdUser):
    return Users.query.get(int(IdUser))



class Categories(db.Model):
    IdCategory = db.Column(db.Integer, primary_key=True)
    Category  = db.Column(db.String(250), nullable=False)
    Enabled = db.Column(db.Integer, db.ForeignKey('situation.IdSituation'))
    CreatedAt = db.Column(db.DateTime, nullable=False) 
    situation = db.relationship('Situation', backref='Categories')


    def __repr__(self) :
        return f"Categories('{self.IdCategory}','{self.Category },'{self.Enabled}','{self.CreatedAt}')"



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



class Products(db.Model):
    IdProduct = db.Column(db.Integer, primary_key=True)
    Name  = db.Column(db.String(250), nullable=True)
    Description  = db.Column(db.String(250), nullable=True)
    Benefit  = db.Column(db.String(250), nullable=True)
    Usage  = db.Column(db.String(250), nullable=True)
    ImageUrl = db.Column(db.String(250), nullable=True)
    IdSize  = db.Column(db.Integer, db.ForeignKey('size.IdSize'))
    IdUser = db.Column(db.Integer, db.ForeignKey('users.IdUser'))
    Enabled = db.Column(db.Integer, db.ForeignKey('situation.IdSituation'))
    IdCategory = db.Column(db.Integer, db.ForeignKey('categories.IdCategory'))
    Price  = db.Column(db.String(250), nullable=True)
    CreatedAt = db.Column(db.DateTime, nullable=False)
    size = db.relationship("Size", backref="Products")
    user = db.relationship('Users',  backref="Products")
    cat = db.relationship('Categories',  backref="Products")
    situation = db.relationship('Situation', backref='Products')



    def __repr__(self) :
        return f"Products('{self.IdProduct}',{self.Name}','{self.Description}','{self.Benefit}','{self.Usage}','{self.ImageUrl}','{self.IdSize}','{self.Enabled}','{self.IdUser}','{self.IdCategory}','{self.Price}','{self.CreatedAt}')"        
    
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
            'IdProduct': self.IdProduct,
            'Name' : self.Name,
            'Description' : self.Description,
            'Benefit' : self.Benefit,
            'ImageUrl' : self.ImageUrl,
            'IdSize' : self.size.Size,
            'IdCategory' : self.cat.Category,
            'Enabled' : self.Enabled,
            'Price' : self.Price,
            'CreatedAt' : self.CreatedAt
       }



class Size(db.Model):
    IdSize  = db.Column(db.Integer, primary_key=True)
    Size   = db.Column(db.String(250), nullable=False)
    Enabled = db.Column(db.Integer, db.ForeignKey('situation.IdSituation'))
    CreatedAt  = db.Column(db.DateTime, nullable=False) 
    situation = db.relationship('Situation', backref='Size')

    def __repr__(self) :
        return f"Portion('{self.IdSize }','{self.Enabled }','{self.Size }','{self.CreatedAt}')"


class Situation(db.Model):
    IdSituation = db.Column(db.Integer, primary_key=True)
    Situation  = db.Column(db.String(250), nullable=False)
    CreatedAt  = db.Column(db.DateTime, nullable=False) 

    def __repr__(self) :
        return f"Situation('{self.IdSituation}','{self.Situation}','{self.CreatedAt}')"
