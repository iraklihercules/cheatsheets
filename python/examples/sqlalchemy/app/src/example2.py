from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker, declarative_base


# Replace 'postgresql://username:password@localhost/db_name' with your PostgreSQL connection string
# db_url = 'postgresql://username:password@localhost/db_name'
db_url = "postgresql://user1:pass1@postgres:5432/tutorial"

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Create a session class
Session = sessionmaker(bind=engine)

# Create a declarative base
Base = declarative_base()


# Define a simple data model
class Example(Base):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True)
    name = Column(String)


# Create the table in the database
Base.metadata.create_all(engine)

# Create a session
session = Session()

# Insert a row of data into the table
new_example = Example(name='Example Data')
session.add(new_example)
session.commit()

# Retrieve the information from the table
result = session.query(Example).first()
print("ID:", result.id)
print("Name:", result.name)

result = session.query(Example).all()
for item in result:
    print("ID:", item.id)
    print("Name:", item.name)

# Close the session
session.close()
