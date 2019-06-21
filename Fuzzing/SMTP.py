from boofuzz import *



def SMTP_Fuzz(host, port):
    session = Session(
            target=Target(
                connection = SocketConnection(host, int(port), proto='tcp'),
            ),)
 
    s_initialize("Login-SMTP")
    with s_block("Auth"):
        s_group("Login", ["HELO", "EHLO"])
        if s_block_start("body", group="Login"):
            s_delim(" ", name="space1")
            s_string("XAXA", name="Fuzz1")
            s_static("\r\n", name="Fuzz-CRFL")
        s_block_end()

    s_initialize("Command-SMTP")
    with s_block("Commands"):
        s_group("Command", ["EXPN", "MAIL FROM:", "ETRN", "HELP", "RCTP TO:"])
        if s_block_start("body", group="Command"):
            s_delim(" ", name="space1")
            s_string("XAXAX", name="fuzz1")
            s_static("\r\n", name="SMTP-CRFT")
        s_block_end()
    session.connect(s_get("Login-SMTP"))
    session.connect(s_get("Login-SMTP"), s_get("Command-SMTP"))
    session.fuzz()