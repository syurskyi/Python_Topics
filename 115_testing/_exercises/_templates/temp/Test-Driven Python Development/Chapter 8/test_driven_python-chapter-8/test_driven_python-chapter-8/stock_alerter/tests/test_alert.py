_____ u__
from u__ _____ mock
from datetime _____ datetime

from ..alert _____ Alert
from ..rule _____ PriceRule
from ..stock _____ Stock
from ..event _____ Event


c_ AlertTest ?.?
    ___ test_action_is_executed_when_rule_matches
        goog = mock.MagicMock(spec=Stock)
        goog.updated = Event()
        goog.update.side_effect = lambda date, value: goog.updated.fire(self)
        exchange = {"GOOG": goog}
        rule = mock.MagicMock(spec=PriceRule)
        rule.matches.return_value = True
        rule.depends_on.return_value = {"GOOG"}
        action = mock.MagicMock()
        alert = Alert("sample alert", rule, action)
        alert.connect(exchange)
        exchange["GOOG"].update(datetime(2014, 2, 10), 11)
        action.execute.assert_called_with("sample alert")
