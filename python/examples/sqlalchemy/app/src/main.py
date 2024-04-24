# Database queries in Python — SQLAlchemy-PostGRESQL
# https://medium.com/technology-hits/database-queries-in-python-sqlalchemy-postgresql-e90afe0a06b4

from sqlalchemy import create_engine, insert, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# f"postgresql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine("postgresql://user1:pass1@postgres:5432/tutorial")
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)


Base.metadata.create_all(bind=engine)


statements = [
    insert(User).values(name='user1', email='user1@example.com', age=18),
    insert(User).values(name='user2', email='user2@example.com', age=45),
    insert(User).values(name='user3', email='user3@example.com', age=30),
]

with engine.connect() as conn:
    for stmt in statements:
        result = conn.execute(stmt)
    conn.commit()


print("\n-- SELECT ALL")
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.email, user.age)


print("\n-- SELECT FIELDS")
users = session.query(User.id, User.name).all()
for user in users:
    print(user.id, user.name)


print("\n-- ORDER BY")
users = session.query(User).order_by(User.age).all()
for user in users:
    print(user.id, user.name, user.email, user.age)


print("\n-- DISTINCT AGES")
users = session.query(User.age).distinct().all()
for user in users:
    print(user.age)


print("\n-- WHERE > 25")
users = session.query(User).filter(User.age > 25).all()
for user in users:
    print(user.id, user.name, user.email, user.age)
