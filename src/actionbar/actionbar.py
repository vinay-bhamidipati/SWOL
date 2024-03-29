from datetime import date
from functools import reduce

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QToolBar,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QDialogButtonBox,
    QFormLayout,
    QDialog,
    QFileDialog,
    QInputDialog,
    QSizePolicy,
    QHBoxLayout,
    QAction,
)
from PyQt5.QtCore import Qt

from ..backend.data import Data
from .newentry import NewEntry


class ActionBar(QToolBar):
    def __init__(self, parent_widget, data):
        super().__init__()
        self.data = data
        self.parent_widget = parent_widget

        self.new_entry = QAction("New Entry")
        self.remove_entry = QAction("Remove Entry")
        self.import_data = QAction("Import Data")
        self.help = QAction("Help")

        self.new_entry.triggered.connect(self._on_new_entry_click)
        self.import_data.triggered.connect(self._on_import_data_click)
        self.remove_entry.triggered.connect(self._on_remove_entry_click)
        self.addAction(self.new_entry)
        self.addAction(self.remove_entry)
        self.addAction(self.import_data)
        self.addAction(self.help)

    def _on_new_entry_click(self):
        NewEntry(self.data, self.parent_widget.table).exec()

    def _on_remove_entry_click(self):
        date, ok = QInputDialog.getText(
            self, "Remove an Entry", "Date to remove:", QLineEdit.Normal
        )
        if date and ok:
            Data.remove(date)
            self.parent_widget.refresh()

    def _on_import_data_click(self):
        delimiter = " "
        file_name = QFileDialog.getOpenFileName(
            self, "Choose Data Source", "/", "Data Files (*.csv, *.txt)"
        )
        with open(file_name, "r"):
            pass
