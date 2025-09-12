
import os
from datetime import datetime

file_name = "journal.txt"  # fixed per spec

class DiaryBox:
    """Manager class handles file I/O and actions for the journal."""
    def __init__(self, filename="file_name"):
        self.filename = filename

    # ADD
    def write_note(self, text):
        # append with timestamp using 'a' mode
        try:
            with open(self.filename, "a", encoding="utf-8") as f:
                clock_tag = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                f.write(clock_tag + "\n" + text.strip() + "\n\n")
            return True, "Entry added successfully!"
        except PermissionError:
            return False, "Permission denied while writing the journal."
        except Exception as e:
            return False, "Unexpected error: " + str(e)

    # VIEW
    def show_notes(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = f.read()
            return True, data if data.strip() else "No journal entries found. Start by adding a new entry!"
        except FileNotFoundError:
            return False, "No journal entries found. Start by adding a new entry!"
        except Exception as e:
            return False, "Unexpected error: " + str(e)

    # SEARCH
    def look_for(self, keyword):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            return False, "Error: The journal file does not exist. Please add a new entry first."
        matches = []
        for i in range(0, len(lines), 3):
            chunk = "".join(lines[i:i+3])
            if keyword.lower() in chunk.lower():
                matches.append(chunk.strip())
        if matches:
            return True, "\n\n".join(matches)
        return False, "No entries were found for the keyword: " + keyword

    # DELETE
    def clear_notes(self):
        if not os.path.exists(self.filename):
            return False, "No journal entries to delete."
        try:
            os.remove(self.filename)
            return True, "All journal entries have been deleted."
        except PermissionError:
            return False, "Permission denied while deleting the journal."
        except Exception as e:
            return False, "Unexpected error: " + str(e)


def menu():
    print("\nWelcome to Simple Diary Console!")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

mgr = DiaryBox()
while True:
    menu()
    choice = input("Please select an option: ").strip()
    if choice == "1":
        user_text = input("Enter your journal entry: ")
        ok, msg = mgr.write_note(user_text)
        print(msg)
    elif choice == "2":
        ok, msg = mgr.show_notes()
        if ok:
            print("Your Journal Entries:\n------------------------------")
            print(msg)
        else:
            print(msg)
    elif choice == "3":
        key = input("Enter a keyword or date to search: ")
        ok, msg = mgr.look_for(key)
        print("Matching Entries:\n------------------------------" if ok else "", end="")
        print(msg)
    elif choice == "4":
        sure = input("Are you sure you want to delete all entries? (yes/no): ").strip().lower()
        if sure == "yes":
            ok, msg = mgr.clear_notes(); print(msg)
        else:
            print("Cancelled.")
    elif choice == "5":
        print("Thank you for using Simple Diary Console. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option from the menu.")
