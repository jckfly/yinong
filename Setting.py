import pymysql
class Setting:
    def __init__(self):
        self.localhost='127.0.0.1'
        self.user='root'
        self.passed='tjn.12345'
        self.database='test'
        self.port=3306
    def connect(self):
        self.db=pymysql.connect(host=self.localhost,user=self.user,passwd=self.passed,database=self.database,port=self.port)
        self.corsor=self.db.cursor()
    def CreateDatabases(self,name='test'):
      sql='Create database if not exists %s',name
      self.corsor.execute(sql)
      self.db.commit()
    def CreateTable(self,table='word'):
        sql='create table if not exists %s (words varchar(30) PRIMARY KEY,number int)',table
        self.corsor.execute(sql)
        self.db.commit()
    def get_db_corsor(self):
        return self.db,self.corsor

        