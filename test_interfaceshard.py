# test_interfaceshard.py
"""
Tests for InterfaceShard module.
"""

import unittest
from interfaceshard import InterfaceShard

class TestInterfaceShard(unittest.TestCase):
    """Test cases for InterfaceShard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InterfaceShard()
        self.assertIsInstance(instance, InterfaceShard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InterfaceShard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
