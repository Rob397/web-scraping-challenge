from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
#  example db = client.team_db

# Drops collection if available to remove duplicates
#example  db.team.drop()



# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route('/')
def index():
    # Store the entire team collection in a list
    # teams = list(db.team.find())
    # print(teams)

    # Return the template with the teams list passed in
    return render_template('index.html', teams=teams)



# ------------------------------Store the return value in Mongo as a Python dictionary



if __name__ == "__main__":
    app.run(debug=True)
