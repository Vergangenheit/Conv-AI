import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time


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
        self.cred = credentials.Certificate('Conv-AI/database/ServiceAccountKey.json')
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
        done_looping = False
        while not done_looping:
            try:
                doc = next(docs)
            except StopIteration:
                done_looping = True
            else:
                doc.reference.delete()


if __name__ == "__main__":
    db = DataBase()
    db.update_history("what's up man?")
