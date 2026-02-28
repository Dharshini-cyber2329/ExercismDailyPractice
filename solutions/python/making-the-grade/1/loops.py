"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count scores at or below 40."""
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    """Return scores greater than or equal to threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    
    interval = (highest - 40) // 4
    return [41 + interval * i for i in range(4)]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""
    
    ranking = []
    for index, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        ranking.append(f"{index}. {name}: {score}")
    return ranking


def perfect_score(student_info):
    """Return first student with perfect score or empty list."""
    
    for student in student_info:
        if student[1] == 100:
            return student
    return []