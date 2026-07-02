def calculate_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def passed(score):
    return score >= 60


# print(__name__)
if __name__ == "__main__":
    print("i am on grade.py")
