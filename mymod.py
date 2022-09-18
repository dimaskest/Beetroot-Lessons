def count_lines(path):
    f = open(path)
    counted_lines = (len(f.readlines()))
    return counted_lines    


def count_chars(path):
    f = open(path)
    counted_chars = len(f.read())
    return counted_chars


def count_words(path):
    f = open(path)
    counted_words = len(f.read().split())
    return counted_words


def test(path):
    lines = count_lines(path)
    chars = count_chars(path)
    words = count_words(path)
    file_name = path.split("/")[-1]
    return lines, words, chars, file_name

print(test("c:/Users/User/Desktop/Python/Beetroot academy/Lesson_09/simplefile.txt"))