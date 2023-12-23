import abc

class DataSource(abc.ABC):
    #DataSource is the 'service' class since this is the 'service' that is used later by the 'client' class
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
    #Inherits from DataSource so this class is also a 'service' class
    def read(self):
        print("reading TEXT file from", self._file_name)

class JsonFile(DataSource):
    # Inherits from DataSource so this class is also a 'service' class
    def read(self):
        print("reading JSON file from", self._file_name)

class SQLLiteDBFile(DataSource):
    # Inherits from DataSource so this class is also a 'service' class
    def read(self):
        print("reading SQLLiteDB file from", self._file_name)


class UI:
    # UI is the 'client' class since it will use a `service' data_source
    def __init__(self, data_source: DataSource):
        """
        Initializes UI
        :param data_source: DataSource
        """
        self._data_source = data_source #data source injected from external source

    def read_data_source(self):
        self._data_source.read()


def main():
    """
    main() is acting as the 'Injector'. It's responsible for 'injecting' or passing the
    DataSource 'service' (JsonFile, TextFile, SQLLiteDBFile)
    into the UI 'client' class
    """

    # Can 'inject'/pass any type of DataSource to UI, and it will work without modifying UI class
    file = JsonFile("data.json")
    # file = TextFile("data.txt")
    # file = SQLLiteDBFile("data.db")

    ui = UI(file) #main() is 'injecting'/passing file 'service' into UI 'client'
    ui.read_data_source()

if __name__ == '__main__':
    main()