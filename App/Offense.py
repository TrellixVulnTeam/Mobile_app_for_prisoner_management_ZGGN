import Connect_DB as c_DB


class Offense:
    """
    have class Offense method and properties name.......
    and Get, Set All Properties
    """
    cls = None

    def __init__(self, name: str):
        cls = self
        self.name = name

    def __str__(self):
        print(f'Name: {self.name}')

    def add_offense(self, name: str):
        """Add Offense name In DB and check value"""
        global db
        try:
            Offense(name)
            db = c_DB.connect_DB()
            temp_str = """INSERT INTO Offense('name') VALUES(:n)"""
            db.cursor().execute(temp_str, {"n": name})
            db.commit()
        except Exception as ex:
            raise ex
        finally:
            if db:
                db.close()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if len(n) <= 1:
            raise ValueError("Error: Offense name must be greater than one Character")
        else:
            global db
            try:
                db = c_DB.connect_DB()
                temp_str = """SELECT name FROM Offense WHERE name=:n"""
                if db.cursor().execute(temp_str, {"n": n}).fetchone():
                    raise ValueError("Error: Offense Name is already defined")
                else:
                    self.__name = n
            except ValueError as ex:
                raise ex
            except Exception as ex:
                raise ex
            finally:
                if db:
                    db.close()
