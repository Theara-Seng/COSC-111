clubs = {}

def create_club():
    name = input("Enter club name: ").strip()
    key = name.lower()
    if key in clubs:
        print(" Club already exists.\n")
        return

    description = input("Enter club description: ")
    leader = input("Enter leader's name: ")
    co_leader = input("Enter co-leader's name: ")
    while True:
        try:
            max_members = int(input("Enter maximum number of members allowed: "))
            if max_members > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    clubs[key] = {
        "name": name,
        "description": description,
        "leader": leader,
        "co_leader": co_leader,
        "max_members": max_members,
        "members": [],
        "activities": []
    }

    print(f" Club '{name}' created successfully!\n")


def join_club():
    name = input("Enter club name to join: ").strip()
    key = name.lower()
    if key not in clubs:
        print(" Club not found.\n")
        return

    if len(clubs[key]["members"]) >= clubs[key]["max_members"]:
        print(" Sorry, this club is full. You cannot join right now.\n")
        return

    member_name = input("Enter your full name: ")
    for m in clubs[key]["members"]:
        if m["name"] == member_name:
            print(" You already joined this club.\n")
            return

    print("Choose your study year:")
    print("1. Freshman")
    print("2. Sophomore")
    print("3. Junior")
    print("4. Senior")
    year_input = input("Enter 1–4: ").strip()

    year_dict = {
        "1": "Freshman",
        "2": "Sophomore",
        "3": "Junior",
        "4": "Senior"
    }

    study_year = year_dict.get(year_input, "Unknown")
    student_id = input("Enter your student ID: ")
    purpose = input("Why do you want to join this club? ")

    new_member = {
        "name": member_name,
        "year": study_year,
        "id": student_id,
        "purpose": purpose
    }

    clubs[key]["members"].append(new_member)
    print(f" {member_name} has joined '{clubs[key]['name']}'!\n")


def add_activity():
    name = input("Enter club name to add activity: ").strip()
    key = name.lower()
    if key not in clubs:
        print(" Club not found.\n")
        return

    activity_name = input("Enter activity title: ")
    activity_date = input("Enter activity date (e.g., 2025-07-04): ")
    activity_description = input("Enter activity description: ")

    activity = {
        "title": activity_name,
        "date": activity_date,
        "description": activity_description
    }

    clubs[key]["activities"].append(activity)
    print(f" Activity '{activity_name}' added to club '{clubs[key]['name']}'.\n")


def view_all_clubs():
    if not clubs:
        print(" No clubs available.\n")
        return

    print(" List of all clubs:")
    for key in clubs:
        print(f"- {clubs[key]['name']}: {clubs[key]['description']}")
    print()


def view_club_details():
    name = input("Enter club name to view: ").strip()
    key = name.lower()
    if key not in clubs:
        print(" Club not found.\n")
        return

    c = clubs[key]
    print(f"\n Club: {c['name']}")
    print(f" Description: {c['description']}")
    print(f" Leader: {c['leader']}")
    print(f" Co-Leader: {c['co_leader']}")
    
    current_members = len(c['members'])
    max_members = c['max_members']
    print(f" Members: {current_members} / {max_members}")

    if current_members >= max_members:
        print(" This club is FULL.\n")
    else:
        print()

    if not c["members"]:
        print("- No members yet")
    else:
        for m in c["members"]:
            print(f" - {m['name']} | {m['year']} | ID: {m['id']} | Reason: {m['purpose']}")

    print(f"\n Activities ({len(c['activities'])}):")
    if not c["activities"]:
        print(" - No activities scheduled.")
    else:
        for a in c["activities"]:
            print(f" - {a['title']} on {a['date']}: {a['description']}")
    print()