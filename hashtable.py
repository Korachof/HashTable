class Hash:
    def __init__(self, size = 7):
        self.hash_map = [None] * size

    def __hash(self, key):
        """
        Runs a hash that will find a place in memory for the given key
        :param key: The given key to be hashed
        :return: the hash result
        """
        hash_time = 0
        for letter in key:
            hash_time = (hash_time + ord(letter) * 31) % len(self.hash_map)

        return hash_time




