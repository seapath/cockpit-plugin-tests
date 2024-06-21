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
        cls.color_online = "rgb(119, 221, 118)"
        cls.color_offline = "rgb(255, 105, 98)"

        cls.cockpit = Cockpit()
        cls.driver = cls.cockpit.setup_cockpit_access()
        cls.cockpit.enable_administrative_access()
        cls.cockpit.load_plugin_web_page(plugin_name="cockpit-cluster-dashboard")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_plugin_access(self):
        self.assertIn("Cluster Dashboard", self.driver.title)

    def test_node_status(self):
        online_nodes = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "node-status-online-nodes"))
        )
        offline_nodes = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "node-status-offline-nodes"))
        )
        self.assertEqual("online nodes : " + ONLINE_NODES, online_nodes.text)
        self.assertEqual("offline nodes : " + OFFLINE_NODES, offline_nodes.text)

    def test_cluster_status(self):
        status = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "cluster-status"))
        )
        logs = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "cluster-logs"))
        )
        self.assertIn(CLUSTER_STATUS, status.text)
        self.assertIn(CLUSTER_LOGS, logs.text)

    def test_vm_resources(self):
        vm_infos_element = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, RESOURCE_VM_NAME + "-" + RESOURCE_VM_HOST ))
        )
        vm_infos = vm_infos_element.text

        self.assertIn(RESOURCE_VM_NAME, vm_infos)
        self.assertIn(RESOURCE_VM_STATE, vm_infos)
        self.assertIn(RESOURCE_VM_TYPE, vm_infos)
        self.assertIn(RESOURCE_VM_HOST, vm_infos)
        self.assertIn(RESOURCE_VM_POLICY, vm_infos)
        self.assertIn(RESOURCE_VM_DEFAULT_HOST, vm_infos)

    def test_cloned_resources(self):
        cloned_resource_infos_element = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, RESOURCE_CLONED_NAME + "-" + RESOURCE_CLONED_HOST ))
        )
        cloned_resource_infos = cloned_resource_infos_element.text

        self.assertIn(RESOURCE_CLONED_NAME, cloned_resource_infos)
        self.assertIn(RESOURCE_CLONED_STATE, cloned_resource_infos)
        self.assertIn(RESOURCE_CLONED_TYPE, cloned_resource_infos)
        self.assertIn(RESOURCE_CLONED_HOST, cloned_resource_infos)
        self.assertIn(RESOURCE_CLONED_POLICY, cloned_resource_infos)
        self.assertIn(RESOURCE_CLONED_DEFAULT_HOST, cloned_resource_infos)

    def test_resources_logs(self):
        logs = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "resources-logs"))
        )
        self.assertIn(RESOURCES_LOGS, logs.text)

    def test_ceph_status(self):
        status = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "ceph-logs"))
        )
        self.assertIn(CEPH_STATUS, status.text)

    def test_ceph_osd(self):
        element = self.driver.find_element(By.ID, "osd-button")
        element.click()

        osd_tree = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "osd-default"))
        )
        self.assertIn(HOST_1, osd_tree.text)
        self.assertIn(HOST_2, osd_tree.text)
        self.assertIn(HOST_3, osd_tree.text)
        self.assertIn("osd", osd_tree.text)

    def test_ceph_mon(self):
        element = self.driver.find_element(By.ID, "mon-button")
        element.click()

        mon_1 = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "mon-" + HOST_1))
        )
        mon_2 = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "mon-" + HOST_2))
        )
        mon_3 = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "mon-" + HOST_3))
        )
        mon_1_status = mon_1.value_of_css_property("background-color")
        mon_2_status = mon_2.value_of_css_property("background-color")
        mon_3_status = mon_3.value_of_css_property("background-color")

        self.assertIn(HOST_1, mon_1.text)
        self.assertIn(HOST_2, mon_2.text)
        self.assertIn(HOST_3, mon_3.text)

        self.assertIn(HOST_1_IP, mon_1.text)
        self.assertIn(HOST_2_IP, mon_2.text)
        self.assertIn(HOST_3_IP, mon_3.text)

        def color_to_status(color):
            if color == self.color_online:
                return "online"
            elif color == self.color_offline:
                return "offline"
            else:
                return "unknown"

        self.assertEqual(color_to_status(mon_1_status), OSD_1_STATUS)
        self.assertEqual(color_to_status(mon_2_status), OSD_2_STATUS)
        self.assertEqual(color_to_status(mon_3_status), OSD_3_STATUS)

if __name__ == "__main__":
    unittest.main()
