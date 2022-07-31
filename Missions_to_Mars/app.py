
import requests
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from flask import Flask, render_template, redirect, url_for
import pymongo
import scrape_mars
from flask_pymongo import PyMongo


app = Flask(__name__)
# ------------------This commented code failed------------------------------
# # setup mongo connection
# conn = "mongodb://localhost:27017"
# client = pymongo.MongoClient(conn)

# # connect to mongo db and collection
# db = client.mars_db
# collection = db.mars_data


# @app.route("/")
# def index():
#     # write a statement that finds all the items in the db and sets it to a variable
#     all_items = collection.find()

#     # render an index.html template and pass it the data you retrieved from the database
#     return render_template("index.html", all_items=all_items)
# Use flask_pymongo to set up mongo connection


app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    # Run the scrape function
    # mars_data = scrape_mars.Mars_news()
    # mars_data = scrape_mars.mars_image()
    mars_data = scrape_mars.Marsfacts()
    # mars_data = scrape_mars.mars_hemispheres()
    # Update the Mongo database using update and upsert=True
    # client.db.collection.update({}, mars_data, upsert=True)
    
    # This line needs fixing-----
    #  pymongo.errors.WriteError: Modifiers operate on fields but we found type string instead.
    mars.update_one({}, {"$set": mars_data}, upsert=True) 


    # Redirect back to home page
    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True)
