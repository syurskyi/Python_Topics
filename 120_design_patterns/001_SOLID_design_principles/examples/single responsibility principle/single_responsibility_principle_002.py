#  Single-Responsibility Principle (SRP)

# Gather together the things that change for the same reasons. Separate those things that change for different reasons


from datetime import datetime


class Journal:
    # Journal formats entries
    def __init__(self):
        self.entries = []
        self.count = 1

    def add_entry(self, text: str, timestamp: datetime = datetime.today()) -> None:
        self.entries.append(f"{self.count}. {text}")
        self.count += 1

    def __str__(self):
        return "\n".join(self.entries)

    # Journal saves itself
    def save(self, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(str(self))


class StorageManager:
    # StorageManager saves things into long-term memory
    def save_journal(self, journal: Journal, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(str(journal))


if __name__ == "__main__":
    journal = Journal()
    journal.add_entry("Today, I'm learning the Single-Responsibility Principle.")
    journal.add_entry("Tomorrow, I'll learn about the Open-Close Principle.")
    print(journal)
