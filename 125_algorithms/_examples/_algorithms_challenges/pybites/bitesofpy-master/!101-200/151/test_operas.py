import pytest

from operas import operas_both_at_premiere


def test_wagner_verdi():
    # materializing to list to support generator as return
    wagner_verdi = list(operas_both_at_premiere("wagner", "verdi"))
    a__ len(wagner_verdi) == 10
    a__ "Otello" not in wagner_verdi


def test_verdi_wagner():
    verdi_wagner = list(operas_both_at_premiere("verdi", "wagner"))
    a__ len(verdi_wagner) == 11

    # premiere after Wagner's death (composed in 1833)
    a__ "The Fairies" not in verdi_wagner


def test_beethoven_wagner():
    beethoven_wagner = list(operas_both_at_premiere("beethoven", "wagner"))
    a__ len(beethoven_wagner) == 0


def test_wagner_beethoven():
    wagner_beethoven = list(operas_both_at_premiere("wagner", "beethoven"))
    a__ len(wagner_beethoven) == 0


def test_beethoven_mozart():
    beethoven_mozart = list(operas_both_at_premiere("beethoven", "mozart"))
    a__ len(beethoven_mozart) == 5
    a__ "Apollo and Hyacinth" not in beethoven_mozart


def test_non_listed_composer():
    with pytest.raises(ValueError):
        list(operas_both_at_premiere("verdi", "dvorak"))


def test_non_listed_guest():
    # a guest must be in the list of composers
    with pytest.raises(ValueError):
        list(operas_both_at_premiere("dvorak", "verdi"))