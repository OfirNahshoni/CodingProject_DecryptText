# This file handles unit tests of the fundomental functions of the project (written in decrypt_message.py)

import unittest
import decrypt_message


class TestFiles(unittest.TestCase):
    # Constructor (__init__ method of unittest)
    # def setUp(self):
    #     self.message = ''
    
    # Test method for readTxtFile method
    def test_isReadTxtString_readTxtFile(self):
        # Checks if the returned value of the function readTxtFile is a string type
        self.assertIsInstance(decrypt_message.readTxtFile(decrypt_message.ENC_MSG_FILENAME1), str)
    
    def test_isReadTxtFromFile_readTxtFile(self):
        # Checks if the function readTxtFile is actually read the text from the file
        # Read first file
        with open(decrypt_message.ENC_MSG_FILENAME1, 'r') as file:
            txt = file.read()
        self.assertEqual(decrypt_message.readTxtFile(decrypt_message.ENC_MSG_FILENAME1), txt)
        with open(decrypt_message.ENC_MSG_FILENAME2, 'r') as file:
            txt = file.read()
        self.assertEqual(decrypt_message.readTxtFile(decrypt_message.ENC_MSG_FILENAME2), txt)
        with open(decrypt_message.ENC_MSG_FILENAME3, 'r') as file:
            txt = file.read()
        self.assertEqual(decrypt_message.readTxtFile(decrypt_message.ENC_MSG_FILENAME3), txt)

    # Need to be added to more functions


if __name__ == '__main__':
    unittest.main()
