def build_roster(registrations):
    """
    Given a list of (student_id, course_id) pairs, build a course roster.

    The result should be a dictionary where:
      - each key is a course id (string)
      - each value is a sorted list of unique student ids (strings)
        enrolled in that course

    Duplicate registrations for the same (student_id, course_id) pair
    should appear only once in the output.
    """

    roster = {}  # course_id -> set of students (using set to remove duplicates)

    # Step 1: Build sets grouped by course
    for student_id, course_id in registrations:
        if course_id not in roster:
            roster[course_id] = set()
        roster[course_id].add(student_id)

    # Step 2: Convert each set into a sorted list
    for course_id in roster:
        roster[course_id] = sorted(roster[course_id])

    return roster


if __name__ == "__main__":
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),  # duplicate
    ]
    print(build_roster(sample))
