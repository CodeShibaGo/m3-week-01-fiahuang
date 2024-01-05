member = [(45, 12.5), (55, 9.0), (65, 8.0), (21, 11.5)]

def categorize_new_member(data):
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            print("Senior")
        elif x[0] < 55 and x[1] > 7:
            print("Senior")
        else:
            print("Open")
    pass


categorize_new_member(member)