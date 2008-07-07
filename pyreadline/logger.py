# -*- coding: utf-8 -*-
#*****************************************************************************
#       Copyright (C) 2006  Jorgen Stenarson. <jorgen.stenarson@bostream.nu>
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#*****************************************************************************

import socket, logging, logging.handlers
from pyreadline.unicode_helper import ensure_str

host="localhost"
port=logging.handlers.DEFAULT_TCP_LOGGING_PORT


root_logger=logging.getLogger('')
root_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
file_handler=None

class NULLHandler(logging.Handler):
    def emit(self, s):
        pass

class SocketStream(object):
    def __init__(self, host, port):
        self.logsocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    def write(self, s):
        self.logsocket.sendto(ensure_str(s),(host,port))

    def flush(self):
        pass

    def close(self):
        pass

socket_handler = logging.StreamHandler(SocketStream(host, port))
socket_handler.setFormatter(formatter)
root_logger.addHandler(NULLHandler())


def start_socket_log():
    root_logger.addHandler(socket_handler)

def stop_socket_log():
    root_logger.removeHandler(socket_handler)

def start_file_log(filename):
    global file_handler
    file_handler=logging.handlers.FileHandler(filename, "w")
    root_logger.addHandler(file_handler)

def stop_file_log():
    global file_handler
    if file_handler:
        root_logger.removeHandler(file_handler)
        file_handler.close()
        file_handler=None

def log(s):
    s = ensure_str(s)
    root_logger.debug(s)

