import unittest


class HashSetTestCase(unittest.TestCase):
    def test_all(self):
        from hash_set import HashSet

        s = HashSet()
        self.assertFalse(s.contains(0))
        self.assertTrue(s.insert(0))
        self.assertTrue(s.contains(0))

        self.assertFalse(s.insert(0))

        self.assertTrue(s.insert(1))
        self.assertEqual(2, s.len())

        self.assertEqual(set([0, 1]), set(s.collect()))
