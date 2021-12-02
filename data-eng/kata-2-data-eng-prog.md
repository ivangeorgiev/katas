## Problem:

We are creating a data-driven application which will study StarWars universe. Our application interacts with the [Star Wars public API](https://swapi.dev/) ([https://swapi.dev/](https://swapi.dev/)) to retrieve data.

### Task 1: People Repositiory

#### Option 1: Object Oriented Approach

Create a class to access data from the Star Wars People API (`StartWarsPeopleRepository` class). The class exposes two public methods:

- `list()` - returns a list of persons from Star Wars
- `find(**criteria)` - search for a person, matching given criteria.

Person information returned by the API:

```python
from typing import Optional

class Person:
    name: str
    height: float
    mass: Optional[float]
    hair_color
```

#### Option 2: Functional Approach

Create a module with two functions to access data from the Star War People API:

* `list()` - returns a list of persons from Star Wars
* `find(**criteria)` - search for a person, matching given criteria.

Person information returned by the API:

```python
luke = dict(
    name: "Luke Skywalker",  # str
    height: 172.0,           # float
    mass: 77,                # Optional[float]
    hair_color: "blond"      # str
)
```

#### Example

```python
>>> repo = StartWarsPeopleRepository()
>>> people_list = repo.list()
>>> luke = repo.find(name="Luke Skywalker")
>>> luke.height
172.0

>>> blond_people = repo.find(hair_color="blond")
>>> len(blond_people)
3
```



### Task 2. Profile People

Create a report which shows a profile of the data retrieved from the Start Wars API. The report should include profile of the `height`, `mass` and `hair color` attributes. Use 5 bins (categories) for profiling numerical attributes. `mass` is optional so you might need one additional bin.

#### Example

```
Mass:
   - 11-30: 5
   - 31-50: 7
   - 51-70: 8
   - 71-90: 5
   - 91-110: 2
   - Unknown: 3
```

## Implementation Criteria

- [ ] Tasks implement required functionality in a program language: Python (preferred), Java, JavaScript, Scala, SQL, etc.

- [ ] Candidate is able to properly discuss the solution

- [ ] Implementation correctness

  - [ ] Automated tests are available to confirm correctness
  - [ ] Error conditions are also covered by tests

- [ ] Style and practices

  - [ ] Automated test coverage is above 80%
  - [ ] Solution passes style checks (PEP-8 for Python)
  - [ ] Solution is documented (style guides PEP-257 for docstrings)

  
