import logging
import os
import pytest
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from utilities.configManager import ConfigManager


@pytest.fixture(scope="session", autouse=True)
def setup_session(request):
    work_dir = RootPathHelper.current_root_path(__file__)
    os.chdir(work_dir)
    for log_name in [
        "selenium.webdriver.remote.remote_connection",
        "selenium.webdriver.common.selenium_manager",
        "urllib3.connectionpool",
    ]:
        logger = logging.getLogger(log_name)
        logger.disabled = True
