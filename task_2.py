def stop_words(words: list):
    def function(func):
        def wrapper(*args, **kwargs):
            sentence = func(*args, **kwargs)
            for word in words:
                sentence = sentence.replace(word, "*")
            return sentence
        return wrapper
    return function
 

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

print(create_slogan("Steve"))