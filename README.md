# startpoint

`pip3 install startpoint`

A simple python module providing a sane alternative to `if __name__ == "__main__"`

To use, simply declare an entry point like so:

```python
from startpoint import entrypoint

@entrypoint(__name__)
def main():
    print("Hello, World!")
```

In this example, `main` will be called only if the file is executed directly, not if imported.
You can also specify a behaviour that will happen when the module is imported:

```python
@entrypoint(__name__, alt=lambda:print("I'm not a library!"))
def main():
```

You can also declare an entry point that take an argument, in which case `sys.argv` will be passed in:

```python
@entrypoint(__name__)
def main(args):
```
