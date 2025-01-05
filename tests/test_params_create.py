import unittest
from console import HBNBCommand
from io import StringIO
import sys

class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()  # Capture the output

    def tearDown(self):
        sys.stdout = self.saved_stdout  # Restore the original stdout

    def test_create_state(self):
        self.cmd.onecmd("create State name=\"California\"")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)  # Check that an ID was printed

    def test_create_place(self):
        self.cmd.onecmd("create Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)  # Check that an ID was printed

    def test_invalid_class(self):
        self.cmd.onecmd("create NonExistentClass")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_missing_class(self):
        self.cmd.onecmd("create")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

if __name__ == "__main__":
    unittest.main()

