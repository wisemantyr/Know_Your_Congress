# import libraries
from flask import Flask, render_template, redirect, jsonify
import pymongo
import json

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

@app.route("/")
def index():
    return "Hello, Congress"

@app.route("/members")
def get_members():
    db = client.congress_db
    members_data = db.members.find()
    response = []
    for member in members_data:
        member['_id'] = str(member['_id'])
        response.append(member)
    return jsonify(response)

@app.route("/votes")
def get_votes():
    db = client.congress_db
    votes_data = db.votes.find()
    response = []
    for vote in votes_data:
        vote['_id'] = str(vote['_id'])
        response.append(vote)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
