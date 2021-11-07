import os

import pymysql

# Environment variables can be set on the client or server
# You can also run `cp .env.example .env` and set them locally
# The .env file will be ignored by version control
# This creates a convenient way to test and transports to prod settings
# Intentionally using os.getenv instead of os.environ here so you get python's None if not set
# This will now only connect to the database at boot, not on each call
db_connection = pymysql.connect(
    database=os.getenv("DB_DATABASE"),
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
)


def update(cursor: pymysql.Connection.cursorclass, data: dict) -> None:
    """Data update method responsible for updating the active data record

    Arguments:
        cursor (pymysql.Connection.cursorclas): the established DB cursor
        data (dict): Python dictionary of data to update
    """

    # Triple quotes make the query much easier to read/format
    # your future self will thank you
    query = """
    Update
        employees
    Set
        family_members = %(family_members)s,
        social_status = %(social_status)s,
        gender = %(gender)s,
        date_birth = %(date_birth)s,
        id_number = %(id_number)s,
        mail = %(mail)s,
        name = %(name)s
    Where
        id = %(id)s
    ;
    """

    # Execute the query
    # This method uses the named vairables from the dict
    # Each variable is escaped protecting you from SQL-injection
    cursor.execute(query, data)

    # Let's get this set to the DB
    cursor.commit()


def main() -> None:
    """General controller method
    This could be
        an application entry point for your GUI
        the start routine for Django/Flask/FastAPI
        Something simple like this wrapped in argparse
    """

    # TODO - Gather this from whatever mechanism is needed
    data = {
        "family_members": "",
        "social_status": "",
        "gender": "",
        "date_birth": "",
        "id_number": 0,
        "mail": "",
        "name": "",
        "id": "",
    }

    # Grab an active cursor object
    cursor = db_connection.cursor()

    # We know the DB is the part that can break, so we'll wrap this first
    try:
        update(cursor, data)
        print("Yay this worked")  # Check the DB and give some user feedback
    except pymysql.DatabaseError as e:
        print(str(e))  # Prints the basic error you encountered
        # If you hit this section, get rid of the try/except or use pdb to walk the error
        # There are multiple ways to print the traceback
        # IMHO the easiest is to just not catch the exception

    # This should only really be terminated when the application is done
    db_connection.close()
