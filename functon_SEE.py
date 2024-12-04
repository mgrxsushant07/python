#create a function that print grade of SEE using 90.

def print_see_grade(score):
    """
    Function to print the grade of SEE based on the provided score.
    :param score: The score (out of 100) to evaluate the grade.
    """
    if not (0 <= score <= 100):  # Ensure the score is within a valid range
        print("Invalid score! Please enter a score between 0 and 100.")
        return

    # Determine grade based on score
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B+"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C+"
    elif score >= 40:
        grade = "C"
    elif score >= 35:
        grade = "D"
    else:
        grade = "E"

    print(f"The grade for a score of {score} is: {grade}")


# Example usage with a score of 90
print_see_grade(90)
