import unittest
import MySQLdb
import sys
sys.path.append('/home/surya/myprgms/tweetfly/src')
from number_normalizer import NumNormalizer
#checking if connection is established
class nrmtest1(unittest.TestCase):
  def runTest(self):
    db = DBCon().get_connection(logger)
    self.assertTrue(db)
"""
#checking if it is exiting if there are no rows
class nrmtest2(unittest.TestCase):
  def runTest(self):
    c_query="CREATE TABLE mytable SELECT * FROM tbl_number_normalizer limit 10"
    t_query="truncate table mytable"     
    l_query = "SELECT id, in_pattern, out_pattern, telco_id, channel, description FROM mytable ORDER BY id DESC"
    self.assertRaises(SystemExit)
    d_query="drop table mytable"
#checking for cursor 
class nrmtest3(unittest.TestCase):
  def runTest(self):
    cursor=cursor = db.cursor()
    self.assertTrue(cursor)
#checking if logger has arguments
class nrmtest4(unittest.TestCase):
  def runTest(self):
    logger = none
    self.assertRaises(SystemExit)
#adding a column
class nrmtest5(unittest.TestCase):
  def runTest(self):
    c_query="CREATE TABLE mytable SELECT * FROM tbl_number_normalizer limit 10"
    u_query="alter table mytable add pattern = int(10)"
    self.assertTrue(logger.info)
    d_query="drop table mytable"
#deleting a column
class nrmtest6(unittest.TestCase):
  def runTest(self):
    c_query="CREATE TABLE mytable SELECT * FROM tbl_number_normalizer limit 10"
    u_query="alter table mytable drop in_pattern"
    self.assertTrue(logger.info)
    d_query="drop table mytable"
"""
if __name__ == '__main__':
  unittest.main()




