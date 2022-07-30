
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from flask import Flask, render_template
import pymongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_db
collection = db.mars_data


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    inventory = collection.find()

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", collection =collection)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    client.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)
