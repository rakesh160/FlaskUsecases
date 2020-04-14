from app.models import *

# add admin & users
user=User(id=1,username='admin',fullname='admin')
user.set_password('admin')
db.session.add(user)


db.session.commit()