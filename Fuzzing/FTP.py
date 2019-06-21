import struct
from boofuzz import *
def FTP_Fuzzing(host, port, username, password):
      session = Session(
        target=Target(
            connection=SocketConnection(host=host, port=int(port), proto='tcp')))

      s_initialize(name="user-ftp")
      with s_block("FTP-Line"):
          s_group('Method', ["USER", "PASS", "STOR", "RETR", "STOU", "APPE", "ALLO", "NOOP"])
          if s_block_start("body", group="Method"):
              s_delim(" ", name="space-1")
              s_string(username, name='username')
              s_static("\r\n", "FTP-CRLF")
          s_block_end()
     
     # session.connect(s_get('user'))
      #session.connect(s_get('pass'))
      #session.connect(s_get("user-ftp"))
      session.connect(s_get("user-ftp"), s_get('pass'))
      session.connect(s_get('STOR'))
      session.connect(s_get('RETR'))
      session.fuzz()