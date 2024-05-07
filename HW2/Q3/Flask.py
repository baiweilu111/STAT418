from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

# Initialize Flask app
app = Flask(__name__)

# Set up database connection and metadata
engine = create_engine('sqlite:///movies.db')
metadata = MetaData()
metadata.bind = engine
Session = sessionmaker(bind=engine)

# Define the Movies table with autoload from the specified engine
try:
    Movies = Table('Movies', metadata, autoload_with=engine)
except Exception as e:
    print(f"Error loading table: {e}")

# Continue with OMDb API setup and Flask route definitions
OMDB_API_KEY = 'http://www.omdbapi.com/?i=tt3896198&apikey=5c3b7669'
OMDB_BASE_URL = 'http://www.omdbapi.com/'

@app.route('/search', methods=['GET'])
def search_movie():
    title = request.args.get('title')
    movie_type = request.args.get('type')
    year = request.args.get('year')
    plot_length = request.args.get('plot', 'short')

    if not title:
        return jsonify({"error": "Missing title parameter"}), 400

    query_params = {
        'apikey': OMDB_API_KEY,
        't': title,
        'type': movie_type,
        'y': year,
        'plot': plot_length,
        'r': 'json'
    }
    query_params = {k: v for k, v in query_params.items() if v is not None}

    response = requests.get(OMDB_BASE_URL, params=query_params)
    if response.status_code != 200:
        return jsonify({"error": "OMDb API request failed"}), response.status_code

    movie_data = response.json()
    if movie_data.get('Response') == 'False':
        return jsonify({"error": "Movie not found in OMDb"}), 404

    session = Session()
    try:
        stmt = select([Movies]).where(Movies.c.Title == movie_data['Title'])
        movie_in_db = session.execute(stmt).scalar_one_or_none()
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

    if not movie_in_db:
        return Response("Movie not found in database", status=404)
    
    movie_info = f"<movie><title>{movie_in_db.Title}</title><year>{movie_in_db.Release_Year}</year></movie>"
    return Response(movie_info, mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///movies.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    ratings = relationship("Rating", back_populates="user")

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    movie = Column(String)
    rating = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="ratings")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/rating', methods=['POST', 'GET', 'PUT'])
def handle_rating():
    if request.method == 'POST':
        data = request.json
        if not data or 'username' not in data or 'rating' not in data or 'movie' not in data:
            return jsonify({"error": "Missing data"}), 400

        session = Session()
        try:
            user = session.query(User).filter_by(username=data['username']).first()
            if not user:
                user = User(username=data['username'], first_name=data['username'], last_name="")
                session.add(user)
                session.commit()

            new_rating = Rating(movie=data['movie'], rating=data['rating'], user=user)
            session.add(new_rating)
            session.commit()
            return jsonify({"success": "Rating added"}), 201
        except SQLAlchemyError as e:
            session.rollback()
            return jsonify({"error": str(e)}), 500
        finally:
            session.close()
    else:
        return jsonify({"error": "Invalid request method"}), 405

if __name__ == '__main__':
    app.run(debug=True)