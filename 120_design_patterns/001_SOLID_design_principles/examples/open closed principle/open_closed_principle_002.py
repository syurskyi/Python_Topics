# Open-Closed Principle (OCP)

# Classes should be open for extension but closed for modification.
from abc import ABC, abstractmethod
from typing import List


class Journal:
    def __init__(self):
        self.entries: List[str] = []
        self.count: int = 1

    def add_entry(self, text: str) -> None:
        self.entries.append(f"{self.count}. {text}")
        self.count += 1

    def __str__(self):
        return "\n".join(self.entries)

    def save(self, storage_manager: "StorageManager", name: str) -> None:
        storage_manager.save(self, name)


class StorageManager(ABC):
    @abstractmethod
    def save(self, journal: Journal, name: str):
        pass


class LocalStorageManager(StorageManager):
    def save(self, journal: Journal, name: str):
        with open(name, "w") as f:
            print(f"Saving journal {name} into local storage.")
            f.write(str(journal))


class ExternalStorageManager(StorageManager):
    def save(self, journal: Journal, name: str):
        print(f"Saving journal {name} into external storage.")


if __name__ == "__main__":
    journal = Journal()
    journal.add_entry("Today, I'm learning about the Open-Closed Principle.")
    journal.add_entry("Yesterday, I've learned about the Single-Responsibility Principle.")
    print(journal)

    external_storage_manager = LocalStorageManager()
    journal.save(external_storage_manager, "my_journal")

    external_storage_manager = ExternalStorageManager()
    journal.save(external_storage_manager, "my_journal")
