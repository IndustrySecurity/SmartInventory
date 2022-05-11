from asyncio import BaseProtocol
import os, sys
from scanner.BaseProtocol import BaseProtocol

class Snmp(BaseProtocol):

    def asyncRequest(self, timeout=5):
        pass