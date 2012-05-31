import sys
import MySQLdb
import traceback
from patterns import singleton
from genutils import UVConf
from dbutils import DBCon

@singleton
class NumNormalizer:
  normalize_rules = []

  def load_rules_from_db(self, *args):
    logger = None
    try:
      logger = args[0]
    except:
      sys.stderr.write("Expecting logger into first explicit argument in NumNormalizer::load_rules_from_db. Parameter is missing or not valid. Terminating")
      sys.stderr.write(traceback.print_exc())
      sys.stderr.flush()
      sys.exit(1)

    db = DBCon().get_connection(logger)
    l_query = "SELECT id, in_pattern, out_pattern, telco_id, channel, description FROM tbl_number_normalizer ORDER BY id DESC"
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
        
    for iter in range(0,numrows):
      row = cursor.fetchone()
      logger.info("id = %d, in_pattern = %s, out_pattern = %s, telco_id = %s, channel = %s, description = %s ", int(row[0]), row[1], row[2], row[3], row[4], row[5])
      self.normalize_rules.append(row)
    logger.info("%d normalized rules loaded successfully", numrows)

  def normalize(msisdn, telco_id = ".*", channel = ".*"):
    pass
   

