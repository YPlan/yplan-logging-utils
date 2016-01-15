#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class BasicTests(unittest.TestCase):

    def test_it(self):
        import yplan_logging_utils
        assert hasattr(yplan_logging_utils, '__version__')
