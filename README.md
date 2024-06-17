<!-- Copyright (C) 2024 Savoir-faire Linux Inc.
SPDX-License-Identifier: Apache-2.0 -->

# cockpit-plugin-tests

This is a Selenium project written in Python to test the following Cockpit plugins for seapath:

- [Cockpit cluster dashboard](https://github.com/seapath/cockpit-cluster-dashboard)
- [Cockpit cluster vm management](https://github.com/seapath/cockpit-cluster-vm-managment)
- [Cockpit update](https://github.com/seapath/cockpit-update)

A configuration file is provided on the utils/ directory and contains all the global variables that can be configured.

## Run the tests with cqfd

[cqfd](https://github.com/savoirfairelinux/cqfd) is a quick and convenient way to run commands in the current directory, but within a pre-defined Docker container.
cqfd is used with Xvfb to run selenium without display.

* Install cqfd

```
$ git clone https://github.com/savoirfairelinux/cqfd.git
$ cd cqfd
$ sudo make install
```

* Use cqfd

`cqfd init`

NOTE: The step above is only required once

`cqfd run xvfb-run -b <flavour_name>`

List of flavours:
- all_tests
- dashboard_tests


## Run the tests without cqfd

This requires to install the following dependancies:

- [Selenium WebDriver](https://www.selenium.dev/) that can be installed whith the following command: `pip install selenium`.
- Firefox web browser


Two options are available to test the plugins:
- `python main.py`: To run all the tests
- `python -m unittest tests/<Test>.py`: To test a specific plugin
