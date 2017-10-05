class PistiClass:
    def __init__(self, character_classes):
        self.character_classes = character_classes

    def magic_splitter(self, text):
        magic_split = []
        for char in text:
            self.add_to_magic_split(magic_split, char)
        return magic_split

    def add_to_magic_split(self, magic_split, char):
        if len(magic_split) and self.compare_character_classes(magic_split[-1][-1], char):
            last_split_element = magic_split.pop() + char
        else:
            last_split_element = char
        return magic_split.append(last_split_element)

    def get_character_class(self, char):
        for character_class in self.character_classes:
            if char in character_class:
                return character_class
        return "default"

    def compare_character_classes(self, char1, char2):
        return (self.get_character_class(char1) == self.get_character_class(char2))
