# Copyright (C) 2024 Savoir-faire Linux Inc.
# SPDX-License-Identifier: Apache-2.0

__unittest = True # Remove traceback

import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.Cockpit import Cockpit
from utils.config import *

class TestClusterDashboard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cockpit = Cockpit()
        cls.driver = cls.cockpit.setup_cockpit_access()
        cls.cockpit.enable_administrative_access()
        cls.cockpit.load_plugin_web_page(plugin_name="cockpit-cluster-vm-management")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_plugin_access(self):
        self.assertIn("Cluster VM Management", self.driver.title)

    def test_vm_resources(self):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, f"#{RESOURCE_VM_NAME}>td:nth-child(3)"), RESOURCE_VM_POLICY)
        )
        vm_infos_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, RESOURCE_VM_NAME ))
        )
        vm_infos = vm_infos_element.text

        self.assertIn(RESOURCE_VM_NAME, vm_infos)
        self.assertIn(RESOURCE_VM_STATE, vm_infos)
        self.assertIn(RESOURCE_VM_HOST, vm_infos)
        self.assertIn(RESOURCE_VM_POLICY, vm_infos)
        self.assertIn(RESOURCE_VM_DEFAULT_HOST, vm_infos)

    def test_vm_action(self):
        selected_vm = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"#{RESOURCE_VM_NAME}>td:nth-child(1)" ))
        )
        selected_vm.click()

        if(RESOURCE_VM_STATE != "Started"):
            start_button = self.driver.find_element(By.ID, "action-start")
            start_button.click()
            # Wait until the VM status changes to "Started"
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, f"#{RESOURCE_VM_NAME}>td:nth-child(2)"), "Started")
            )

        stop_button = self.driver.find_element(By.ID, "action-stop")
        stop_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, f"#{RESOURCE_VM_NAME}>td:nth-child(2)"), "Stopped")
        )

        vm_name = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"#{RESOURCE_VM_NAME}>td:nth-child(2)" ))
        )
        self.assertIn("Stopped", vm_name.text)

        start_button = self.driver.find_element(By.ID, "action-start")
        start_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, f"#{RESOURCE_VM_NAME}>td:nth-child(2)"), "Started")
        )

if __name__ == "__main__":
    unittest.main()
