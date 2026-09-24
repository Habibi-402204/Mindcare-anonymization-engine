import hashlib
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mindcare_db"]

def hide_pii(value):
    return hashlib.sha256(str(value).encode()).hexdigest()[:16]

def anonymize():
    moods = list(db["mood_logs"].find({}))
    clean = []
    for m in moods:
        clean.append({
            "user_hash": hide_pii(m.get("email")),
            "mood": m.get("mood_type"),
            "score": m.get("mood_score")
        })
    print(clean)
    return clean

anonymize()
