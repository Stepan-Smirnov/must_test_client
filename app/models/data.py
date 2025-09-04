from typing import Any

from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt


class DataModel(QAbstractListModel):
    """Base class for Data Model QListView"""

    def __init__(self):
        super().__init__()
        self.data_list = []

    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> list[Any]:
        """Get data of item"""

        if role == Qt.ItemDataRole.DisplayRole:
            return self.data_list[index.row()]
        return None

    def rowCount(self, parent=QModelIndex) -> int:
        """Get count data"""

        return len(self.data_list)

    def clear(self) -> None:
        """Clear data"""

        self.data_list.clear()

    def add_items(self, data: list) -> None:
        """Add data items"""

        for item in data:
            self.data_list.append(str(item))
