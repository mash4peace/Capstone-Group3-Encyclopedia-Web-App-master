import unittest
import models
class TestDBhelper(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testUserID(self):
        name = 'Kayla'
        result = models.getId('Kayla')
        self.assertEqual(result, 2)
if __name__ == '__main__':
    unittest.main()