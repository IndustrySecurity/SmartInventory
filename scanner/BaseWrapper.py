import os, sys

class BaseWrapper:

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

    def asyncRequest(self, timeout=5):
        pass

    def Request():
        pass