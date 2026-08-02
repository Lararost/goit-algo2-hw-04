from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        """
        Повертає кількість слів у Trie,
        які закінчуються заданим суфіксом.
        """
        if not isinstance(pattern, str):
            raise TypeError("Suffix pattern must be a string.")

        if pattern == "":
            return 0

        return self._count_words_with_suffix(self.root, pattern)

    def _count_words_with_suffix(self, node, pattern: str) -> int:
        """
        Рекурсивно обходить усі вузли Trie
        та рахує слова із заданим суфіксом.
        """
        count = 0

        if node.value is not None:
            word = self._get_word_by_value(node.value)

            if word is not None and word.endswith(pattern):
                count += 1

        for child in node.children.values():
            count += self._count_words_with_suffix(child, pattern)

        return count

    def _get_word_by_value(self, value):
        """
        Знаходить слово за значенням, збереженим у Trie.
        """
        return self._find_word(self.root, value, "")

    def _find_word(self, node, target_value, current_word):
        if node.value == target_value:
            return current_word

        for char, child in node.children.items():
            found_word = self._find_word(
                child,
                target_value,
                current_word + char,
            )

            if found_word is not None:
                return found_word

        return None

    def has_prefix(self, prefix) -> bool:
        """
        Перевіряє, чи існує в Trie хоча б одне слово
        із заданим префіксом.
        """
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string.")

        if prefix == "":
            return False

        current = self.root

        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]

        return True


if __name__ == "__main__":
    trie = Homework()

    words = ["apple", "application", "banana", "cat"]

    for index, word in enumerate(words):
        trie.put(word, index)

    assert trie.count_words_with_suffix("e") == 1
    assert trie.count_words_with_suffix("ion") == 1
    assert trie.count_words_with_suffix("a") == 1
    assert trie.count_words_with_suffix("at") == 1

    assert trie.has_prefix("app") is True
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True
    assert trie.has_prefix("ca") is True

    print("Усі тести для завдання 1 пройдено успішно.")
