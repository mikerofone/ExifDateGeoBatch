from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListView


class CustomListView(QListView):
    def __init__(self, right_click_handler):
        super().__init__()
        self._right_click_handler = right_click_handler

    def mousePressEvent(self, e):
        super().mousePressEvent(e)

        index = self.indexAt(e.pos())

        if not index.isValid():
            self.clearSelection()
        elif e.button() == Qt.MouseButton.RightButton and self._right_click_handler:
            self._right_click_handler(index)

