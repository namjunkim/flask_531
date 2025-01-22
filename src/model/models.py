from src.config.db_config import db

class Users(db.Model):

    __table_args__ = {'schema': '531_srv'}

    id = db.Column(db.String(11), primary_key=True)
    #username = db.Column(db.String(100), unique=True, nullable=False)
    e_mail = db.Column(db.String(50), nullable=False)
    #name = db.Column(db.String(128))
    def to_dict(self):
        return {
            'id': self.id,
            'e_mail': self.e_mail
    }