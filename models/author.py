from .__init__ import conn, cursor
class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.add_to_database()

    def __repr__(self):
        return f'<Author {self.name}>'
    
    def add_to_database(self):
        sql = """
            INSERT INTO authors (id, name)
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.id, self.name))
        conn.commit()
    
    @property
    def id(self):
        self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("Id must be an integer.")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            if not hasattr(Author, name):
                self._name = name
            else:
                raise AttributeError("Cannot change the name of the author after instantiation.")
        else:
            raise ValueError("Name must be a non-empty string.")