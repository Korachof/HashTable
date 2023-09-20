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

    def set_item(self, key, value):
        """
        Set the index of a new key/value pair.
        :param key: The key of the key/value pair
        :param value: The value of the key/value pair
        :return: None
        """
        index = self.__hash(key)
        if self.hash_map[index] is None:
            self.hash_map[index] = []

        self.hash_map[index].append([key, value])

    def get_item(self, key):
        """
        Get the value of the given key
        :param key: the key of the key/value pair to be found
        :return: Value of the given key
        """
        index = self.__hash(key)

        if self.hash_map[index] is not None:

            for element in range(len(self.hash_map[index])):
                if self.data_map[index][element][0] == key:
                    return self.data_map[index][element][1]

    def keys(self):
        """
        Finds and returns all of the keys in the Hash map
        :return: The hash keys
        """
        hash_keys = []

        for element in range(len(self.hash_map)):
            if self.hash_map[element] is not None:
                for hashed_element in range(len(self.hash_map[element])):
                    hash_keys.append(self.data_map[element][hashed_element][0])

        return hash_keys






