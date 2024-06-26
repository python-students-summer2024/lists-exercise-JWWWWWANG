import os
import datetime

def assess_mood():
    valid_moods = ["happy", "relaxed", "apathetic", "sad", "angry"]
    data_directory = "data"
    os.makedirs(data_directory, exist_ok=True)
    file_path = os.path.join(data_directory, "mood_diary.txt")
    date_today = datetime.date.today()
    date_today = str(date_today)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                if line.startswith(date_today):
                    print("Sorry, you have already entered your mood today.")
                    return None

    while True:
        current_mood = input("Enter your current mood (happy, relaxed, apathetic, sad, angry): ").strip().lower()
        if current_mood in valid_moods:
            break
        else:
            print("Invalid mood. Please enter one of the following:", ", ".join(valid_moods))

    mood_value = valid_moods.index(current_mood)
    with open(file_path, "a") as file:  
        file.write(f"{date_today} {mood_value}\n")

    if not os.path.exists(file_path) or len(open(file_path, "r").readlines()) < 7:
        print("Not enough entries for diagnosis yet. Please keep using this tool to track your moods!")
        return None
    
    with open(file_path, "r") as file:
        lines = file.readlines()[-7:]

    mood_values = [int(line.strip().split()[1]) for line in lines]
    
    mood_counts = {mood: mood_values.count(mood) for mood in valid_moods}
    diagnosis = ""
    if mood_counts["happy"] >= 5:
        diagnosis = "manic"
    elif mood_counts["sad"] >= 4:
        diagnosis = "depressive"
    elif mood_counts["apathetic"] >= 6:
        diagnosis = "schizoid"
    else:
        most_frequent_mood = max(mood_counts, key=mood_counts.get)
        diagnosis = most_frequent_mood

    print(f"Your diagnosis: {diagnosis.capitalize()}!")


