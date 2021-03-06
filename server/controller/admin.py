from db.dbconn import curs


class AdminInfo:

    def __init__(self, person_id):
        self.id = person_id

    def CheckAuth(self):
        error = False
        AuthQuery = "SELECT `auth` FROM `User` WHERE \
                     `person_id` = %s;"
        curs.execute(AuthQuery, (self.id, ))
        auth_ = curs.fetchone()
        if auth_[0] == 0:
            error = True
        return error
