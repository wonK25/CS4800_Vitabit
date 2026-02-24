from flask import Flask, jsonify, render_template, request
import os
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
import re

load_dotenv()

# Database Connection for Vitabit Project
# Make sure your MongoDB cluster is 'Online' before running this script
MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set. Copy .env.example to .env and add your MongoDB URI.")

client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)

# Selecting the Database and Collection for Supplements
db = client["Vitabit-Database"]
collection = db["supplements"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
@app.route("/search/<keyword>")
def search_vitamin_info(keyword=None):
    """
    Search for supplements by matching the keyword against 
    both the 'name' and 'benefit' fields in the database.
    """
    result = []
    keyword = (keyword or request.args.get("keyword", "")).strip()
    if not keyword:
        return jsonify([])
    
    # Query: Find items where either the name OR benefit contains the keyword
    # "$or" allows searching across multiple fields
    # "$options": "i" makes the search case-insensitive (e.g., 'vitamin' matches 'Vitamin')
    escaped_keyword = re.escape(keyword)
    query = {
        "$or": [
            {"name": {"$regex": escaped_keyword, "$options": "i"}},
            {"benefit": {"$regex": escaped_keyword, "$options": "i"}}
        ]
    }

    try:
        for item in collection.find(query):
            # Convert MongoDB ObjectId to string for JSON serialization
            item["_id"] = str(item["_id"])
            result.append(item)
    except PyMongoError as exc:
        print(f"MongoDB query failed: {exc}")
        return jsonify({"error": "Database query failed"}), 503

    print(f"Search query: '{keyword}' | Found: {len(result)} items")
    return jsonify(result)



if __name__ == "__main__":
    # Start the server on port 5050
    app.run(host="0.0.0.0", port=5050, debug=True)
