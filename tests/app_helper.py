from PySide6.QtCore import Qt
from PySide6.QtTest import QTest

from main import MainWindow


class HelpButtons:
    """Help class for tests"""

    def __init__(self, window: MainWindow):
        self.window = window

    def get_total_data(self) -> int:
        """Get Total Data in app"""

        return int(self.window.ui.total_data.text().split(sep=" ")[2])

    def add_data_text(self, text: str) -> None:
        """add text in line"""

        self.window.ui.add_data_text.setText(text)

    def push_add_data_button(self) -> None:
        """Button send data"""

        QTest.mouseClick(
            self.window.ui.add_data_btn,
            Qt.MouseButton.LeftButton,
        )

    def get_data_text(self) -> None:
        """Get current data line text"""

        return len(self.window.ui.add_data_text.text())

    def push_get_data_button(self) -> None:
        """Button get data"""

        QTest.mouseClick(
            self.window.ui.get_data_btn,
            Qt.MouseButton.LeftButton,
        )

    def push_next_page_button(self) -> None:
        """Push next-page button"""

        QTest.mouseClick(
            self.window.ui.next_page_btn,
            Qt.MouseButton.LeftButton,
        )

    def push_prev_page_button(self):
        """Push prev-page button"""

        QTest.mouseClick(
            self.window.ui.prev_page_btn,
            Qt.MouseButton.LeftButton,
        )

    def get_current_page(self) -> int:
        """Get number current-page"""

        return int(self.window.ui.curent_page.text().split(sep=" ")[2])

    def set_items_in_list(self, count: int) -> None:
        """set count items in QListView"""

        self.window.ui.page_count.setValue(count)
