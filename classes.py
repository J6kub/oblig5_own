from app import full_db

def saveAllDb():
    for i in full_db:
        full_db[i].save()

