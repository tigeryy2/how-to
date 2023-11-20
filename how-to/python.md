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

#### Unpacking Dataclasses

Use the `dataclasses.astuple(obj)` method to unpack a dataclass instance into a tuple. Note that this is recursive.

See
[python 3.7 dataclass unpacking](https://stackoverflow.com/questions/37837520/implement-packing-unpacking-in-an-object)
and [as-tuple deep copy](https://stackoverflow.com/questions/51802109/why-is-dataclasses-astuple-returning-a-deepcopy-of-class-attributes/51802661#51802661)

#### Dataclass `__post_init__`

Use the `__post_init__` method in dataclasses to run code immediately after initialization of the dataclass'
attributes. This can replace code normally placed in the `__init__` method of a typical class, and is a good
place to set attributes that are not simply provided by the user.

    @dataclass
    class Vehicle:
        brand: str
        catalogue_price: int
        electric: bool
        license_plate: str = field(init=False)

        def __post_init__(self):
            self.license_plate = generate_vehicle_license()
   
        @property
        def tax(self) -> int:
            tax_rate = 0.02 if self.electric else 0.05
            return int(tax_rate * self.catalogue_price)

    def main():
        tesla = Vehicle("Tesla Model 3", 6000000, True)
        volkswagen = Vehicle("Volkswagen", 3500000, True)
        print(tesla.tax)
        print(volkswagen.tax)

#### Dataclass `keyword-only __init__ parameters`

Introduced in Python 3.10, dataclasses can now be created in keyword-only mode.

    @dataclass(kw_only=True)
    class SomeData:
        name: str
        value: str

In this example, both the parameters to the generated __init__ are keyword-only. The generated __init__ is:

    def __init__(self, *, name:str, value:str):

Keyword only mode is useful for dataclass inheritance.
See [py3.10 new dataclass features](https://www.trueblade.com/blogs/news/python-3-10-new-dataclass-features)

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

### Collections

The `collections.abc` module provides Abstract Base Classes for various containers. These containers provide various
interfaces.

#### Making an object subscriptable and iterable

Providing the `__getitem__` and `__setitem__` magic methods allows usage of subscripts directly on the object.
Further, providing the `__len__` method allows automatic generation of the `__next__` and `__iter__` functionalities.

    class SomeContainer:
        def __init__(self):
            self.items = list(range(10))
    
        def __getitem__(self, index):
            return self.items[index]
    
        def __setitem__(self, key, value):
            self.items[key] = value
    
        def __len__(self):
            return len(self.items)

    container = SomeContainer()
    # can directly use subscripts instead of using `container.items[0]`
    zero = container[0]

    # iterate over container, `__iter__` is autogenerated
    for item in container:
        print(item)

### Asterisks

The `*` and `**` operators in python can be used in several ways, including tuple unpacking, iterator unpacking into
lists, and more.

See [asterisks in python](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/).

### Single Line if else

For example: `value = <value_if_true> if <expression> else <value_if_else>`

## Python Related Tools

Python related tools such as `pip`, `virtualenv`, `pipenv`, `conda`.

### Conda Install and Setup

See https://docs.conda.io/en/latest/miniconda.html for install link. Use `miniconda` as it doesn't download all packages
by default.

1. Install miniconda with installer
2. Add `\path\to\miniconda\condabin` to `PATH`
    - Don't add `miniconda\Scripts`, this exposes a bunch of other things (python, etc)
3. Run `conda init`, and optionally `conda update conda`

See [Adding conda to path windows](https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10)