# from firebase import firebase
# import config

# def upload_personality(personality):
#     # Create the connection to our Firebase database
#     DBConn = firebase.FirebaseApplication(config.dsn, None)

#     result = DBConn.post('/personality', personality)
import pyrebase
import db_config


firebase = pyrebase.initialize_app(db_config.config)

db = firebase.database()

def push_personality(personality):
    firebase = pyrebase.initialize_app(db_config.config)

    db = firebase.database()
    # check if the child contains something
    if db.child("personalities").child("personality").get().val() is None:
        db.child("personalities").push({"personality": personality})

    else:
        db.child("personalities").update({"personality": personality})

