# PistiClassKata - Solution

# Description

Your task is to group similar characters in a text. You will be given a string and a specification of similar characters. 

You should split the input text into longest possible sequences of character that fall into the same class. Unclassified characters should fall into a single default character class.

It can be safely assumed, that the given text is always a string, and after solving this Kata programming will never be the same again.

# Example

```
text = "Hello Pisti"
character_classes = [['i'], ['e', 'l']]

magic_splitter(text, character_classes)
// --> ["H", "ell", "o P", "i", "st", "i"]
```

If no character class is given, every character falls into the single default one:

```
text = "Hello Pisti"
character_classes = []

magic_splitter(text, character_classes)
// --> ["Hello Pisti"]
```
