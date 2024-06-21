# Copyright (C) 2024 Savoir-faire Linux Inc.
# SPDX-License-Identifier: Apache-2.0

# Global variables
COCKPIT_URL = "https://192.168.216.137:9090"
COCKPIT_USERNAME = "virtu"
COCKPIT_PASSWORD = "toto"

HOST_1 = "nuc1"
HOST_2 = "nuc2"
HOST_3 = "nuc3"

HOST_1_IP = "192.168.216.135"
HOST_2_IP = "192.168.216.136"
HOST_3_IP = "192.168.216.137"

HOST_1_STATUS = "online"
HOST_2_STATUS = "offline"
HOST_3_STATUS = "online"

OSD_1_STATUS = "online"
OSD_2_STATUS = "offline"
OSD_3_STATUS = "online"

CEPH_STATUS = "HEALTH_WARN 1/3 mons down, quorum nuc1,nuc3"

RESOURCE_VM_NAME = "guest3"
RESOURCE_VM_STATE = "Started"
RESOURCE_VM_TYPE = "VirtualDomain"
RESOURCE_VM_HOST = HOST_3
RESOURCE_VM_POLICY = "pin"
RESOURCE_VM_DEFAULT_HOST = HOST_3

RESOURCE_CLONED_NAME = "cl_ptpstatus_test"
RESOURCE_CLONED_STATE = "Stopped"
RESOURCE_CLONED_TYPE = "ptpstatus_test"
RESOURCE_CLONED_HOST = HOST_2
RESOURCE_CLONED_POLICY = "-"
RESOURCE_CLONED_DEFAULT_HOST = "-"

RESOURCES_LOGS = ""

def dashboard_variables():
    global ONLINE_NODES, OFFLINE_NODES, CLUSTER_STATUS, CLUSTER_LOGS

    ONLINE_NODES = " ".join([host for host, status in [(HOST_1, HOST_1_STATUS), (HOST_3, HOST_3_STATUS)] if status == "online"])
    OFFLINE_NODES = " ".join([host for host, status in [(HOST_2, HOST_2_STATUS)] if status == "offline"])

    CLUSTER_STATUS = "CLUSTER WARN" if OFFLINE_NODES else "CLUSTER OK"
    CLUSTER_LOGS = f"offline node: {OFFLINE_NODES}" if OFFLINE_NODES else ""

dashboard_variables()


