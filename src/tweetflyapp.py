import logging
from patterns import singleton
from genutils import UVConf
import genutils

@singleton
class TweetFlyApp:
  app_logger = None
  log_filename = "/usr/local/uv/log/tweetfly.log"
  conf_filename = "/usr/local/uv/conf/tweetfly.conf"
  log_level = logging.DEBUG
  app_conf = None

  def __init__(self, p_conf_filename, p_log_filename, p_log_level):
    #TODO check log_filename and its path existance
    #TODO validate log_level
    conf_filename = p_conf_filename
    app_logger = init_logger(__name__, p_log_filename, p_log_level);
    app_conf = UVConf(app_logger, conf_filename);


  def start(self):
    #TODO Initialize TweetStreamListner
    #TODO Authenticate
    #TODO Wait for updates
    for i in range(10):
      app_logger.info("I am running now - %d" % i)
    pass

  def on_tweet_update(self):
    #TODO Write tweet into db
    pass
  


if __name__ == '__main__':
  """
    Parameters - appname, conf_filename, log_filename, log_level
    logging.DEBUG
    10
    logging.INFO
    20
    logging.WARNING
    30
    logging.ERROR
    40
    logging.CRITICAL
    50

  """
  #TODO Validate arguments
  tweet_fly_app = TweetFlyApp(argv[1], argv[2], argv[3])
  tweet_fly_app.start()
