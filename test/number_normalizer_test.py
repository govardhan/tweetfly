import unittest
from number_normalizer import NumNormalizer

class nrmtest1(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('123456789') == '91123456789' , 'u entered wrong'
class nrmtest2(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('12345678') == '9112345678' , 'u entered wrong'
class nrmtest3(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('1234567') == '911234567' , 'u entered wrong'
class nrmtest4(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('123456') == '91123456' , 'u entered wrong'
class nrmtest5(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('12345') == '9112345' , 'u entered wrong'
class nrmtest6(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('1234') == '911234' , 'u entered wrong'
class nrmtest7(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('123') == '91123' , 'u entered wrong'
class nrmtest8(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('12') == '9112' , 'u entered wrong'
class nrmtest9(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('1') == '911' , 'u entered wrong'
class nrmtest10(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('1234a56789') == '911234a56789' , 'u entered wrong'
class nrmtest11(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('12345 6789') == '9112345 6789' , 'u entered wrong'
class nrmtest12(unittest.TestCase):
  def runTest(self):
    assert NumNormalizer('12a45 6789') == '9112a45 6789' , 'u entered wrong'

if __name__ == '__main__':
  unittest.main()

