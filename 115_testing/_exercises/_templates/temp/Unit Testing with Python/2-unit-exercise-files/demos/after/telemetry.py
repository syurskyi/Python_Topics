DiagnosticChannelConnectionString = "*111#"

c_ TelemetryDiagnosticControls:

    ___  -   telemetry_client=None):
        self.telemetry_client = telemetry_client or TelemetryClient()
        self.diagnostic_info = ""

    ___ check_transmission(self):
        telemetry_client = self.reconnect(DiagnosticChannelConnectionString)
        self.diagnostic_info = ""
        self.diagnostic_info = self.fetch_diagnostic_info(telemetry_client)

    ___ reconnect  address):
        self.telemetry_client.disconnect()
        retryLeft = 3
        while ((not self.telemetry_client.online_status) and retryLeft > 0):
            self.telemetry_client.connect(address)
            retryLeft -= 1

        if not self.telemetry_client.online_status:
            raise Exception("Unable to connect.")
        return self.telemetry_client

    ___ fetch_diagnostic_info  connected_client):
        connected_client.send(TelemetryClient.DIAGNOSTIC_MESSAGE)
        if not self.telemetry_client.online_status:
            raise Exception("Unable to connect.")
        return connected_client.receive()



c_ TelemetryClient(object):
    DIAGNOSTIC_MESSAGE = "AT#UD"

    ___  - (self):
        self.online_status = False
        self._diagnostic_message_result = ""

    ___ connect  telemetry_server_connection_string):
        if not telemetry_server_connection_string:
            raise Exception()

        # simulate the operation on a real modem
        success = random.randint(0, 10) <= 8
        self.online_status = success

    ___ disconnect(self):
        self.online_status = False

    ___ send  message):
        if not message:
            raise Exception()

        if message == TelemetryClient.DIAGNOSTIC_MESSAGE:
            # simulate a status report
            self._diagnostic_message_result = """\
LAST TX rate................ 100 MBPS\r\n
HIGHEST TX rate............. 100 MBPS\r\n
LAST RX rate................ 100 MBPS\r\n
HIGHEST RX rate............. 100 MBPS\r\n
BIT RATE.................... 100000000\r\n
WORD LEN.................... 16\r\n
WORD/FRAME.................. 511\r\n
BITS/FRAME.................. 8192\r\n
MODULATION TYPE............. PCM/FM\r\n
TX Digital Los.............. 0.75\r\n
RX Digital Los.............. 0.10\r\n
BEP Test.................... -5\r\n
Local Rtrn Count............ 00\r\n
Remote Rtrn Count........... 00"""

            return
        # here should go the real Send operation (not needed for this exercise)

    ___ receive(self):
        if not self._diagnostic_message_result:
            # simulate a received message (just for illustration - not needed for this exercise)
            message = ""
            messageLength = random.randint(0, 50) + 60
            i = messageLength
            while(i >= 0):
                message += chr((random.randint(0, 40) + 86))
                i -= 1
        else:
            message = self._diagnostic_message_result
            self._diagnostic_message_result = ""

        return message