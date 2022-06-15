# Anagrams

## Task

In this Kata, you will be given a wordlist. Your task is to write
code to determine which words in this wordlist are anagrams.
Be aware that the given wordlist here is relatively large with roughly
340.000 unique words, so very straightforward solutions may not work here.

## Important Notes

The file is not in ASCII, but in ISO-8859 encoding. You can specify the encoding
when opening the file in Python:

```
with open("wordlist.txt", encoding="ISO-8859-1") as file:
    pass
```

When solved correctly, you should end up with 20683 sets of anagrams
(a total of 48162 words).

## Some Tips

### Testing

We encourage you to use TDD to write your code. A file to execute your unit
tests already exists. Be aware that your test cases have to start with the
word `test`; otherwise they will not be executed upon calling `unittest.main()`.

This works ✅

```
def test_function_runs_correctly():
    assert True
```

This doesn't work ❌

```
def function_should_work():
    assert True
```

### Python Best Practices

**Type Hints**

It is strongly encouraged to use Type Hints for readability.
The Type Hints are ignored by the Python runtime, so they won't affect
the behaviour of your code. They're there just for humans and potentially
your IDE. Use them like this:

```
def add(x: int, y: int) -> int:
    pass
```

For more non-primitive datatypes, you'll have to use an import statement:

```
from typing import List

def sum_all(list_of_numbers: List[int]) -> int:
    pass
```

**Read Files**

There are two ways that you can open and read a file:

```
f = open('wordlist.txt')
data = f.read()
# mutate or pass data
f.close()
```

This requires you to manually close the file. Instead, I suggest using the following code:

```
with f as open('wordlist.txt'):
    data = f.read()
    # mutate or pass data
```

The `with` statement ensures that the file is automatically closed, which
means you won't have to think about cleanup operations. You could also use
it to open several files at once, for example if you want an input- and an output-file.

**Timing**

There is a lot of optimisation you can perform with this task. The solution
I currently have runs the whole wordlist at 700ms on the 2021 M1 Macbook Pro.
There are several ways to time your code, but you can use this code snippet:

```
def main():
    start = datetime.datetime.now()
    
    # do stuff
    
    end = datetime.datetime.now()
    
    delta_in_ms = (end - start).total_seconds() * 1000
```