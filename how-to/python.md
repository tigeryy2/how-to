# Python References

Python notes and references

## Project Setup and Packaging

Python project setup, packaging, tools.

### Project Structure

Typical Project Structure:

    project-name/
        project-name/
            __init__.py
            __main__.py
        tests/
            __init__.py
        docs/
            docs.md
        setup.py
        LICENSE
        README.md
        .gitignore

See [python project template](https://github.com/tigeryy2/python-template).

### Project Setup

Provide a `setup.py` to enable Python project setup.

The `setup.py` script allows installation of the project, both as a standalone project and as a package in another
project.

    """
    Setup script for project.
    
    To install as a standalone project run::
    
        pipenv install -e .
    
    This installs project in editable mode using this file .
    
    To install as a package, particularly as a submodule inside another project::

    pipenv install -e path-to-submodule

    This installs the project in editable mode as a package
    """
    import pathlib
    
    from setuptools import find_packages, setup
    
    HERE = pathlib.Path(__file__).parent
    
    VERSION = "0.1.0"
    PACKAGE_NAME = "python-template"
    AUTHOR = "Tiger Yang"
    AUTHOR_EMAIL = "tigeryyang@gmail.com"
    DESCRIPTION = "python-template"
    LONG_DESCRIPTION = (HERE / "README.md").read_text()
    LONG_DESC_TYPE = "text/markdown"
    
    # use `setuptools.find_packages` to discover all modules and packages from the project
    setup(name=PACKAGE_NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          long_description_content_type=LONG_DESC_TYPE,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          packages=find_packages(exclude=['docs', 'tests']))

See [setup.py template](https://github.com/tigeryy2/python-template/blob/main/setup.py).

References:

- https://oak-tree.tech/blog/python-packaging-primer
- https://shunsvineyard.info/2019/12/23/using-git-submodule-and-develop-mode-to-manage-python-projects/

## Builtin Modules and Functions

Python built-in modules, functions, and tools.

### dataclass

Provides `@dataclass` decorator for basic functionality for classes used to hold data.

    from dataclasses import dataclass

    @dataclass
    class Person:
        # type hints are mandatory in data classes to include fields
        # optionally, use the `Any` type
        name: str
        age: int
        height: float
        weight: float
        
        # use `Literal` type to support typehinting to limited values
        sex: Literal["male", "female"]
        
        # using default values
        address: Optional[str] = None
        
        # freely define methods, just as in a normal class
        def workout(duration: float):
            ...

    tiger = Person("Tiger Yang", 24, 6, 180, "male", address="Austin, Texas")

Dataclasses provides the `__init__`, `__repr__`, and `__eq__` methods.

See [realpython dataclasses](https://realpython.com/python-data-classes/)
and [Literals](https://adamj.eu/tech/2021/07/09/python-type-hints-how-to-use-typing-literal/).

### namedtuple

Tuple and Dictionary like objects to store values in both key-value and iterative patterns. Use `collections.namedtuple`

    # example from geeksforgeeks.org
    from collections import namedtuple
      
    # Declaring namedtuple()
    Student = namedtuple('Student', ['name', 'age', 'DOB'])
      
    # Adding values
    S = Student('Nandini', '19', '2541997')
      
    # Access using index
    print("The Student age using index is : ", end="")
    print(S[1])
      
    # Access using name
    print("The Student name using keyname is : ", end="")
    print(S.name)

See [namedtuple-in-python](https://www.geeksforgeeks.org/namedtuple-in-python/)

### Pathlib

Python's built-in module for filesystem paths. See [pathlib docs](https://docs.python.org/3/library/pathlib.html)
and [realpython pathlib](https://realpython.com/python-pathlib/).

#### Get path of current file

Use `pathlib.Path(__file__).resolve()` to get path to the current file.

    import pathlib
    # directory of the current file
    pathlib.Path(__file__).parent.resolve()
    
    # current working directory
    pathlib.Path().resolve()

#### pathlib.resolve()

Removes any symlinks and makes a path absolute.
