"""Tests for the auto-scaling program."""

import unittest
import scaling


class ScalingTests(unittest.TestCase):

    def test_low_traffic(self):
        self.assertEqual(scaling.required_servers(50), 1)

    def test_high_traffic(self):
        self.assertEqual(scaling.required_servers(250), 3)

    def test_zero_viewers(self):
        self.assertEqual(scaling.required_servers(0), 1)

    def test_invalid_viewers(self):
        with self.assertRaises(ValueError):
            scaling.required_servers(-10)

    def test_average_load(self):
        self.assertEqual(scaling.average_load(200, 2), 100)


if __name__ == "__main__":
    unittest.main()