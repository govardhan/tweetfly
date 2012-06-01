import sys
import MySQLdb
import traceback
from patterns import singleton
from genutils import UVConf
from dbutils import DBCon

@singleton
class UserProfileMgr:
  user_profiles = {}


class UserProfile:
  def create_profile(self, logger, msisdn):
    assert type(msisdn) in (int, long, str, list)

    """phonelist = []
    if(type(msisdn) in (int, long, str)):
      phonelist = [str(msisdn)]
    else:
      phonelist = list
    """
    #prepare sql statement
    db = DBCon().get_connection(logger)
    conf = UVConf();
    l_lang = conf.get("core", "lang")
    l_telcoid = conf.get("core", "telcoid")
    l_query = "INSERT INTO tbl_user_profile(msisdn, user_name, display_name, channel, created_ts, operator_id, lang, privacy) VALUES ('%s','%s','%s',21, now(), '%s', '%s', 'public')"%(msisdn, msisdn, msisdn, l_lang, l_telcoid)
    #l_valuepart = ''
    #for phnum in phonelist:
    #  l_valuepart = l_valuepart + "('%s','%s','%s',now(), '%s', '%s', 'public')"%(phnum, phnum, phnum, l_lang, l_telcoid)
    #l_query = l_query + l_valuepart

    logger.debug("user profile creation query = %s", l_query)

    try:
      cursor = db.cursor()
      cursor.execute(l_query)
    except:
      logger.critical("Failed to run query %s. Terminating now", l_query)
      logger.exception(traceback.print_exc())
      sys.exit(1)
        
  def get_profile(msisdn): pass

