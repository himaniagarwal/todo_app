from todoapp.config.database import get_db


class DBSessionContext(object):
    def __init__(self):
        self.db = get_db()
