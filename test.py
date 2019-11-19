import argparse
import os
import shutil
import tempfile
import unittest
from unittest import mock

from io_test import main


def checkExistsFiles(fileName):
    return os.path.exists(fileName)


class MainTest(unittest.TestCase):
    file_name = "file"
    outfile_path = tempfile.mkdtemp()

    # def setUp(self):
    #     os.mkdir(self.outfile_path)

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(files=3, size=1024, path=outfile_path,
                                                P="\0", parallel=3))
    def test_main(self, mock_args):
        main()
        for i in mock_args.files:
            self.assertEqual(checkExistsFiles(self.outfile_path + "/" + self.file_name + i), True)

    def tearDown(self):
        shutil.rmtree(self.outfile_path)
        # os.rmdir(self.outfile_path)
        # os.remove(self.file_name)


if __name__ == '__main__':
    unittest.main()
