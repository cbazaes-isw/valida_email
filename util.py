# pylint: disable=C0103,W0702,C0301
"""
Implementación de
https://www.scottbrady91.codnspym/Email-Verification/Python-Email-Verification-Script
"""
import re
import smtplib
import socket

import dns.resolver


def emailValido(email):
    """
    emailValido(email)
    """

    # 1. Validates format
    if not re.match(
            r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
            email) != None:
        return False

    host = email.split("@")[1]

    try:

        # 2. Validates DNS
        records = dns.resolver.query(host, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        # Get local server hostname
        localhost = socket.gethostname()

        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(localhost)
        server.mail('me@domain.com')
        code, message = server.rcpt(str(email))
        server.quit()

        # Assume 250 as Success
        return code == 250
    except:
        return False
