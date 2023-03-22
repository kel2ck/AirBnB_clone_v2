import unittest
import sys
import io
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestConsoleCreate(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create_base_model(self):
        # Redirect stdout to a StringIO object to capture printed output
        sys.stdout = io.StringIO()

        # Test creation of BaseModel object with parameters
        self.console.onecmd('create State name="Kwara"')

        # Get the printed output and extract the ID of the created object
        object_id = sys.stdout.getvalue().strip()

        # Reset stdout to the original sys.stdout
        sys.stdout = sys.__stdout__

        # Retrieve the created object using the ID
        created_object = None
        for obj in storage.all().values():
            if obj.id == object_id:
                created_object = obj
                break

        # Check if the object has been created successfully and has the correct attributes
        self.assertIsInstance(created_object, State)
        self.assertEqual(created_object.name, "Kwara")
        # Add more test methods for other classes (User, Place, etc.) similar to test_create_base_model

if __name__ == "__main__":
    unittest.main()
