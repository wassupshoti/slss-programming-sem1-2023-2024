
# Format Strings
We can evaluate inside of strings using *f-strings*.
To create an f-string, we can put an f before the opening quote.

```python
fave-food = input("What's your favourite food? ")
print(f"Oooooo, {fave_food} sounds good!")
```

# Strings Methods

[[Methods]] are functions that we can use on [[Objects]]

Sting methods allow us to modify and work with strings

Say for example, we want to make all characters of a string
lowercase

```python
mr_ubial_yelling = "PLEASE PUSH YOUR CHAIRS IN"

print(mr_ubial_yelling.lower())   # lowercase the letters
```

The .`lower()` method takes a string and converts all UPPERCASE
to lowercase

## `.lower()` 

The `.lower()` method takes a string and converts all UPPERCASE
characters to lowercase

We can use `.lower()` to help with [[Errors#Semantic Errors|Errors]]

## `.upper()`

The `.upper()` method. converts all lowercase characters to uppercase in 
a string

## `.strip(str)`

The `.strip()` method removes characters from the beginning and end of
the string

```python
user_feeling = input("how are you feeling? ")

# "good" "Good" "GOOD" "GOOD!" "good." "good?"
if user_feeling.lower().strip("!.,?") == "good":
	print("That's great!")
```


## `.split(str) -> List`

The `.split()` method splits a string into a list, separating the string
based on the characters you give it


```python
grocery_str = "eggs mil cheese hotwheels"

grocery_list = grocery_str.split(" ")
```

