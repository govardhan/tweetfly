
import re,os,sys
import MySQLdb

class NumNormalizer:

  def load_rules_from_db(self):
    db = MySQLdb.connect(host="localhost", user="root", passwd="root",db="uv_core")
    cursor = db.cursor()
    cursor.execute("SELECT id, in_pattern, out_pattern, telco_id, channel, description FROM tbl_number_normalizer")
    numrows = int(cursor.rowcount)
    if numrows == 0:
      logger
    for x in range(0,numrows):
      row = cursor.fetchone()
      print row[0], "-->", row[1]

  #def normalizestr(patrn,text,rep):
  def normalize(msisdn):
    match= re.search(patrn,text)
    if match: 
      print 'match found' , match.group()
      replacement= re.sub(patrn,rep,text)
      return replacement
    else: 
      print 'not found'
      return text
    
