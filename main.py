import logging
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from app.api.data_api import DataAPI
from app.config.error import Ui_Form
from app.config.un_main import Ui_MainWindow
from app.constants import CURRENT_PAGE, TOTAL_DATA, TOTAL_PAGES
from app.models.data import DataModel

logger = logging.getLogger(__name__)


class ErrorWindow(QWidget):
    """Error window class"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.error_btn.pressed.connect(self.close_error_window)

    def close_error_window(self):
        """close error window"""

        self.close()


class MainWindow(QMainWindow):
    """Main window class"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.client = DataAPI()
        self.model = DataModel()
        self.ui.list_data.setModel(self.model)
        self.error_window = ErrorWindow()

        self.current_page = None
        self.per_page = None
        self.total_pages = None
        self.total_items = None
        self.sequence_number = 1

        self.get_data()
        self.ui.get_data_btn.pressed.connect(self.get_data)
        self.ui.next_page_btn.pressed.connect(self.switch_next_page)
        self.ui.prev_page_btn.pressed.connect(self.switch_prev_page)
        self.ui.add_data_btn.pressed.connect(self.add_data)

    def get_data(self, firs_page=True) -> None:
        """handler of button get data"""

        try:
            if firs_page or self.per_page != self.ui.page_count.value():
                self.current_page = 1

            self.model.data_list.clear()

            self.per_page = self.ui.page_count.value()
            data_list = self.client.get_data(
                page=self.current_page, per_page=self.per_page
            )
            self.model.add_items(data=data_list.get("data"))
            self.model.layoutChanged.emit()

            self.total_items = data_list.get("total_items")
            self.ui.total_data.setText(
                TOTAL_DATA.format(number=self.total_items)
            )

            self.current_page = data_list.get("current_page")
            self.ui.curent_page.setText(
                CURRENT_PAGE.format(page=self.current_page)
            )

            self.total_pages = data_list.get("total_pages")
            self.ui.total_pages.setText(
                TOTAL_PAGES.format(pages=self.total_pages)
            )
        except Exception:
            self.open_error_window()
            logger.exception(msg="Error: ")

    def switch_next_page(self) -> None:
        """handler button switch to next page"""

        if not self.current_page == self.total_pages:
            self.current_page += 1
            self.get_data(firs_page=False)

    def switch_prev_page(self) -> None:
        """handler button switch to prev page"""

        if not self.current_page == 1:
            self.current_page -= 1
            self.get_data(firs_page=False)

    def add_data(self) -> None:
        """handler button add data"""

        try:
            text = self.ui.add_data_text.text()
            if not text or text.isspace():
                self.ui.add_data_text.clear()
                return

            self.client.add_data(
                text=text, sequence_number=self.sequence_number
            )
            self.sequence_number += 1
            self.ui.add_data_text.clear()
            self.total_items += 1
            self.ui.total_data.setText(
                TOTAL_DATA.format(number=self.total_items)
            )
        except Exception:
            self.open_error_window()
            logger.exception(msg="Error: ")

    def open_error_window(self) -> None:
        """call error window"""

        self.error_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
