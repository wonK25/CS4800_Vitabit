from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://yusuncs_db_user:Vky3XrzNoUHJXk0N@lunch-db.mmengdc.mongodb.net/?appName=lunch-db"
client = MongoClient(MONGODB_URI)

db = client["5-dollar"]
collection = db["food"]

# --- WRITE (insert one document) ---
# collection.insert_one({"name": "Panda Express", "price": 10.99, "image_url" : "https://assets.simpleviewinc.com/simpleview/image/upload/c_fill,f_jpg,h_418,q_65,w_600/v1/crm/PalmSpringsCA/2020/06/3511bdf68711b42d370cd30d6b2494e5_cfc7b6e3-b0aa-4d77-b689-10bf9af676a0.jpg"})
# collection.insert_one({"name": "Starbucks", "price": 4.99, "image_url" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc04AHM_-3F1WLk3-DGTOu0FLT0FB8vKYYSQ&s"})
# collection.insert_one({"name": "Roundtable Pizza", "price": 5.99, "image_url" : "https://www.fatbrands.com/wp-content/uploads/2023/03/RTP-RTP_Pizza_OH_Pepperoni_Slice.jpg"})

# --- READ (find one document) ---
for f in collection.find():
    print(f)
