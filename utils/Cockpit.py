# Copyright (C) 2024 Savoir-faire Linux Inc.
# SPDX-License-Identifier: Apache-2.0

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from utils.config import *

class Cockpit(object):

    def setup_cockpit_access(self):
        options = Options()
        options.accept_insecure_certs = True

        self.driver = webdriver.Firefox(options=options)
        self.driver.get(COCKPIT_URL)

        element = self.driver.find_element(By.ID, "login-user-input")
        element.clear()
        element.send_keys(COCKPIT_USERNAME)

        element = self.driver.find_element(By.ID, "login-password-input")
        element.clear()
        element.send_keys(COCKPIT_PASSWORD)

        element = self.driver.find_element(By.ID, "login-button")
        element.click()

        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, "toolbar"))
            )
            return self.driver
        except:
            self.driver.close()
            print("connection to Cockpit failed")

    def enable_administrative_access(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, "button.ct-locked.pf-m-link.pf-c-button")
        if elements:
            elements[0].click()

            WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-cancel.pf-m-secondary.pf-c-button"))
            ).click()

    def load_plugin_web_page(self, plugin_name):
        self.driver.get(f"{COCKPIT_URL}/{plugin_name}")

        # Cockpit uses iframes to load a webpage inside the main webpage.
        WebDriverWait(self.driver,1).until(
            EC.frame_to_be_available_and_switch_to_it((By.NAME, f"cockpit1:localhost/{plugin_name}"))
        )
