_____ u__
____ u__ _____ mock
____ d_t_ _____ d_t_

____ ..legacy _____ AlertProcessor


c_ TestAlertProcessor(AlertProcessor):
    ___  -  ex__):
        AlertProcessor. -  autorun=F..)
        ex__ = ex__


c_ AlertProcessorTest ?.?
    @mock.patch("builtins.print")
    ___ test_processor_characterization_1 mock_print):
        AlertProcessor()
        mock_print.assert_has_calls([mock.call("AAPL", 8),
                                     mock.call("GOOG", 15),
                                     mock.call("AAPL", 10),
                                     mock.call("GOOG", 21)])

    ___ test_processor_characterization_2
        processor = AlertProcessor(autorun=F..)
        w__ mock.patch("builtins.print") as mock_print:
            processor.run()
        mock_print.assert_has_calls([mock.call("AAPL", 8),
                                     mock.call("GOOG", 15),
                                     mock.call("AAPL", 10),
                                     mock.call("GOOG", 21)])

    ___ test_processor_characterization_3
        processor = AlertProcessor(autorun=F..)
        mock_goog = mock.Mock()
        processor.ex__ = {"GOOG": mock_goog}
        updates = [("GOOG", d_t_(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.u...a_c_w..(d_t_(2014, 12, 8), 5)

    ___ test_processor_characterization_4
        mock_goog = mock.Mock()
        mock_aapl = mock.Mock()
        ex__ = {"GOOG": mock_goog, "AAPL": mock_aapl}
        processor = AlertProcessor(autorun=F.., ex__=ex__)
        updates = [("GOOG", d_t_(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.u...a_c_w..(d_t_(2014, 12, 8), 5)

    ___ test_processor_characterization_5
        mock_goog = mock.Mock()
        mock_aapl = mock.Mock()
        ex__ = {"GOOG": mock_goog, "AAPL": mock_aapl}
        processor = TestAlertProcessor(ex__)
        updates = [("GOOG", d_t_(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.u...a_c_w..(d_t_(2014, 12, 8), 5)

    ___ test_processor_characterization_6
        processor = AlertProcessor(autorun=F..)
        processor.do_updates = mock.Mock()
        processor.run()
        processor.do_updates.a_c_w..([
            ('GOOG', d_t_(2014, 2, 11, 14, 10, 22, 130000), 5),
            ('AAPL', d_t_(2014, 2, 11, 0, 0), 8),
            ('GOOG', d_t_(2014, 2, 11, 14, 11, 22, 130000), 3),
            ('GOOG', d_t_(2014, 2, 11, 14, 12, 22, 130000), 15),
            ('AAPL', d_t_(2014, 2, 11, 0, 0), 10),
            ('GOOG', d_t_(2014, 2, 11, 14, 15, 22, 130000), 21)])

    ___ test_processor_characterization_7
        mock_reader = mock.MagicMock()
        mock_reader.parse_file.return_value = [
            ('GOOG', d_t_(2014, 2, 11, 14, 12, 22, 130000), 15)]
        processor = AlertProcessor(autorun=F.., reader=mock_reader)
        w__ mock.patch("builtins.print") as mock_print:
            processor.run()
        mock_print.a_c_w..("GOOG", 15)

    ___ test_processor_characterization_8
        mock_reader = mock.MagicMock()
        mock_reader.parse_file.return_value = [
            ('GOOG', d_t_(2014, 2, 11, 14, 10, 22, 130000), 5)]
        processor = AlertProcessor(autorun=F.., reader=mock_reader)
        w__ mock.patch("builtins.print") as mock_print:
            processor.run()
        aF..(mock_print.called)

    ___ test_processor_characterization_9
        processor = AlertProcessor(autorun=F..)
        processor.print_action = mock.Mock()
        processor.do_updates([
            ('GOOG', d_t_(2014, 2, 11, 14, 12, 22, 130000), 15)])
        aT..(processor.print_action.called)

    ___ test_processor_gets_values_from_reader
        mock_reader = mock.MagicMock()
        mock_reader.parse_file.return_value = \
            [('GOOG', d_t_(2014, 2, 11, 14, 12, 22, 130000), 15)]
        processor = AlertProcessor(autorun=F.., reader=mock_reader)
        processor.print_action = mock.Mock()
        processor.run()
        aT..(processor.print_action.called)
