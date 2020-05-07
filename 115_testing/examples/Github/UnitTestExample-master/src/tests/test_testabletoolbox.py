from os import path
import unittest
import random
import arcpy


class TestTestableToolbox(unittest.TestCase):
    database_path = path.join(path.dirname(path.abspath(__file__)), "data", "test_testabletoolbox.gdb")
    point_path = path.join(database_path, "PointData")

    toolbox_path = path.join(path.dirname(path.dirname(path.abspath(__file__))), "TestableToolbox.pyt")

    def test_point_data(self):
        arcpy.AddToolbox(self.toolbox_path)

        # Create an output location in scratch that uses a common prefix and random suffix
        # This helps prevent conflicts if things don't get cleaned up.
        temp_output = path.join("%scratchGDB%", "test_point_data_{}".format(random.randint(0, 9999)))

        # Execute the tool
        arcpy.TestableBufferTool_TT(self.point_path, temp_output)

        # Build the location of the answer
        answer_output = path.join(self.database_path, "test_point_data_answer")

        # Compare the temp_output to the known answer.
        result = arcpy.FeatureCompare_management(in_base_features=answer_output,
                                                 in_test_features=temp_output,
                                                 sort_field=["Value"],
                                                 continue_compare=True)

        # If it returns false, something has gone wrong, so fail the test.
        if result.getOutput(1) != 'true':
            print(result.getMessages())

        self.assertEqual(result.getOutput(1), 'true')

        # Clean up after ourselves
        arcpy.Delete_management(temp_output)


if __name__ == '__main__':
    unittest.main()
