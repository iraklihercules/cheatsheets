
## 4 Paradigms of OOP
- **Encapsulation:** Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. It allows data hiding, where the internal representation of an object is hidden from the outside world, and access to the data is restricted to methods defined within the class. In Python, encapsulation is achieved through the use of classes, where attributes are defined as class variables and methods are defined as functions within the class.
- **Abstraction:** Abstraction is the process of hiding the complex implementation details of an object and only exposing the essential features and functionalities to the outside world. It allows developers to focus on what an object does rather than how it does it. In Python, abstraction is achieved by defining interfaces (abstract classes or interfaces) that define the methods that subclasses must implement without specifying how they are implemented.
- **Inheritance:** Inheritance is the mechanism by which a new class (subclass) can inherit properties (attributes and methods) from an existing class (superclass). It promotes code reuse and allows for the creation of a hierarchy of classes with increasing levels of specialization. Subclasses can override methods or add new methods to customize the behavior inherited from the superclass. In Python, inheritance is implemented using the syntax class SubClass(SuperClass):.
- **Polymorphism:** Polymorphism allows objects to be treated as instances of their parent class or any of their subclasses interchangeably. It enables code to work with objects of different classes through a uniform interface, without needing to know the specific class of each object at compile time. Polymorphism in Python is primarily achieved through method overriding, where subclasses can provide their own implementation of methods defined in the superclass, and method overloading is achieved through the use of default arguments or variable-length argument lists. Python also supports duck typing, where the type of an object is determined by its behavior rather than its explicit type.


## Common Design Patterns
- **Singleton Pattern:** Ensures that a class has only one instance and provides a global point of access to that instance.
- **Factory Method Pattern:** Defines an interface for creating an object, but allows subclasses to alter the type of objects that will be created.
- **Abstract Factory Pattern:** Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
- **Builder Pattern:** Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
- **Prototype Pattern:** Creates new objects by copying an existing object, thus avoiding the need to instantiate new objects.
- **Adapter Pattern:** Allows incompatible interfaces to work together by providing a wrapper that converts the interface of a class into another interface that a client expects.
- **Decorator Pattern:** Attaches additional responsibilities to an object dynamically, providing a flexible alternative to subclassing for extending functionality.
- **Proxy Pattern:** Provides a placeholder for another object to control access to it, allowing for additional functionality such as lazy initialization or access control.
- **Observer Pattern:** Defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.
- **Strategy Pattern:** Defines a family of algorithms, encapsulates each one, and makes them interchangeable, allowing the algorithm to vary independently from clients that use it.
- **Command Pattern:** Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.
- **Template Method Pattern:** Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.
- **State Pattern:** Allows an object to alter its behavior when its internal state changes, encapsulating state-specific behavior into separate classes and delegating the responsibility for state transitions.
- **Iterator Pattern:** Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- **Composite Pattern:** Composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and compositions of objects uniformly.
