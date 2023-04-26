from flask import Flask, jsonify, request
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
db = create_engine('postgresql://poop402r:dkISUQ3mtL9v@ep-round-darkness-324267.us-east-2.aws.neon.tech/neondb')
Base = declarative_base()

Session = sessionmaker(db)
session = Session()


class ResumeBot(Base):
    __tablename__ = 'resume_bot'
    id = Column(Integer, primary_key=True)
    name_surname = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    education = Column(String, nullable=True)
    lang = Column(ARRAY(String), nullable=True)
    lang_level = Column(ARRAY(String), nullable=True)
    country = Column(String, nullable=True)
    city = Column(String, nullable=True)
    description = Column(String, nullable=True)
    profession = Column(String, nullable=True)
    soft_skills = Column(String, nullable=True)
    tech_skills = Column(String, nullable=True)
    projects = Column(String, nullable=True)
    how_long = Column(ARRAY(String), nullable=True)
    job_description = Column(ARRAY(String), nullable=True)
    past_work = Column(ARRAY(String), nullable=True)
    password = Column(String, nullable=True)


@app.route('/register_user', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    user = ResumeBot(email=email, password=password)
    session.add(user)
    session.commit()
    return jsonify('User successfully registered'), 201



if __name__ == '__main__':
    print('start')
    Base.metadata.create_all(db)
    print('finish')