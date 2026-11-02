from datetime import datetime, timedelta


class Assignment:
    def __init__(self, title, course, platform, due_date):
        self.title = title
        self.course = course
        self.platform = platform  # 'Brightspace', 'Ed', or 'Pearson'
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d %H:%M")

    def __repr__(self):
        return f"[{self.platform}] {self.course}: {self.title} (Due: {self.due_date.strftime('%b %d, %Y - %H:%M')})"


class DeadlineAggregator:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def fetch_brightspace_deadlines(self):
        self.add_assignment(
            Assignment("Homework 9: Software Architecture", "CS 19300", "Brightspace", "2026-11-05 23:59"))

    def fetch_ed_deadlines(self):
        self.add_assignment(Assignment("Module 2 Quiz", "CS 18000", "Ed", "2026-11-03 17:00"))

    def fetch_pearson_deadlines(self):
        self.add_assignment(Assignment("Chapter 4 Practice Set", "MATH 16500", "Pearson", "2026-11-04 23:59"))

    def get_upcoming_deadlines(self, days_ahead=7):
        now = datetime.now()
        limit = now + timedelta(days=days_ahead)

        upcoming = [a for a in self.assignments if now <= a.due_date <= limit]
        upcoming.sort(key=lambda x: x.due_date)
        return upcoming


if __name__ == "__main__":
    aggregator = DeadlineAggregator()

    aggregator.fetch_brightspace_deadlines()
    aggregator.fetch_ed_deadlines()
    aggregator.fetch_pearson_deadlines()

    print("=== Upcoming Deadlines (Next 7 Days) ===")
    for item in aggregator.get_upcoming_deadlines():
        print(item)