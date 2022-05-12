from asyncio import BaseProtocol
import os, sys
from scanner.BaseWrapper import BaseWrapper

class SnmpWrapper(BaseWrapper):

    def asyncRequest(self, timeout=5):
        pass