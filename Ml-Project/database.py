import pymysql as sql


class Database:

    # * instance of class
    __instance = None

    @staticmethod
    def getImages():
        Database.__instance.__cursor.execute('SELECT * FROM IMAGE')

        return Database.__instance.__cursor.fetchall()

    # * method for getting details after detection
    @staticmethod
    def getCitizenDetailsAfterDetection(id):
        Database.__instance.__cursor.execute(
            f'SELECT * FROM CITIZEN WHERE ID = {id}')

        return Database.__instance.__cursor.fetchall()

    # * method to get instance
    @staticmethod
    def getInstance():
        if Database.__instance == None:
            Database()
        else:
            return Database.__instance

    @staticmethod
    def citizenDetails(searchValue, value):
        if searchValue == 1:
            Database.__instance.__cursor.execute(
                f''' 
                SELECT * FROM CITIZEN WHERE ID = {int(value)}
                '''
            )
        elif searchValue == 2:
            Database.__instance.__cursor.execute(
                f"""
               SELECT * FROM citizen WHERE name LIKE ('{value}%') OR name LIKE ('%{value}')
                """
            )

        else:
            Database.__instance.__cursor.execute(
                f"""
                SELECT * FROM CITIZEN WHERE MOBILE LIKE '{value}%' or MOBILE LIKE ('%{value}')
                """
            )

        # * fetch data
        return Database.__instance.__cursor.fetchall()

    @staticmethod
    def getHospitalDetails(name, date):
        Database.__instance.__cursor.execute(f"""
            SELECT ID,NAME,LOCATION,TYPE FROM VACCINE_CENTER
            WHERE NAME = '{name}'
        """)

        hospitalData = Database.__instance.__cursor.fetchall()

        Database.__instance.__cursor.execute(f"""
        SELECT COUNT(*) FROM CITIZEN WHERE FIRST_DOZE = STR_TO_DATE('{date}','%Y-%m-%d') OR SECOND_DOZE = STR_TO_DATE('{date}','%Y-%m-%d') 
        """)

        count = Database.__instance.__cursor.fetchall()

        return hospitalData[0], count[0]

    @staticmethod
    def login(user, password):
        Database.__instance.__cursor.execute(
            f"SELECT * from Admin where user = '{user}'")
        result = Database.__instance.__cursor.fetchall()

        if result == ():
            return None

        else:
            return result[0][1] == password, result[0][0]

    @staticmethod
    def loginVaccine(id, password):
        Database.__instance.__cursor.execute(
            f"SELECT id,password from VACCINE_CENTER where id = {id}")
        result = Database.__instance.__cursor.fetchall()

        if result == ():
            return None

        else:
            return result[0][1] == password

    @staticmethod
    def returnHospitalsName():
        Database.__instance.__cursor.execute('SELECT NAME FROM VACCINE_CENTER')

        names = Database.__instance.__cursor.fetchall()
        ListOfNames = []

        for name in names:
            ListOfNames.append(name[0])

        return ListOfNames

    def __init__(self):
        if Database.__instance == None:
            Database.__instance = self

            self.__conn = sql.connect(
                host='13.232.35.56', password='palak@123', database='palak', user='palak')
            self.__cursor = Database.__instance.__conn.cursor()

    # * method to dispose database

    @staticmethod
    def disposeDatabase():
        Database.__instance.__cursor.close()
        Database.__instance.__conn.close()
