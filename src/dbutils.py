import re,os,sys
import MySQLdb
import traceback
from patterns import singleton
from genutils import UVConf


@singleton
class DBCon:
  db = None
  def get_connection(self, logger):
    conf = UVConf();
    l_host = conf.get("db","coredb_host")
    l_user = conf.get("db","coredb_user")
    l_passwd = conf.get("db","coredb_passwd")
    l_db = conf.get("db","coredb_name")
    logger.info("Mysql Connection setup params - host = %s, user = %s, passwd = %s, db = %s", l_host, l_user, l_passwd, l_db)

    try:
      self.db = MySQLdb.connect(host=l_host, user=l_user, passwd=l_passwd, db=l_db) 
      logger.info("connected to database. %s", str(self.db))
    except:
      logger.critical("Failed to connect to database. Terminating now. Traceback ...")
      logger.exception(traceback.print_exc())
      sys.exit(1)
    return self.db
