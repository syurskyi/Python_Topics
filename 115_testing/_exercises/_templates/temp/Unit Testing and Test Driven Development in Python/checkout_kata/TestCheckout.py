______ pytest
____ Checkout ______ Checkout

@pytest.fixture()
___ checkout(
    checkout _ Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    r_ checkout

___ test_CanCalculateTotal(checkout
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

___ test_GetCorrectTotalWithMultipleItems(checkout
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

___ test_canAddDiscountRule(checkout
    checkout.addDiscount("a", 3, 2)

___ test_canApplyDiscountRule(checkout
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2

___ test_ExceptionWithBadItem(checkout
    w__ pytest.raises(Exception
        checkout.addItem("c")




