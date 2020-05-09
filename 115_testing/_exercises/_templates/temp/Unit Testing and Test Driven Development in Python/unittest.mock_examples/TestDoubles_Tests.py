______ pytest
____ pytest ______ raises
____ unittest.mock ______ MagicMock
____ LineReader ______ readFromFile

@pytest.fixture()
___ mock_open(monkeypatch):
    mock_file _ MagicMock()
    mock_file.readline _ MagicMock(return_value_"test line")
    mock_open _ MagicMock(return_value_mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    r_ mock_open

___ test_returnsCorrectString(mock_open, monkeypatch):
    mock_exists _ MagicMock(return_value_True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result _ readFromFile("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"

___ test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists _ MagicMock(return_value_False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result _ readFromFile("blah")
