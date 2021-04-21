import unittest
from directory_manager import DirectoryManager

SAMPLE_RECORD = dict(zip(
    ["name", "email", "age", "origin_country"], 
    ["Marco", "A00354896@mail.com", 27, "Mexico"]))

class DirectoryManagerTest(unittest.TestCase):

    def test_add_record(self):
        directory_manager = DirectoryManager()
        directory_manager.add_record(SAMPLE_RECORD)

        # Verify the record can be found in the directory
        self.assertIsNotNone(directory_manager.find_record(SAMPLE_RECORD))

    def test_delete_record(self):
        directory_manager = DirectoryManager()
        directory_manager.delete_record(SAMPLE_RECORD)

        # Verify the record cannot be found in the directory
        self.assertIsNone(directory_manager.find_record(SAMPLE_RECORD))

        
    def test_find_record_by_email(self):
        directory_manager = DirectoryManager()
        record = directory_manager.find_record_by_email(SAMPLE_RECORD["email"])

        if (record != None):
            # Assert the email property matches the one that was searched
            self.assertEqual(record["email"], SAMPLE_RECORD["email"])

    def test_find_record_by_age(self):
        directory_manager = DirectoryManager()
        record = directory_manager.find_record_by_age(SAMPLE_RECORD["age"])

        if (record != None):
            # Assert the age property matches the one that was searched
            self.assertEqual(record["age"], SAMPLE_RECORD["age"])
        
        
    def test_list_all_records(self):
        directory_manager = DirectoryManager()
        all_records = directory_manager.list_all_records()

        for record in all_records:
            print(record)

        # No conditions to test

if __name__ == '__main__':
    unittest.main()