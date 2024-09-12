import random
mood = ["happy", "sad", "energetic", "calm"]
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in week:
    print(f'(On {day}, you were feeling {random.choice(mood)})')

    
