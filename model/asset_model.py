from PySide2.QtCore import QAbstractTableModel, Qt

COLUMN_HEADERS = ['Asset Name', 'Asset Type', 'Created Time', 'Updated Time']

class TableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.asset_table = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.asset_table[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.asset_table)

    def columnCount(self, index):
        if self.asset_table:
            return len(self.asset_table[0])
        else:
            return 0

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return COLUMN_HEADERS[section]  # section => 0, 1, 2,,,, header에서 column 의미
        return super().headerData(section, orientation, role)