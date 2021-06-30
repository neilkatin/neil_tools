#! /usr/bin/env python

import unittest

import init_config
import test_file

class InitConfigTestCase(unittest.TestCase):

    def testDotEnv(self):
        result = init_config.init_config({}, env_file_name='test_config.env')

        self.assertTrue("A" in result)
        self.assertTrue("B" in result)
        self.assertFalse("C" in result)

        self.assertEqual(result["A"], "A_VALUE")
        self.assertEqual(result["B"], "B_VALUE")

        self.assertEqual(result.A, "A_VALUE")
        self.assertEqual(result.B, "B_VALUE")

    def testDotEnvDict(self):

        config = {
                'A': 'A_CONFIG',
                'B': 'B_CONFIG',
                }

        result = init_config.init_config(config, env_file_name='missing_file.env')

        #print(f"result { result.keys() }")

        self.assertTrue("A" in result)
        self.assertTrue("B" in result)
        self.assertFalse("C" in result)

        self.assertEqual(result["A"], "A_CONFIG")
        self.assertEqual(result["B"], "B_CONFIG")

        self.assertEqual(result.A, "A_CONFIG")
        self.assertEqual(result.B, "B_CONFIG")


    def testDotEnvFile(self):

        result = init_config.init_config(test_file, env_file_name='missing_file.env')

        #print(f"result { result.keys() }")

        self.assertTrue("A" in result)
        self.assertTrue("B" in result)
        self.assertFalse("C" in result)

        self.assertEqual(result["A"], "A_FILE")
        self.assertEqual(result["B"], "B_FILE")

        self.assertEqual(result.A, "A_FILE")
        self.assertEqual(result.B, "B_FILE")
        
if __name__ == '__main__':
    unittest.main()
