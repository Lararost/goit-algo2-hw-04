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

        return self._count_suffix_matches(
            node=self.root,
            current_word="",
            pattern=pattern,
        )

    def _count_suffix_matches(
        self,
        node,
        current_word: str,
        pattern: str,
    ) -> int:
        count = 0

        if node.value is not None and current_word.endswith(pattern):
            count += 1

        for char, child in node.children.items():
            count += self._count_suffix_matches(
                node=child,
                current_word=current_word + char,
                pattern=pattern,
            )

        return count

    def has_prefix(self, prefix) -> bool:
        """
        Повертає True, якщо в Trie є хоча б одне слово
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
