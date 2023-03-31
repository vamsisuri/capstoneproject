import logging
logging.basicConfig(filename='..//Logger//capestone.log',level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
from searchfileindrives.searchfiles import SearchFilesDrives
from SearchinDB.DBConnection import DatabaseConnection
from SearchinDB.SearchFilepath import SearchFile
from CapestoneExceptions.MysqlException import MySqlError
from SearchinDB.InsertData import InsertFileDB
import openpyxl as xl
import mysql.connector
import time

def userdata():
    dir=input("Enter the drive like c:// d:// \n" )
    filename=input("Enter the file name with extension like demo.txt \n")
    logging.info(f"Drive name{dir} file name{filename}")
    dbobj=SearchFile()
    logging.info(f"class used {SearchFile.__name__}")
    wb=xl.load_workbook("C://testdata//Testfiles.xlsx")
    ws=wb.active
    try:
        dbobj.Connect("localhost",'root','Lava@2000','myhcl',3306)
        logging.info("myhcl database is connected")
        result=dbobj.Search(filename)
    except mysql.connector.Error as err:
        raise MySqlError(f'{err.msg}',err.errno)
        logging.exception(err,exc_info=True)
    finally:
            dbobj.connect.close()

    if len(result)==0:
        print("Not Found in Database")
        print("Now Searching in Drives...")
        logging.info("Not Found in Database")
        logging.info("Now Searching in Drives")
        start_time=time.time()
        obj=SearchFilesDrives()
        logging.info(f' for searching in drive  {SearchFilesDrives.__name__}is used')
        files=obj.searchfiles(dir,filename)
        ws.cell(row=1,column=1).value=str(files)
        wb.save("C://testdata//Testfiles.xlsx")
        wb.close()
        insertobj=InsertFileDB()
        insertobj.insert(files)
        print(files)
        obj.start()
        # obj.join()
        end_time=time.time()
        logging.info(f'time taken{end_time-start_time}')
        logging.info("Ending")
        print(end_time-start_time)
    else:
        result="found in database!"
        print(result)
userdata()
