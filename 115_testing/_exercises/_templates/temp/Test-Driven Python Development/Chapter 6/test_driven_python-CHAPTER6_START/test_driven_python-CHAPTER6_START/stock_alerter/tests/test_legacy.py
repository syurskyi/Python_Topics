_____ u__
from u__ _____ mock
from datetime _____ datetime

from ..legacy _____ AlertProcessor


c_ TestAlertProcessor(AlertProcessor):
    ___  -  exchange):
        AlertProcessor. -  autorun=False)
        exchange = exchange


c_ AlertProcessorTest ?.?
    @mock.patch("builtins.print")
    ___ test_processor_characterization_1 mock_print):
        AlertProcessor()
        mock_print.assert_has_calls([mock.call("AAPL", 8),
                                     mock.call("GOOG", 15),
                                     mock.call("AAPL", 10),
                                     mock.call("GOOG", 21)])

    ___ test_processor_characterization_2
        processor = AlertProcessor(autorun=False)
        with mock.patch("builtins.print") as mock_print:
            processor.run()
        mock_print.assert_has_calls([mock.call("AAPL", 8),
                                     mock.call("GOOG", 15),
                                     mock.call("AAPL", 10),
                                     mock.call("GOOG", 21)])

    ___ test_processor_characterization_3
        processor = AlertProcessor(autorun=False)
        mock_goog = mock.Mock()
        processor.exchange = {"GOOG": mock_goog}
        updates = [("GOOG", datetime(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.update.assert_called_with(datetime(2014, 12, 8), 5)

    ___ test_processor_characterization_4
        mock_goog = mock.Mock()
        mock_aapl = mock.Mock()
        exchange = {"GOOG": mock_goog, "AAPL": mock_aapl}
        processor = AlertProcessor(autorun=False, exchange=exchange)
        updates = [("GOOG", datetime(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.update.assert_called_with(datetime(2014, 12, 8), 5)

    ___ test_processor_characterization_5
        mock_goog = mock.Mock()
        mock_aapl = mock.Mock()
        exchange = {"GOOG": mock_goog, "AAPL": mock_aapl}
        processor = TestAlertProcessor(exchange)
        updates = [("GOOG", datetime(2014, 12, 8), 5)]
        processor.do_updates(updates)
        mock_goog.update.assert_called_with(datetime(2014, 12, 8), 5)

    ___ test_processor_characterization_6
        processor = AlertProcessor(autorun=False)
        processor.do_updates = mock.Mock()
        processor.run()
        processor.do_updates.assert_called_with([
            ('GOOG', datetime(2014, 2, 11, 14, 10, 22, 130000), 5),
            ('AAPL', datetime(2014, 2, 11, 0, 0), 8),
            ('GOOG', datetime(2014, 2, 11, 14, 11, 22, 130000), 3),
            ('GOOG', datetime(2014, 2, 11, 14, 12, 22, 130000), 15),
            ('AAPL', datetime(2014, 2, 11, 0, 0), 10),
            ('GOOG', datetime(2014, 2, 11, 14, 15, 22, 130000), 21)])

    ___ test_processor_characterization_7
        mock_reader = mock.MagicMock()
        mock_reader.parse_file.return_value = [
            ('GOOG', datetime(2014, 2, 11, 14, 12, 22, 130000), 15)]
        processor = AlertProcessor(autorun=False, reader=mock_reader)
        with mock.patch("builtins.print") as mock_print:
            processor.run()
        mock_print.assert_called_with("GOOG", 15)

    ___ test_processor_characterization_8
        mock_reader = mock.MagicMock()
        mock_reader.parse_file.return_value = [
            ('GOOG', datetime(2014, 2, 11, 14, 10, 22, 130000), 5)]
        processor = AlertProcessor(autorun=False, reader=mock_reader)
        with mock.patch("builtins.print") as mock_print:
            processor.run()
        assertFalse(mock_print.called)

    ___ test_processor_characterization_9
        processor = AlertProcessor(autorun=False)
        processor.print_action = mock.Mock()
        processor.do_updates([
            ('GOOG', datetime(2014, 2, 11, 14, 12, 22, 130000), 15)])
        assertTrue(processor.print_action.called)

    ___ test_processor_gets_values_from_reader
        mock_reader = mock.MagicMock()
        mock_reader.parse_file.return_value = \
            [('GOOG', datetime(2014, 2, 11, 14, 12, 22, 130000), 15)]
        processor = AlertProcessor(autorun=False, reader=mock_reader)
        processor.print_action = mock.Mock()
        processor.run()
        assertTrue(processor.print_action.called)
