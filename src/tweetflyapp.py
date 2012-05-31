import sys,os
import logging
from patterns import singleton
from genutils import UVConf
from number_normalizer import NumNormalizer
import genutils

@singleton
class TweetFlyApp:
  app_logger = None
  log_filename = "/usr/local/uv/log/tweetfly.log"
  conf_filename = "/usr/local/uv/conf/tweetfly.conf"
  log_level = logging.DEBUG
  app_conf = None
  normalizer = None

  def init(self, p_conf_filename, p_log_filename, p_log_level):
    #TODO validate log_level
    self.app_logger = genutils.init_logger(__name__, p_log_filename, p_log_level);
    self.app_logger.info("TweetFlyApp logger initialized" )
    self.app_logger.info("p_conf_filename=%s p_log_filename=%s p_log_level=%s" ,p_conf_filename, p_log_filename ,str(p_log_level)  )
    #check log_filename and its path existance
    if ( False == os.path.exists(p_conf_filename) ):
      self.app_logger.critical("Configuration file %s does not exists. Terminating application now", p_conf_filename)
      sys.exit(1)

    if ( False == os.path.exists(os.path.dirname(p_log_filename)) ):
      self.app_logger.warning("Log directory %s does not exists. Creating new directory", os.path.dirname(p_log_filename))
      os.makedirs(os.path.dirname(p_log_filename))
      
      
    conf_filename = p_conf_filename
    self.app_logger.info("Initializing TweetFlyApp with configuration file %s", conf_filename )
    self.app_conf = UVConf()
    self.app_conf.init(self.app_logger, conf_filename);
    self.app_logger.info("TweetFlyApp configuration initialization done")

    #Loading normalization rules
    self.normalizer = NumNormalizer()
    self.normalizer.load_rules_from_db(self.app_logger) 

  def start(self):
    #TODO Initialize TweetStreamListner
    #TODO Authenticate
    #TODO Wait for updates
    for i in range(10):
      self.app_logger.info("I am running now - %d" % i)
    pass

  def on_tweet_update(self):
    #TODO Write tweet into db
    pass
  

def main(argv):
  #Looks like no additional configuration parameters
  l_conf_filename = '/usr/local/uv/conf/tweetfly.conf'
  l_log_filename = "/usr/local/uv/log/tweetfly.log"
  l_log_level = logging.DEBUG
  sys.stderr.write("l_conf_filename="+ l_conf_filename + " l_log_filename=" + l_log_filename + " l_log_level="+str(l_log_level)+ "\n")
  sys.stderr.flush()
    
  tweet_fly_app = TweetFlyApp()
  tweet_fly_app.init(l_conf_filename, l_log_filename, l_log_level)
  tweet_fly_app.start()
  

if __name__ == '__main__':
  """
    Parameters - appname, conf_filename, log_filename, log_level
  """
  sys.stderr.write("Command line arguments "+ str(sys.argv)+ "\n")
  sys.stderr.flush()
  main(sys.argv)
