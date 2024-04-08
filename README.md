# Fifth_Challenge_OOP
In this challenge we have to take the code of the last challenge (https://github.com/DanielBlaDi/Fourth_Challenge_OOP), the Shapes part, and trying to make packages and modules of it, by to ways:

## First_Shape
This folder has the structure that was solicitate (A unique module inside of package shape), in this case, there is a module called ``Shape`` that is inside of the package ``shape``. Also, the package ``shape`` has his own ``main`` inside the folder First_Shape for testing if the program works.

```css
File_structure/
├── First_Shape/
│   ├── shape/
│   │   ├── __init__.py
│   │   └── Shape.py
│   └── main.py
```

## Second_Shape

This folder has the structure that was solicitate (Individual modules that import Shape in inheritates from it), in this case, there is a package called ``shapes`` which has inside of it 3 modules (``Line.py``, ``Point.py``, ``Shape.py``), and a package called ``figures``; inside of this package there are some Individual modules that import Shape in inheritates from it (``Equilateral.py``, ``Isosceles.py``, ``REctangle.py``, ``Scalene.py``, ``Square.py``,``Triangle.py``, ``TriRectangle.py``). Also, the package ``shapes`` has his own ``main.py`` inside the folder Second_Shape for testing if the program works.

```css
File_structure/
├── Second_Shape/
│   ├── shapes/
│   │   ├── __init__.py
│   │   │── Shape.py
│   │   │── Line.py
│   │   │── Point.py
│   │   └── Figures
│   │   │   │── __init__.py
│   │   │   │── Equilateral.py
│   │   │   │── Isosceles.py
│   │   │   │── Rectangle.py
│   │   │   │── Scalene.py
│   │   │   │── Square.py
│   │   │   │── Triangle.py
│   │   │   └── TriREctangle.py
│   └── main.py
```