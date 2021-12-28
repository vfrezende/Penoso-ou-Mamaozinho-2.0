import re
import unidecode


def update_session(session, user):
    session["logged_in"] = True
    session["id"] = user["id"]
    session["username"] = user["username"]
    session["name"] = user["name"]
    session["email"] = user["email"]
    session["profile_picture"] = user["picture"]


def sanitizeString(string):
    string = re.sub("ª", " ", string)
    string = re.sub("º", " ", string)
    string = re.sub("°", " ", string)

    # remove all accents
    string = unidecode.unidecode(string)

    # Remove all Markup tags in string
    p = re.compile(r"<.*?>")
    string = p.sub("", string)

    string = re.sub(r"[^A-Za-z0-9]+", "", string)

    return string.lower()
