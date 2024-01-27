#!/usr/bin/env python3
"""
Simple and most common way of Pagination
"""


def index_range(page, page_size):
    """
    simplest pagination method
    """
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)
