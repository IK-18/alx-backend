#!/usr/bin/env python3
"""
index_range module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range and page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
