from firebase import firebase
import config

def upload_personality(personality):
    # Create the connection to our Firebase database
    DBConn = firebase.FirebaseApplication(config.dsn, None)

    result = DBConn.post('/personality', personality)
