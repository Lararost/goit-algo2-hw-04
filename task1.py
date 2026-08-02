from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")

        return self._count_suffix(self.root, "", pattern)

    def _count_suffix(self, node, current_word, pattern):
        count = 0

        if node.value is not None and current_word.endswith(pattern):
            count += 1

        for char, child in node.children.items():
            count += self._count_suffix(
                child,
                current_word + char,
                pattern,
            )

        return count

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")

        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True


if __name__ == "__main__":
    trie = Homework()

    words = ["apple", "application", "banana", "cat"]

    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів за суфіксом
    assert trie.count_words_with_suffix("e") == 1
    assert trie.count_words_with_suffix("ion") == 1
    assert trie.count_words_with_suffix("a") == 1
    assert trie.count_words_with_suffix("at") == 1

    # Перевірка префіксів
    assert trie.has_prefix("app") is True
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True
    assert trie.has_prefix("ca") is True

    print("All tests passed!")
