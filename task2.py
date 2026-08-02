from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list):
            raise TypeError("Input must be a list.")

        if len(strings) == 0:
            return ""

        if any(not isinstance(word, str) for word in strings):
            raise TypeError("All elements must be strings.")

        # Створюємо нове Trie
        self.root = Trie().root
        self.size = 0

        # Додаємо всі слова
        for i, word in enumerate(strings):
            self.put(word, i)

        current = self.root
        prefix = ""

        while True:
            # Зупиняємось, якщо:
            # - більше одного нащадка
            # - або кінець одного зі слів
            if len(current.children) != 1 or current.value is not None:
                break

            char = next(iter(current.children))
            prefix += char
            current = current.children[char]

        return prefix


if __name__ == "__main__":
    trie = LongestCommonWord()

    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed!")
