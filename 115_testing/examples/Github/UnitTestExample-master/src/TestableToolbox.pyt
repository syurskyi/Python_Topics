import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "TestableToolbox"
        self.alias = "TT"

        # List of tool classes associated with this toolbox
        self.tools = [TestableBufferTool]


class TestableBufferTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Testable Buffer Tool"
        self.description = "Buffers the input layer and adds an area field."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        in_features = arcpy.Parameter(
            displayName="Input Features",
            name="in_features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")

        out_features = arcpy.Parameter(
            displayName="Output Features",
            name="out_features",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output")
        return [in_features, out_features]

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # Extract parameters as variables
        in_features = parameters[0].value
        out_features = parameters[1].value

        # Buffer the input features
        arcpy.Buffer_analysis(in_features=in_features,
                              out_feature_class=out_features,
                              buffer_distance_or_field="5280 Feet")

        # Clean up the output schema
        arcpy.DeleteField_management(out_features, "BUFF_DIST")
        arcpy.DeleteField_management(out_features, "ORIG_FID")
        arcpy.AddField_management(out_features, "MyBufferDistance", "Double")

        # Calculate the area in square miles
        arcpy.CalculateField_management(out_features,
                                        "MyBufferDistance",
                                        "!shape.area@squaremiles!",
                                        "PYTHON_9.3")

        return
