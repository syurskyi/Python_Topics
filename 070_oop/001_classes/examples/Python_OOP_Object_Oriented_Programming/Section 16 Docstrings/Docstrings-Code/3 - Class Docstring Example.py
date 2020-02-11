class TissueSample:
    """Class that represents a tissue sample.

    Attributes:
        patient (Patient): the patient associated with the tissue sample.
        organ (str): the organ associated with tissue sample.
        code (str): a unique alphanumeric sequence that identifies the tissue sample.
        diagnosis (str): the diagnosis associated with this tissue sample. By default,
            it is initialized to None when the instance is created.

    Methods:
        show_data(): displays the four main properties of the tissue sample
            in a human-readable format. 
    """
    
    def __init__(self, patient, organ, code):
        """Initalize the values of the instance attributes of an instance of TissueSample.

        Args:
            patient (Patient): the patient associated with the tissue sample.
            organ (str): the organ associated with tissue sample.
            code (str): a unique alphanumeric sequence that identifies the tissue sample.
        """
        self.patient = patient
        self.organ = organ
        self._code = code
        self._diagnosis = None

    def show_data(self):
        """Display tissue sample data in a human-readable format."""
        print(f"==== Tissue Sample (code #{self.code})====")
        print(f"Patient:", self.patient.name)
        print(f"Organ:", self.organ)

        if self.diagnosis:
            print(f"Diagnosis:", self.diagnosis)

    # Read-only property (only a getter)
    @property
    def code(self):
        """Code of the tissue sample."""
        return self._code

    @property
    def diagnosis(self):
        """Diagnosis associated with the tissue sample."""
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, diagnosis):
        self._diagnosis = diagnosis
