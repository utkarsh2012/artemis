# -*- coding: utf-8 -*-

import unittest
import requests
from tasks import _construct_url, _get_metrics


class TestArtemisTasks(unittest.TestCase):

    def test_correct_construct_url(self):
        url = _construct_url("localhost", "metric")
        self.assertEqual(url, "http://localhost/metric")

    def test_invalid_node_construct_url(self):
        self.assertRaises(IOError, _construct_url, "", "metric")

    def test_invalid_url_construct_url(self):
        self.assertRaises(IOError, _construct_url, "localhost", "")

    def test_invalid_request(self):
        self.assertRaises(requests.ConnectionError, _get_metrics, "http://hello")

if __name__ == '__main__':
    unittest.main()
