import random
time = ["morning", "afternoon", "evening"]
mood = ["happy", "sad", "energetic", "calm"]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in week:
    for i in time:
        print(f'(On {day} {i}, you were feeling {random.choice(mood)})')

