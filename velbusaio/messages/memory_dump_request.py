"""
:author: Thomas Delaet <thomas@delaet.org>
"""
from __future__ import annotations

from velbusaio.command_registry import register_command
from velbusaio.message import Message

COMMAND_CODE = 0xCB


class MemoryDumpRequestMessage(Message):
    """
    send by:
    received by: VMB6IN, VMB4RYLD
    """

    def populate(self, priority, address, rtr, data):
        """
        :return: None
        """
        self.needs_low_priority(priority)
        self.needs_no_rtr(rtr)
        self.needs_no_data(data)
        self.set_attributes(priority, address, rtr)

    def data_to_binary(self):
        """
        :return: bytes
        """
        return bytes([COMMAND_CODE])


register_command(COMMAND_CODE, MemoryDumpRequestMessage)
