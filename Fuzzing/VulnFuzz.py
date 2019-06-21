import socket
from boofuzz import *

def VulnServer(host, port):
   csv_out = "True"
   fuzz_loggers = [FuzzLoggerText()]
   if csv_out is not None:
       f = open("Vuln-Fuzz", "wb")
       fuzz_loggers.append(FuzzLoggerCsv(file_handle=f))
   session = Session(
            target=Target(
                connection = SocketConnection(host, int(port), proto='tcp'),
            ),)
 
 
   s_initialize("VulnFuzz")
   with s_block("codes"):
    s_group("Commands", ["SRUN", "GMON", "KSTAN"])
    if s_block_start("body", group="Commands"):
      s_delim(" ", name="space1")
      s_string("XAXAX", name="Fuzz1")
      s_static("\r\n", name="Controls")
   s_block_end()
   session.connect(s_get("VulnFuzz")), #callback=get_banner)
   session.fuzz()