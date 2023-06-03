from classes.Level import Level
import unittest
from unittest.mock import MagicMock, patch
# python.exe -m unittest discover tests

class BankTest(unittest.TestCase):
    @patch("classes.Level.input")
    def test_ask_for_level_and_give(self, mock_input):
        mock_input.return_value = "1"
        character = MagicMock
        level = Level()
        level.ask_for_level_and_give(character)
        self.assertEqual(character.level, 1)
