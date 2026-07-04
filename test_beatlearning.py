# test_beatlearning.py
"""
Tests for BeatLearning module.
"""

import unittest
from beatlearning import BeatLearning

class TestBeatLearning(unittest.TestCase):
    """Test cases for BeatLearning class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BeatLearning()
        self.assertIsInstance(instance, BeatLearning)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BeatLearning()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
