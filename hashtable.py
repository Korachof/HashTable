class Hash:
    def __init__(self, size = 7):
        self.hash_map = [None] * size

    def __hash(self, key):
        hash_time = 0
        for letter in key:
            hash_time = (hash_time + ord(letter) * 31) % len(self.hash_map)

        return hash_time

