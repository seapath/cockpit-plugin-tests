# Copyright (C) 2024 Savoir-faire Linux Inc.
# SPDX-License-Identifier: Apache-2.0

__unittest = True # Remove traceback

import unittest
import os

from utils.Cockpit import Cockpit
from utils.config import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestClusterDashboard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cockpit = Cockpit()
        cls.driver = cls.cockpit.setup_cockpit_access()
        cls.cockpit.enable_administrative_access()
        cls.cockpit.load_plugin_web_page(plugin_name="cockpit-cluster-update")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_plugin_access(self):
        self.assertIn("Update", self.driver.title)

    def test_upload_file(self):

        element = self.driver.find_element(By.ID, "updateUpload")
        element.click()

        file_path = os.path.abspath("files/upload_test.swu")
        element = self.driver.find_element(By.ID, "inputFile")
        element.send_keys(file_path)

        element = self.driver.find_element(By.ID, "uplaodFileButton")
        element.click()

        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element((By.ID, "progressUpload"), "100")
        )

if __name__ == "__main__":
    unittest.main()
