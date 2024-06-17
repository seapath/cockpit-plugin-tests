# Copyright (C) 2024 Savoir-faire Linux Inc.
# SPDX-License-Identifier: Apache-2.0

import unittest

from utils.Cockpit import Cockpit
from utils.config import *

class TestClusterDashboard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cockpit = Cockpit()
        cls.driver = cls.cockpit.setup_cockpit_access()
        cls.cockpit.enable_administrative_access()
        cls.cockpit.load_plugin_web_page(plugin_name="cockpit-cluster-dashboard")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_plugin_access(self):
        self.assertIn("Cluster Dashboard", self.driver.title)

if __name__ == "__main__":
    unittest.main()
