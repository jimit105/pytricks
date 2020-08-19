# Underscore in Python

Besides its usage as a normal variable, `_` is a special variable in Python which returns the value of the last executed expression in Python interpreter.

This is useful when we would like to access the result of the previous calculation or we would like to interact with objects without assigning a name.

**Example - 1**
```python
>>> a = 10
>>> a + 5
15
>>> _
15
```

**Example - 2**
```python
>>> list()
>>> _.append(10)
>>> _.append(5)
>>> _
[10, 5]
```
