"""Framer."""
__all__ = [
    "FramerAscii",
    "FramerBase",
    "FramerBanner",
    "FramerRTU",
    "FramerSocket",
    "FramerTLS",
    "FramerType"
]

from pymodbus.framer.ascii import FramerAscii
from pymodbus.framer.base import FramerBase, FramerType
from pymodbus.framer.banner import FramerBanner
from pymodbus.framer.rtu import FramerRTU
from pymodbus.framer.socket import FramerSocket
from pymodbus.framer.tls import FramerTLS


FRAMER_NAME_TO_CLASS = {
    FramerType.ASCII: FramerAscii,
    FramerType.RTU: FramerRTU,
    FramerType.BANNER: FramerBanner,
    FramerType.SOCKET: FramerSocket,
    FramerType.TLS: FramerTLS,
}
