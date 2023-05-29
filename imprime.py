import datetime

import classes


def prueba():
    a = classes.dao.UserInDB(username="test", hashed_password="1")
    a.full_name = "Test"

    a.mongo_id = "1"
    a.disabled = False
    a.email = "test@test.com"

    classes.connect_to_users().update_one({"_id": a.mongo_id}, {"$set": a.to_mongo()})


if __name__ == "__main__":
    print("tes", datetime.datetime.now())
