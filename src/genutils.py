
import os,sys,io,logging
import traceback
import ConfigParser
from patterns import singleton

@singleton
class UVEnvi:
  pass

@singleton
class UVConf:
  uvconf = None

  def init(self, app_logger, app_conf_filename):
    #try:
    #  uv_home_path = os.environ['UV_HOME']
    #except KeyError:
    #  uv_home_path = '/usr/local/uv/'

    try:
      self.uvconf = ConfigParser.RawConfigParser()
      self.uvconf.read(app_conf_filename)
      app_logger.info("UVConf initialization done for conf file %s.", app_conf_filename)
      app_logger.info("uvconf sections are ")

      for sec in self.uvconf.sections():
        app_logger.info(("%s"% sec).center(60,'*'))
        #app_logger.info("***************** %25s *************** ", sec)
        for option in self.uvconf.options(sec):
          app_logger.info("%16s => %-16s ", option, self.uvconf.get(sec, option))

    except:
      app_logger.critical("UVConf initialization failed for conf file %s. Terminating now. Traceback ...", app_conf_filename)
      app_logger.exception(traceback.print_exc())
      sys.exit(1)


  def get(self, p_key):
    return self.uvconf.get("core", p_key)

  def get(self, p_section, p_key):
    return self.uvconf.get(p_section, p_key)

  def getint(self, p_section, p_key):
    return self.uvconf.getint(p_section, p_key)

  def getfloat(self, p_section, p_key):
    return self.uvconf.getfloat(p_section, p_key)

  def getboolean(self, p_section, p_key):
    return self.uvconf.getboolean(p_section, p_key)


def init_logger(app_name, log_filename, log_level=logging.DEBUG):
  try:
    sys.stderr.write('app name = %s file name = %s log level = %d\n' %(app_name, log_filename, log_level))
    sys.stderr.flush()
    logger = logging.getLogger(app_name)
    hdlr = logging.FileHandler(log_filename)  
    formatter = logging.Formatter('%(asctime)s|%(process)-5d|%(thread)d|%(filename)-16s|%(funcName)-16s|%(lineno)4d|%(levelname)-8s| %(message)s')
    #formatter = logging.Formatter('%(asctime)s|%(process)-5d|%(thread)d|%(name)s|%(filename)-14s|%(funcName)s|%(lineno)4d|%(levelname)-7s|%(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(log_level)
    return logger
  except:
    sys.stderr.write("logger initialization failed. Terminating application now. Traceback ...")
    sys.stderr.write(traceback.print_exc())
    sys.stderr.flush()
    sys.exit(1)


