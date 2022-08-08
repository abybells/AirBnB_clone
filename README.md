<div>
  <img src="https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png" alt="">
</div>

# AirBnB_clone
AirBnB clone project for ALX cohort 5
## PROJECT DESCRIPTION
This repository contains the AirBnB clone project as part of the ALX Software Engineering Project written in Python. The Console is a Data Model management via command interpreter. The Overall project scope is to:
- Build a command line interpreter to manipulate data without a visual interface.
### Concepts

For this project, we expect you to look at these concepts:

- [Python packages](https://alx-intranet.hbtn.io/concepts/66)
- [AirBnB clone](https://alx-intranet.hbtn.io/concepts/74)

  ![Airbnb Console](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220801%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220801T050509Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9d30c1351aed7ca61e6bf8a3e6d637b0059e8e1bd19d4be19764fd598d5e0096)
### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

  - put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
  - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
  - create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
  - create the first abstracted storage engine of the project: File storage.
  - create all unittests to validate all our classes and storage engine
## What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

  - Create a new object (ex: a new User or a new Place)
  - Retrieve an object from a file, a database etc…
  - Do operations on objects (count, compute stats, etc…)
  - Update attributes of an object
  - Destroy an object
## Requirements
### Python Scripts

   - Allowed editors: vi, vim, emacs
   - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
   - All your files should end with a new line
   - The first line of all your files should be exactly #!/usr/bin/python3
   - A README.md file, at the root of the folder of the project, is mandatory
   - Your code should use the pycodestyle (version 2.8.*)
   - All your files must be executable
   - The length of your files will be tested using wc
   - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
   - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
   - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
## Python Unit Tests

   - Allowed editors: vi, vim, emacs
   - All your files should end with a new line
   - All your test files should be inside a folder tests
   - You have to use the unittest module
   - All your test files should be python files (extension: .py)
   - All your test files and folders should start by test_
   - Your file organization in the tests folder should be the same as your project
    e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
    e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
   - All your tests should be executed by using this command: python3 -m unittest discover tests
   - You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
   - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
   - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
   - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
   - We strongly encourage you to work together on test cases, so that you don’t miss any edge case

