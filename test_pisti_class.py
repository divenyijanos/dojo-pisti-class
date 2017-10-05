from unittest import TestCase
from pisti_class import PistiClass


class TestPistiClass(TestCase):
    def test_magic_splitter_returnsTextInArrayWhenEmptyCharacters(self):
        text = "Hello Pisti"
        character_classes = []
        self.assertEqual(PistiClass(character_classes).magic_splitter(text), ["Hello Pisti"])

    def test_magic_splitter_TwoCharacters_returnSplittedCharactersWhenCharacterSetContainsOneOfThem(self):
        text = "ab"
        character_classes = [["a"]]
        self.assertEqual(PistiClass(character_classes).magic_splitter(text), ["a", "b"])

    def test_magic_splitter_ThreeCharacters_returnSplittedCharactersWhenCharacterSetContainsOneOfThem(self):
        text = "abc"
        character_classes = [["a"]]
        self.assertEqual(PistiClass(character_classes).magic_splitter(text), ["a", "bc"])

    def test_magic_splitter_returnSplittedTextWhenEveryCharIsInCharSet(self):
        text = "abc"
        character_classes = [["a"], ["b"], ["c"]]
        self.assertEqual(PistiClass(character_classes).magic_splitter(text), ["a", "b", "c"])

    def test_magic_splitter_ThreeCharacters_returnSplittedCharactersWhenCharacterSetContainsMiddleOfThem(self):
        text = "abc"
        character_classes = [["b"]]
        self.assertEqual(PistiClass(character_classes).magic_splitter(text), ["a", "b", "c"])

    def test_magic_splitter_ComplexCharacterClasses(self):
        text = "Hello Pisti"
        character_classes = [['i'], ['e', 'l']]
        self.assertEqual(PistiClass(character_classes).magic_splitter(text), ["H", "ell", "o P", "i", "st", "i"])
