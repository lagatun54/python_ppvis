from random import randint
from parsers.dom_writer import XmlWriter
from numpy.random import choice
import numpy as np
import names


class XMLGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_xml_files(files_count: int, stock_count: int) -> None:
       
        for i in range(files_count):
            path = f"../xml/{str(i)}.xml"
            data_dict = {}
            line_up_values = np.array(['popcorn', 'kamenb', 'Coca-cola'])
            warehouse_values = np.array(['1620 Johnson Way', '1214 FIRST STATE BLVD'])
            with open(path, 'w') as file:
                dom_writer = XmlWriter(path)
                for _ in range(stock_count):
                    # dictionary filling
                    data_dict["name"] = names.get_full_name()
                    data_dict["line_up"] = choice(line_up_values)
                    data_dict["titles"] = str(randint(999, 9999))
                    data_dict["position"] = str(randint(0, 150))
                    data_dict["rank"] = choice(warehouse_values)
                    dom_writer.create_stock(data_dict)
            # creating xml file using dom parser
            dom_writer.create_xml_file()


def main():
    XMLGenerator.generate_xml_files(files_count=10, stock_count=50)


if __name__ == "__main__":
    main()
