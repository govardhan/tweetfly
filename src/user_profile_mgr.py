
from patterns import singleton

@singleton
class UserProfileMgr:
  user_profiles = {}


class UserProfile:
  def create_profile(msisdn)
