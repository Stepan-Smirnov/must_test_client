import pytest
from app_helper import HelpButtons
from PySide6.QtWidgets import QApplication

from main import MainWindow


@pytest.fixture(scope="session")
def app():
    """add app fixture"""

    return QApplication()


@pytest.fixture(scope="session")
def button(app):
    """add widget main_window fixture"""

    return HelpButtons(window=MainWindow())
