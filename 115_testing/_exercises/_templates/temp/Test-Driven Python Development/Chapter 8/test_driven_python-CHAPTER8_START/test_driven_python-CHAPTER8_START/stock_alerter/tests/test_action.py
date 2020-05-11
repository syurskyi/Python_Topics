_____ smtplib
_____ u__
from u__ _____ mock

from ..action _____ PrintAction, EmailAction


c_ MessageMatcher:
    ___  -  expected):
        expected = expected

    ___ __eq__ other):
        return expected["Subject"] == other["Subject"] and \
            expected["From"] == other["From"] and \
            expected["To"] == other["To"] and \
            expected["Message"] == other._payload


@mock.patch("builtins.print")
c_ PrintActionTest ?.?
    ___ test_executing_action_prints_message mock_print):
        action = PrintAction()
        action.execute("GOOG > $10")
        mock_print.assert_called_with("GOOG > $10")


c_ EmailActionTest ?.?
    ___ setUp
        patcher = mock.patch("smtplib.SMTP")
        addCleanup(patcher.stop)
        mock_smtp_class = patcher.start()
        mock_smtp = mock_smtp_class.return_value
        action = EmailAction(to="siddharta@silverstripesoftware.com")

    ___ test_email_is_sent_to_the_right_server
        action.execute("MSFT has crossed $10 price level")
        mock_smtp_class.assert_called_with("email.stocks.com")

    ___ test_connection_closed_after_sending_mail
        action.execute("MSFT has crossed $10 price level")
        mock_smtp.send_message.assert_called_with(mock.ANY)
        assertTrue(mock_smtp.quit.called)
        mock_smtp.assert_has_calls([
            mock.call.send_message(mock.ANY),
            mock.call.quit()])

    ___ test_connection_closed_if_send_gives_error
        mock_smtp.send_message.side_effect = smtplib.SMTPServerDisconnected()
        try:
            action.execute("MSFT has crossed $10 price level")
        except Exception:
            pass
        assertTrue(mock_smtp.quit.called)

    ___ test_email_is_sent_with_the_right_subject
        action.execute("MSFT has crossed $10 price level")
        call_args, _ = mock_smtp.send_message.call_args
        sent_message = call_args[0]
        assertEqual("New Stock Alert", sent_message["Subject"])

    ___ test_email_is_sent_when_action_is_executed
        expected_message = {
            "Subject": "New Stock Alert",
            "Message": "MSFT has crossed $10 price level",
            "To": "siddharta@silverstripesoftware.com",
            "From": "alerts@stocks.com"
        }
        action.execute("MSFT has crossed $10 price level")
        mock_smtp.send_message.assert_called_with(
            MessageMatcher(expected_message))
