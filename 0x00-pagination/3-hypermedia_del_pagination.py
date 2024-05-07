#!/usr/bin/env python3
"""
Pagination sample
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range and page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes a new Server
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves info about a page from a
        given index and with a specified size
        """
        data = self.dataset()
        total_pages = math.ceil(len(data) / page_size)
        if index is None:
            index = 0
        assert 0 <= index < len(data), "Index out of range."
        start = index
        end = min(index + page_size, len(data))
        dataset = data[start:end]
        if end == len(data):
            next_index = None
        else:
            next_index = end
        page_info = {
            'index': start,
            'next_index': next_index,
            'page_size': page_size,
            'data': dataset,
            'total_pages': total_pages,
        }
        return page_info
