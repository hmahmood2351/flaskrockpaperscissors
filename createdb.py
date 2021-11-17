# from flask.sessions import NullSession
from application import db

db.drop_all()
db.create_all()

# testmatch = Winlose(player='ROCK', opponent='PAPER', result='LOST')
# testmatch2 = Winlose(player='PAPER', opponent='PAPER', result='DRAW')

# db.session.add(testmatch)
# db.session.add(testmatch2)
# db.session.commit()

# allresults = Winlose.query.all()
# print(allresults)