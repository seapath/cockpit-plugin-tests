# Copyright (C) 2024 Savoir-faire Linux Inc.
# SPDX-License-Identifier: Apache-2.0

import unittest

test_loader = unittest.TestLoader()
tests = test_loader.discover('tests', pattern='*.py')

test_runner = unittest.TextTestRunner()
test_runner.run(tests)
