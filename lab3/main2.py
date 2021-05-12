"""
Files comparations
"""

import unittest
import filecmp

START_ME_UP_FILE = "start_me_up_lyrics.txt"
START_ME_UP_COPY_FILE = "start_me_up_lyrics_copy.txt"
START_ME_UP_MODIFIED_FILE = "start_me_up_lyrics_modified.txt"
ENTRE_DOS_TIERRAS_FILE = "entre_dos_tierras_lyrics.txt"
NON_EXISTENT_FILE = "non_existent_file.txt"


class FileCmpTest(unittest.TestCase):
    """
    Test class
    """

    def test_equal_case(self):
        """
        test_equal_case
        """
        self.assertTrue(filecmp.cmp(START_ME_UP_FILE, START_ME_UP_COPY_FILE))

    def test_different_case(self):
        """
        test_different_case
        """
        self.assertFalse(filecmp.cmp(START_ME_UP_FILE, ENTRE_DOS_TIERRAS_FILE))

    def test_same_file(self):
        """
        test_same_file
        """
        self.assertTrue(filecmp.cmp(START_ME_UP_FILE, START_ME_UP_FILE))

    def test_non_existent_file(self):
        """
        test_non_existent_file
        """
        self.assertRaises(
            FileNotFoundError,
            filecmp.cmp,
            NON_EXISTENT_FILE,
            START_ME_UP_FILE)

    def test_non_existent_file_2(self):
        """
        test_non_existent_file_2
        """
        self.assertRaises(
            FileNotFoundError,
            filecmp.cmp,
            START_ME_UP_FILE,
            NON_EXISTENT_FILE)

    def test_similar_files(self):
        """
        test_similar_files
        """
        self.assertFalse(filecmp.cmp(
            START_ME_UP_FILE,
            START_ME_UP_MODIFIED_FILE))


if __name__ == '__main__':
    unittest.main()
