import struct
from boofuzz import *
def HTTP_Fuzzing(host, port):
    print("Working")
    """
    This example is a very simple HTTP Fuzzer
    """
    session = Session(
        target=Target(
            connection=SocketConnection(host=host, port=int(port), proto='tcp')))

    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'DEBUG'])
        if s_block_start("body", group="Method"):
            s_delim(" ", name='space-1')
            s_string("/", name='Request-URI')
            s_delim(" ", name='space-2')
            s_string('HTTP/1.1', name='HTTP-Version')
            s_static("\r\n", name="Request-Line-CRLF")
        s_static("\r\n", "Request-CRLF")
        s_block_end()

    s_initialize(name="CommandsArray")
    with s_block("Commands-Line"):
        s_group("Commands", ['User-Agent:', 'Date:', 'Authorization:', 'Connection:'])
        if s_block_start("body", group="Commands"):
            s_delim(" ", name='space-1')
            s_string("XAXAX", name='Request-URI')
            s_delim(" ", name='space-2')
            s_static("\r\n", name="Request-Line-CRLF")
        s_static("\r\n", "Request-CRLF")
        s_block_end()
    
    
    session.connect(s_get("Request"), s_get("CommandsArray"))
    session.fuzz()