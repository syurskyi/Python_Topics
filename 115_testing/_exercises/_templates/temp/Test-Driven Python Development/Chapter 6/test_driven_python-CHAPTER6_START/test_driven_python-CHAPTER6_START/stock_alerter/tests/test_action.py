_____ smtplib
_____ u__
____ u__ _____ mock

____ ..action _____ PrintAction, EmailAction


c_ MessageMatcher:
    ___  -  expected):
        expected = expected

    ___ __eq__ other):
        r_ expected["Subject"] == other["Subject"] and \
            expected["From"] == other["From"] and \
            expected["To"] == other["To"] and \
            expected["Message"] == other._payload


@mock.patch("builtins.print")
c_ PrintActionTest ?.?
    ___ test_executing_action_prints_message mock_print):
        action = PrintAction()
        action.execute("GOOG > $10")
        mock_print.a_c_w..("GOOG > $10")


@mock.patch("smtplib.SMTP")
c_ EmailActionTest ?.?
    ___ setUp
        action = EmailAction(to="siddharta@silverstripesoftware.com")

    ___ test_email_is_sent_to_the_right_server mock_smtp_class):
        action.execute("MSFT has crossed $10 price level")
        mock_smtp_class.a_c_w..("email.stocks.com")

    ___ test_connection_closed_after_sending_mail mock_smtp_class):
        mock_smtp = mock_smtp_class.return_value
        action.execute("MSFT has crossed $10 price level")
        mock_smtp.send_message.a_c_w..(mock.ANY)
        aT..(mock_smtp.quit.called)
        mock_smtp.assert_has_calls([
            mock.call.send_message(mock.ANY),
            mock.call.quit()])

    ___ test_connection_closed_if_send_gives_error mock_smtp_class):
        mock_smtp = mock_smtp_class.return_value
        mock_smtp.send_message.side_effect = smtplib.SMTPServerDisconnected()
        ___
            action.execute("MSFT has crossed $10 price level")
        _____ E..:
            pass
        aT..(mock_smtp.quit.called)

    ___ test_email_is_sent_with_the_right_subject mock_smtp_class):
        mock_smtp = mock_smtp_class.return_value
        action.execute("MSFT has crossed $10 price level")
        call_args, _ = mock_smtp.send_message.call_args
        sent_message = call_args[0]
        aE..("New Stock Alert", sent_message["Subject"])

    ___ test_email_is_sent_when_action_is_executed mock_smtp_class):
        expected_message = {
            "Subject": "New Stock Alert",
            "Message": "MSFT has crossed $10 price level",
            "To": "siddharta@silverstripesoftware.com",
            "From": "alerts@stocks.com"
        }
        mock_smtp = mock_smtp_class.return_value
        action.execute("MSFT has crossed $10 price level")
        mock_smtp.send_message.a_c_w..(
            MessageMatcher(expected_message))
