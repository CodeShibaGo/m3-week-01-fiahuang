def find_capitals(word):
    capitals = [char for char in word if char.isupper()]
    return ''.join(capitals)