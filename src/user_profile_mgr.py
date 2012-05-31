import sys
import MySQLdb
import traceback
from patterns import singleton
from genutils import UVConf
from dbutils import DBCon

@singleton
class UserProfileMgr:
  logger 
  user_profiles = {}


class UserProfile:
  def create_profile(self, msisdn)
    assert type(msisdn) in (int, long, str, list)

    phonelist = []
    if(type(msisdn) in (int, long, str):
      phonelist = [str(msisdn)]
    else:
      phonelist = list

    

    db = DBCon().get_connection(logger)
    l_query = "INSERT INTO tbl_user_profile(msisdn, user_name, display_name, created_ts, operator_id, lang, privacy) VALUES('%s','%s','%s',now(), '%s', '%s', 'public')"%(phnum, phnum, phnum, l_lang)
    numrows = 0
    try:
      cursor = db.cursor()
      cursor.execute(l_query)
      numrows = int(cursor.rowcount)
      if numrows == 0:
        logger.critical("No rows found [%d] in tbl_number_normalizer. Terminating application now ", numrows)
        sys.exit(1)
      else:
        logger.critical("[%d] rows found in tbl_number_normalizer. loading now ", numrows)
    except:
      logger.critical("Failed to run query %s. Terminating now", l_query)
      logger.exception(traceback.print_exc())
      sys.exit(1)
        
  def get_profile(msisdn)
