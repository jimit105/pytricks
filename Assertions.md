# Assertions

The `assert` keyword in Python is used to test a condition.  
If the condition evaluates to `True`, then the program executes as normal.  
But if the condition evaluates to `False`, then the program will raise an `AssertionError` along with an optional message.

**Example - 1**

```python
a = 10
b = 2

assert b != 0, 'Denominator cannot be zero'
print(a/b)
```
```
5.0
```

**Example - 2**

```python
a = 5
b = 0

assert b != 0, 'Denominator cannot be zero'
print(a/b)
```

```python
AssertionError                            Traceback (most recent call last)
<ipython-input-7-b5ac1363a51c> in <module>
      2 b = 0
      3 
----> 4 assert b != 0, 'Denominator cannot be zero'
      5 print(a/b)

AssertionError: Denominator cannot be zero
```
