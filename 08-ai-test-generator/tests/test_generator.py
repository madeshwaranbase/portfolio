import unittest
from generate_tests import operations_from_spec

class GeneratorTests(unittest.TestCase):
    def test_reads_http_operations_from_spec(self):
        spec = {"openapi":"3.0.0","paths":{"/events":{"get":{"summary":"List events"},"post":{"operationId":"createEvent"}}}}
        result = operations_from_spec(spec)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["method"], "GET")

if __name__ == "__main__":
    unittest.main()
