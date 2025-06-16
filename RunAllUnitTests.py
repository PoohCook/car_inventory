#! /usr/bin/env python3

import sys
import unittest
import logging


print("================== Begin run of all unit tests =====================")

# Core Test Suite
from test.ManTest import *


if __name__ == '__main__':
    unittest.main()
