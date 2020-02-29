from abs_adapter import AbsAdapter

class CustAdapter(AbsAdapter):
    def name(self):
        return self._adaptee.name

    def address(self):
        return self._adaptee.address
        