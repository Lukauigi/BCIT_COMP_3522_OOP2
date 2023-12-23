import abc

class DataSource(abc.ABC):
    def __init__(self, file_name):
        """
        Initializes DataSource
        :param file_name: file name of data source
        """
        self._file_name = file_name

    @abc.abstractmethod
    def read(self):
        pass

class TextFile(DataSource):
    def read(self):
        print("reading TEXT file from", self._file_name)

class JsonFile(DataSource):
    def read(self):
        print("reading JSON file from", self._file_name)

class SQLLiteDB(DataSource):
    def read(self):
        print("reading SQLLiteDB file from", self._file_name)


class UI:
    def __init__(self):
        """
        Initializes UI
        :param data_source: DataSource
        """
        """
        Instantiating TextFile in initializer. Tight coupling of UI class to TextFile.
        If I want to change UI to read a different file, need to change code in UI initializer
        """
        self._data_source = TextFile("data.txt")

    def read_data_source(self):
        self._data_source.read()


def main():
    ui = UI()
    ui.read_data_source()

if __name__ == '__main__':
    main()