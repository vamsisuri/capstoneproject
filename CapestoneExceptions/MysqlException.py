import mysql.connector
class MySqlError(Exception):
    def __init__(self,message,err_no):
        super().__init__(message)
        self.err_num=err_no


