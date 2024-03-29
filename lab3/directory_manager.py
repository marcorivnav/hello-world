"""
Module to handle a directory
"""

import json

DIRECTORY_FILE = 'directory.txt'


class DirectoryManager:
    """
    Class to handle the directory
    """

    @staticmethod
    def add_record(record):
        """
        Function to insert a new record into the directory file.
            @param    record      A map (dict) cotaining the properties:
                               - name
                               - email
                               - age
                               - origin_country
        """
        with open(DIRECTORY_FILE, 'a') as directory_file:
            directory_file.write(str(record).replace("'", "\"") + "\n")


    @staticmethod
    def delete_record(record):
        """
        Method to delete a record from the directory file.
        @param    record      A map (dict) cotaining the properties:
                              - name
                              - email
                              - age
                              - origin_country
        """

        content = []
        with open(DIRECTORY_FILE, 'r') as directory_file:
            for line in directory_file:
                # Remove the \n from read lines
                line = line.replace("\n", "")

                if line != str(record).replace("'", "\""):
                    content.append(line)

        with open(DIRECTORY_FILE, "w") as directory_file:
            for line in content:
                directory_file.write(line + "\n")


    @staticmethod
    def find_record_by_field(field_name, value):
        """
        Generic method to find a record by any given field
        @param    field_name      A string containing the name of the field
                                  to be compared
        @param    value           The value to be compared
        @return                   If the record is found, the record dict is
                                  returned, Otherwise None is returned
        """

        with open(DIRECTORY_FILE, "r") as directory_file:
            found = False

            for line in directory_file:
                # Remove the \n from read lines
                line = line.replace("\n", "")

                # Convert the line to dict
                line_dict = json.loads(line)

                if line_dict[field_name] == value:
                    found = True
                    return line_dict

            if not found:
                print(
                    "Did not find the record with " +
                    field_name + " " + value)

        return None


    def find_record_by_email(self, email):
        """
        Short method to find a record by email
        @param    email       The value of the email to search
        @return               If the record is found, the record
                              dict is returned, Otherwise None is returned
        """

        return self.find_record_by_field("email", email)


    def find_record_by_age(self, age):
        """
        Short method to find a record by age
        @param    age         The value of the age to search
        @return               If the record is found, the record dict is
                              returned, Otherwise None is returned
        """

        return self.find_record_by_field("age", age)


    @staticmethod
    def list_all_records():
        """
        Returns the list of all the records in the directory
        """

        records_list = []

        with open(DIRECTORY_FILE, "r") as directory_file:
            for line in directory_file:
                # Remove the EOL separator
                line = line.replace("\n", "")

                # Convert the line to dict
                line_dict = json.loads(line)

                records_list.append(line_dict)

        return records_list


    @staticmethod
    def find_record(record):
        """
        Method to find a record
        @param    record      The value of the age to search
        @return               If the record is found, the record
                              dict is returned, Otherwise None is returned
        """

        with open(DIRECTORY_FILE, 'r') as directory_file:
            for line in directory_file:
                # Remove the \n from read lines
                line = line.replace("\n", "")

                if line == str(record).replace("'", "\""):
                    return record
        return None
