
import os,sys,io,logging
import ConfigParser
from patterns import singleton

@singleton
class UVEnvi:
  pass

@singleton
class UVConf:
  def __inint__(self, app_logger, app_conf_filename):
    #try:
    #  uv_home_path = os.environ['UV_HOME']
    #except KeyError:
    #  uv_home_path = '/usr/local/uv/'

    try:
      uvconf = ConfigParser.RawConfigParser()
      uvconfig.read(app_conf_filename)
    except:
      sys.stderr.write("UVConf initialization failed")
      sys.exit(1)
    

def init_log(app_name, log_filename, log_level=logging.DEBUG):
  logger = logging.getLogger(app_name)
  hdlr = logging.FileHandler(log_filename)  
  formatter = logging.Formatter('%(asctime)s|%(process)-5d|%(thread)d|%(name)s|%(filename)s|%(func)s|%(levelname)s|%(message)s')
  hdlr.setFormatter(formatter)
  logger.addHandler(hdlr)
  logger.setLevel(log_level)
  return logger
  
  
