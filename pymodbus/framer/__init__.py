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

from .ascii import FramerAscii
from .base import FramerBase, FramerType
from .framer.banner import FramerBanner
from .rtu import FramerRTU
from .socket import FramerSocket
from .tls import FramerTLS


FRAMER_NAME_TO_CLASS = {
    FramerType.ASCII: FramerAscii,
    FramerType.RTU: FramerRTU,
    FramerType.BANNER: FramerBanner,
    FramerType.SOCKET: FramerSocket,
    FramerType.TLS: FramerTLS,
}
