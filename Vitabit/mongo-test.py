from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set. Copy .env.example to .env and add your MongoDB URI.")

client = MongoClient(MONGODB_URI)

db = client["Vitabit-Database"]
collection = db["supplements"]

# --- WRITE (Insert supplement data into MongoDB) ---

# 1. Replace supplement data with a clean seed set
data = [
    {
        "name": "Vitamin C",
        "benefit": "Immune support & Antioxidant",
        "how_to_take": "Take 1 tablet daily after a meal",
        "male_daily_intake": "90 mg/day",
        "female_daily_intake": "75 mg/day",
        "intake_note": "UL (upper limit): 2000 mg/day. High doses may cause GI upset.",
        "image_url": "/static/images/vitamin-c.svg"
    },
    {
        "name": "Magnesium",
        "benefit": "Muscle relaxation & Better sleep",
        "how_to_take": "Take 1 capsule before bedtime",
        "male_daily_intake": "400-420 mg/day",
        "female_daily_intake": "310-320 mg/day",
        "intake_note": "Supplemental UL is 350 mg/day from non-food sources due to diarrhea risk.",
        "image_url": "/static/images/magnesium.svg"
    },
    {
        "name": "Vitamin D3",
        "benefit": "Bone health & Mood boost",
        "how_to_take": "Take with a meal containing fat",
        "male_daily_intake": "600 IU/day (15 mcg/day)",
        "female_daily_intake": "600 IU/day (15 mcg/day)",
        "intake_note": "Adults 71+ often use 800 IU/day. Check blood 25(OH)D when supplementing long term.",
        "image_url": "/static/images/vitamin-d3.svg"
    }
]

collection.delete_many({})
collection.insert_many(data)

print("Supplement data reset complete.")

# --- READ (find one document) ---
for f in collection.find():
    print(f)
