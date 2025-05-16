import datetime

def add_note(filename):
    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Entry not added.")
        return

    location = input("Enter location: ")
    text = input("Enter note text: ")

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"Date: {date_str}\n")
        f.write(f"Location: {location}\n")
        f.write(f"Text: {text}\n")
        f.write("---\n")
    print("Entry added successfully.")

def search_notes(filename):
    search_term = input("Enter date (YYYY-MM-DD) or keyword to search: ").lower()
    found_entries = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            all_entries = f.read().split("---\n")
            for entry in all_entries:
                if not entry.strip():
                    continue
                if search_term in entry.lower():
                    found_entries.append(entry.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    if found_entries:
        print("\nFound entries:")
        for entry in found_entries:
            print(entry)
            print("---\n")
    else:
        print("No entries found matching your search.")

def analyze_travels(filename):
    visited_locations = set()
    total_records = 0
    total_words = 0

    try:
        with open(filename, "r", encoding="utf-8") as f:
            all_entries = f.read().split("---\n")
            for entry in all_entries:
                if not entry.strip():
                    continue
                total_records += 1
                lines = entry.strip().split("\n")
                location = ""
                text = ""
                for line in lines:
                    if line.startswith("Location:"):
                        location = line.split(": ")[1]
                        visited_locations.add(location)
                    elif line.startswith("Text:"):
                        text = line.split(": ")[1]
                        total_words += len(text.split())
                    elif not line.startswith("Date:"):  
                        total_words += len(line.split())

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    print("\nTravel Analytics:")
    print(f"Number of visited locations: {len(visited_locations)}")
    print(f"Total number of entries: {total_records}")
    print(f"Total number of words in entries: {total_words}")

def main():
    """Main function of the program."""
    notebook_file = "travel_notes.txt"

    while True:
        print("\nTravel Notes")
        print("1. Add new entry")
        print("2. Search entries")
        print("3. Travel analytics")
        print("4. Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            add_note(notebook_file)
        elif choice == "2":
            search_notes(notebook_file)
        elif choice == "3":
            analyze_travels(notebook_file)
        elif choice == "4":
            print("Thank you for using the travel notes!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()