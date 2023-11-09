


# Synytax Errors

Syntax errors
## Semantic Errors

Semantic errors occur when our code doesn't **MEAN** what we 
intend it to MEAN

These errors in Mr. Ubial's opinion, are FAR MORE challenging
to spot and fix

One way to solve this problem is to use [[Strings#String Methods|string methods.]]
We can use `.lower()` to fix this error.


```python
user_response = input("Do you like to eat food?")

if user_response.lower() == "yes":
	print("You are a human indeed")
else:
	print("What are you a robot????")
```

The problem with the code above is subtle. What I (Mr. Ubial) mean
is that EVERY ANSWER OF YES should go into the YES block