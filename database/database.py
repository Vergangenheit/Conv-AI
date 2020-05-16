# import pyrebase
# import db_config


# firebase = pyrebase.initialize_app(db_config.config)

# db = firebase.database()

# def push_personality(personality):
#     firebase = pyrebase.initialize_app(db_config.config)

#     db = firebase.database()
#     # check if the child contains something
#     if db.child("personalities").child("personality").get().val() is None:
#         db.child("personalities").push({"personality": personality})

#     else:
#         db.child("personalities").update({"personality": personality})
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time


# db.collection('personalities').document('personality').set({
#     '0': 'I love to play poker',
#     '1': 'I live in Massachussets',
#     '2': 'I went to harvard',
#     '3': 'I am a smart ass'
# })
#query document
# x = db.collection('personalities').get()
# for i in x:
#     print(i.to_dict())
#update document
# db.collection('personalities').document('personality').update({
#     '0': 'I love to play bass guitar',
#     '1': 'I live in Toulon',
#     '2': 'I went to hell',
#     '3': 'I am a crooked ass'
# })

def push_personality(personality):

    global db
    cred = credentials.Certificate('conv-ai/database/ServiceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    if db.collection("personalities").document("personality").get().to_dict() is None:
        db.collection("personalities").document("personality").set({"personality": personality})

    else:
        db.collection("personalities").document("personality").update({"personality": personality})

def update_history(out_ids):
    # cred = credentials.Certificate('conv-ai/database/ServiceAccountKey.json')
    # default_app = firebase_admin.initialize_app(cred)
    # db = firestore.client()

    db.collection("history").document().set({'msg': out_ids, 'timestamp': firestore.SERVER_TIMESTAMP})

def get_history():
    cred = credentials.Certificate('conv-ai/database/ServiceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    history = db.collection("history").get().to_dict()

    return history

def clear_history():
    cred = credentials.Certificate('./database/ServiceAccountKey.json')
    default_app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    
    docs = db.collection("history").stream()
    
    if docs is not None:
        for doc in docs:
            doc.reference.delete()

class DataBase(object):
    def __init__(self):
        self.cred = credentials.Certificate('./database/ServiceAccountKey.json')
        self.default_app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def push_personality(self, personality):

        if self.db.collection("personalities").document("personality").get().to_dict() is None:
            self.db.collection("personalities").document("personality").set({"personality": personality})

        else:
            self.db.collection("personalities").document("personality").update({"personality": personality})

    def update_history(self, out_ids):
        self.db.collection("history").document().set({'msg': out_ids, 'timestamp': firestore.SERVER_TIMESTAMP})

    def clear_history(self):
        docs = self.db.collection("history").stream()
        if docs is not None:
            for doc in docs:
                doc.reference.delete()
    

    



if __name__ == "__main__":
    clear_history()


    

