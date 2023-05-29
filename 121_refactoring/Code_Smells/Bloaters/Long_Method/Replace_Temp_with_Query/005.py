# Problem

def calculateGrade():
    totalScore = midtermScore + finalScore + assignmentScore
    averageScore = totalScore / 3

    if averageScore >= 90:
        grade = "A"
    elif averageScore >= 80:
        grade = "B"
    elif averageScore >= 70:
        grade = "C"
    elif averageScore >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade

# Solution

def calculateGrade():
    averageScore = calculateAverageScore()

    if averageScore >= 90:
        grade = "A"
    elif averageScore >= 80:
        grade = "B"
    elif averageScore >= 70:
        grade = "C"
    elif averageScore >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade

def calculateAverageScore():
    totalScore = midtermScore + finalScore + assignmentScore
    averageScore = totalScore / 3
    return averageScore

#  In this example, we extract the calculation of the average score into a separate function calculateAverageScore().
#  This eliminates the need for the temporary variable averageScore in the main function, making the code more readable.