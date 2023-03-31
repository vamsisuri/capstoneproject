
from SearchinDB.DBConnection  import DatabaseConnection
class SearchFile(DatabaseConnection):
    def Search(self,filename):
        print("Searching in Database ....")
        self.filename=filename
        #sql="select * from fileinfo where filename=%s"
        sql="""select * from fileinfo where filename like '%{0}'""".format(filename)
        self.cur.execute(sql)
        data=self.cur.fetchall()
        return data