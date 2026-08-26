# test_nftcompass.py
"""
Tests for NFTCompass module.
"""

import unittest
from nftcompass import NFTCompass

class TestNFTCompass(unittest.TestCase):
    """Test cases for NFTCompass class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTCompass()
        self.assertIsInstance(instance, NFTCompass)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTCompass()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
