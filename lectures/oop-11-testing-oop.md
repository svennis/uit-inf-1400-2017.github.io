Testing Object-Oriented Programs (OOP 11)
=========================================

Why testing?
- Difficult to catch all analytically through code review
- Alternative is to implicitly let users do the testing
- Changing code may break other parts of the system that used to work

Note: testing will not catch all errors. It will only show you that the ones you specifically tested for didn't occur in testing. Likewise, proving mathematically that a program is error free doesn't mean that we know that it will run without bugs. Proofs usually focus on specific properties in a program, so you could, for instance, say that a design is deadlock-free but fail to detect problems in the run-time that causes your program to crash. 

Manual testing is labour-intensive. A small modification one place may break the system in several other places. Testing all potentially influenced places manually is impractical, therefore we normally use automated testing.

Test-driven development
-----------------------

Main mantra: write tests first. Then you can write the code that should pass the tests. 

A few points:
- writing tests after writing the main code often results in forgetting to put the test in
- writing tests afterwards may lead to tests that test the implemented code, you want to focus on the specification of what the code should do instead
- writing the test first may expose that the planned interface is too complicated, and the interface can be changed before implementing it


Unit testing
-------------
Unit testing focuses on testing small units. It's much easier to isolate and find bugs if you can, for instance, test every function or method in your program before you test the combination of many. 

Example built-in library for unit testing in Python: `unittest`. 
https://docs.python.org/3/library/unittest.html

The `TestCase` class has a number of built-in methods for comparing values and results of functions. This can be useful when setting up a set of tests. You add your own test methods by adding methods that start with `test_` and that take no arguments. 

```python
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
```

Running the unit test: 
```
> python3 unittest1.py -v 
test_isupper (__main__.TestStringMethods) ... ok
test_split (__main__.TestStringMethods) ... ok
test_upper (__main__.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

py.test
-------

The unittest library design is based on the JUnit testing framework for Java and results in a lot of boilerplate code. An alternative is `py.test` or `pytest`:  


http://pytest.org/latest/

https://wiki.python.org/moin/PyTest

Documentation: 
http://pytest.org/latest/contents.html#toc

Examples: 
http://pytest.org/latest/example/index.html


Any properly named function can be a test. It doesn't even need to import any library: 

```python
#!/usr/bin/env python3

def test_int_float():
    assert 1 == 1.0
```


```
> py.test-3  pytestex1.py 
========================================== test session starts ==========================================
platform linux -- Python 3.4.2 -- py-1.4.23 -- pytest-2.6.0
collected 1 items 

pytestex1.py .

======================================= 1 passed in 0.01 seconds ========================================
```

You can also use classes:

```python
#!/usr/bin/env python3

def test_int_float():
    assert 1 == 1.0

def poink():
    print("foo")
    assert 2 == 3

class TestFoo():
    def test_int_float(self):
        assert 1 == 1.0
    def test_int_str(self):
        pass
        #assert 1 == "1"
```

```
> py.test-3  -v pytestex1.py
========================================== test session starts ==========================================
platform linux -- Python 3.4.2 -- py-1.4.23 -- pytest-2.6.0 -- /usr/bin/python3
collected 3 items 

pytestex1.py@3::test_int_float PASSED
pytestex1.py@11::TestFoo::test_int_float PASSED
pytestex1.py@13::TestFoo::test_int_str PASSED

======================================= 3 passed in 0.01 seconds ========================================
```


You can also check if a specific exception is raised:

```python
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```


Doctest
--------

Doctest has been mentioned earlier in the course. The advantage here is that you combine documentation and testing.

https://docs.python.org/3/library/doctest.html


### Digression
Doctest taken to the extreme: Literate programming.
http://en.wikipedia.org/wiki/Literate_programming
