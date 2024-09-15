DEBUG = True

DATABASE = 'homolog'
USERNAME_DB = 'root'
PASSWORD_DB = 'root'
SERVER = 'localhost'

SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE}.db'
#QLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME_DB}:{PASSWORD_DB}@{SERVER}/{DATABASE}'
#SQLALCHEMY_DATABASE_URI = f'postgresql://bibliolink_db_user:6t4rYf7AlOzNvL9wHqd7FHRPsRFwEfEd@dpg-cqmf0kbv2p9s73f9v01g-a.oregon-postgres.render.com/bibliolink_db'





SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY='jfgfghgfhgdgfsdfrtukiluyoiu5453eythjuioipp97yt6563etrytuyiku'