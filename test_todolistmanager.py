import unittest
import todolistmanager

class TestToDoListManagerMain(unittest.TestCase):
    def test_welcome_heading(self):
        expected = """
         <<< Welcome to my To-Do list App >>>
         _____________________________________
        """
        self.assertEqual(welcome_heading, expected)
        
        
def test_list_menu(self):
        expected = """
         1.  Add a task
         2. View Task
         3. Mark task as complete
         4. Delete a task
         5. Exit
        """
        self.assertEqual(list_menu(), expected)



if __name__ == "__main__":
    unittest.main()