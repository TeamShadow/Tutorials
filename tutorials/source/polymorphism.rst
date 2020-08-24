************
Polymorphism
************

This tutorial focuses on *polymorphism* and ends with some additional information about casting. Polymorphism is a confusing term and is best understood in terms of an example. 

Consider the classes described in the :ref:`inheritance tutorial<Inheritance>`: a parent class ``Employee`` and three child classes, ``Waiter``, ``Chef``, and ``Manager``. Only the ``Waiter`` implementation is given, as ``Chef`` and ``Manager`` were suggested as an exercise. All three of these child classes will inherit the methods ``clockIn()`` and ``clockOut()`` from ``Employee``.


Let's say we decided to *override* ``clockIn()`` in the child classes.  Consider the ``work()`` method defined below:

.. code-block:: shadow

	public work(Employee employee, int hours) => ()
	{
		employee.clockIn(hours);
		double money = employee->wage * employee->hoursWorked;
		employee.clockOut();
		return money;
	}


Now, we could create objects of each child class and call the ``work()`` method on them:

.. code-block:: shadow

	Waiter waiter = Waiter:create("Herbert", 5.50);
	Manager manager = Manager:create("Veronica", 16.75);
	Chef chef = Chef:create("Clotilde", 22.45);	
	double totalCost = 0.0;
	totalCost += work(waiter, 4);
	totalCost += work(manager, 6);
	totalCost += work(chef, 8);

Since ``Chef``, ``Manager``, and ``Waiter`` are all children of ``Employee``, we can legally pass in objects of *any* of these classes as parameters into ``work()``.  Even though the method expects an ``Employee`` parameter, Shadow will allow any child of ``Employee`` to be used where an ``Employee`` is required.

However, the same ``work()`` method called on children of ``Employee`` might give completely different results, if they have all overridden the ``clockIn()`` method. This idea is the  essence of polymorphism: Many different objects can be used in the same code yet produce results appropriate to that object. After all, the word *polymorphism* comes from Greek roots meaning "many forms." 

The following example shows the power of polymorphism again. First, here's a parent class, ``SeaCreature``: 

.. code-block:: shadow

    import shadow:io@Console;

    class tutorials:polymorphism@SeaCreature
    {
        get String type; 
		get String ocean; 
		
		public create(String type, String ocean)
		{
			this:type = type; 
			this:ocean = ocean; 
		}
		
		public swim() => ()
		{
			Console.printLine("This " # type # " is swimming!"); 
		}
    }

The following are two child classses of ``SeaCreature``:

.. code-block:: shadow

    import shadow:io@Console;

    class tutorials:polymorphism@Dolphin is SeaCreature
    {
		public create(String type, String ocean)
		{
			super(types, ocean); 
		}
		
		public swim() => ()
		{
			Console.printLine("This " # this->type # " jumps above the waves!"); 
		}
		
		public dive() => ()
		{
			Console.printLine("We dive deep!");
		}
    }

 

.. code-block:: shadow

    import shadow:io@Console;

    class tutorials:polymorphism@Turtle is SeaCreature
    {
        public create(String type, String ocean)
		{
			super(type, ocean); 
		}
	
		public swim() => ()
		{
			Console.printLine("This " # this->type # " glides through the water!"); 
		}
    }

Lastly, the driver program and console output are provided below:

.. code-block:: shadow
	:linenos:

    SeaCreature creature = SeaCreature:create("creature", "Arctic"); 
    creature.swim(); 
		
    SeaCreature dolphin = Dolphin:create("dolphin", "Atlantic"); 
    dolphin.swim(); 
		
    SeaCreature turtle = Turtle:create("turtle", "Pacific"); 
    turtle.swim(); 

.. code-block:: console

    This creature is swimming!
    This dolphin jumps above the waves!
    This turtle glides through the water!
	

Static vs. dynamic type
=======================

In the driver program above, the *static type* of each object is ``SeaCreature``. A variable's static type, the type used to declare the variable, is the type that's checked at compile time. 

When would you get a compile error? Note that the ``Dolphin`` class has a method called ``dive()`` that ``SeaCreature`` does not.  What if we made the method call ``dolphin.dive()``? This code would not compile because the static type of ``dolphin`` is ``SeaCreature``, and ``SeaCreature`` does not have a ``dive()`` method. Even though *dynamic type* of ``dolphin`` is  ``Dolphin``, which has the ``dive()`` method, it doesn't matter because the static type is checked at compile time. An object's dynamic type is the true type of the object itself, not the variable it's stored into. 

This concept of a dynamic type leads us into the next point. Look at **Lines 4-8** in the driver program. We call ``swim()`` on both ``dolphin`` and ``turtle``. You may be asking yourself, how do we know which ``swim()`` method will be executed -- the one in ``SeaCreature`` or the overridden one in ``Dolphin`` or ``Turtle``? Although the static type determines if the program will compile, the object's dynamic type determines which method will run. For ``dolphin``, its dynamic type is ``Dolphin``, so the ``swim()`` method in that class will run. The same goes for ``turtle``; its dynamic type is ``Turtle``, so the ``swim()`` method in ``Turtle`` will run, as seen in the console output.


Abstract classes
================

A tool of inheritance commonly used with polymorphism is *abstract classes*.  An abstract class is marked with the keyword ``abstract`` and can *never* be instantiated.  If a class can never be instantiated, what's its value?  Abstract classes are allowed to contain abstract methods.

Similar to the method headers in interfaces, abstract methods have no method body.  Any classes that inherit from an abstract class must provide an implementation for every abstract method in the parent class (unless the child class is also abstract).  However, not every method in an abstract class must be marked ``abstract``. Child classes of an abstract class will inherit any normal methods and member variables that the abstract class defines.

These normal methods and member variables are the central difference between abstract classes and interfaces.  Interfaces cannot have any implemented methods or contain any data, but abstract classes can.  While an interface is only a list of methods that a class must implement, an abstract class is a list of such methods as well as other methods that are already implemented.

Abstract classes are intended to form a framework that child classes can be built upon.  Of course, this additional power comes at a cost: A child class may only inherit from one class, abstract or otherwise, but it can implement an unlimited number of interfaces. The reason for this limitation is precisely these methods and member variables.  If a class could inherit from more than one class, it might have conflicting definitions for different methods and member variables.  There are also performance issues associated with multiple inheritance.

The goal of both interfaces and abstract classes is abstraction.  We want to write code that can work with a wide range of objects, whose static types need not be known.  All we need to know is that there is a list of methods we can call on a given object, and both abstract classes and interfaces provide this guarantee.

.. note:: Neither interfaces and nor abstract classes can ever be instantiated.  Using the keyword ``create`` with either type will cause a compiler error. 

To create abstract classes, simply put the ``abstract`` keyword in front of the ``class`` keyword when defining the class.  Then, you'll be allowed to put abstract methods in the class.  Making an abstract method is very similar to defining method headers in interfaces, with two differences: You must put the keyword ``abstract`` before the name of the method, and you must mark the method ``public``, ``private``, or ``protected``.  Unlike interface methods, abstract methods do not need to be public, although they usually are.  Just like interface methods, however, abstract methods must have a semicolon after the method header and no method body. 

Take a look at the example below to see how an abstract class works. The first class is ``Vehicle``, the abstract class:

.. code-block:: shadow 
 
    import shadow:io@Console;

    abstract class tutorials:polymorphism@Vehicle
    {
        get String type; 
		get set int year; 
		get set int miles; 
		get double price; 
		
		public create(String type, int year, int miles, double price)
		{
			this:type = type; 
			this:year = year; 
			this:miles = miles
			this:price = price; 
		}
		
		public abstract takeATrip(int mph) => (); 
		
		public buy(double offer) => () 
		{
			if ((price - offer) <= 1000)
			{
				Console.printLine("Your offer is accepted! The " # type # " is yours!"); 
			}
			else 
			{
				Console.printLine("Sorry, your offer is too low"); 
			}			
		} 
    }

The second is ``Motorcycle``, which inherits from ``Vehicle``: 

.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:polymorphism@Motorcycle is Vehicle
    {	
        public create(String type, int year, int miles, double price)
        {
            super(type, year, miles, price);  
        }
	
        public takeATrip(int mph) => ()
        {
			Console.printLine("Buckle up!"); 
			Console.printLine("Your " # this->type # " is going " # mph); 
		}
    }
	
Aside from the keyword ``abstract`` in the class header and the method header for ``takeATrip()``, the ``Vehicle`` class is similar to classes we have seen before. It has a constructor, member variables, and one concrete method, ``buy()``. 

The second class, ``Motorcycle``, inherits from ``Vehicle``, as you can tell from the keyword ``is`` in the class header. ``Motorcycle`` does not override ``buy()``, but it must provide an implementation for ``takeATrip()``, which it does on **Lines 10-14**. Note the ``super()`` call to the ``Vehicle`` constructor on **Line 7**. Using ``super`` in this way was covered in the :ref:`previous tutorial <Calling parent constructors>`. 

Here's an excerpt from a driver class and the console output:

.. code-block:: shadow 
    :linenos:

    Motorcycle harley = Motorcycle:create("motorcycle", 2012, 8000, 30000.50); 
    harley.buy(29500.50);  
    harley.takeATrip(75);  


.. code-block:: console

    Your offer is accepted! The motorcycle is yours!
    Buckle up!
    Your motorcycle is going 75 mph 


In the driver program, we create a ``Motorcycle`` object and call methods on it. However, we could have declared ``harley`` as follows:  

.. code-block:: shadow 

    Vehicle harley = Motorcycle:create("Harley", 2012, 8000, 30000.50); 


Here, the static type of the variable ``harley`` is ``Vehicle``, but its dynamic type is ``Motorcycle``.


Casting reference types
=======================

We discussed casting between primitive types in an :ref:`earlier tutorial <Primitive casting>`.  Casting between primitive types actually changes data from one format inside the computer into another.  It's also possible to use the same syntax to cast between reference types; however, this kind of casting doesn't change how the data is stored.  Instead, it changes the static type of an expression to a different static type.

When using inheritance and polymorphism, it will sometimes be necessary to convert one static type into another.

 
Recall that the syntax for casting is as follows: 

.. code-block:: shadow 

	cast<resultType>(expression)

Using the ``SeaCreature``, ``Dolphin``, ``Turtle``, and driver classes above, consider the following example: 

.. code-block:: shadow
	:linenos:

	Turtle yertle = Turtle:create("Yertle", "pond");
    SeaCreature animal = cast<SeaCreature>(yertle); 
    animal.swim(); 
		
On **Line 1** we create a ``Turtle`` object.  Then, we cast it to the type ``SeaCreature`` on **Line 2**. Why does this work? Recall the idea of an *is-a* relationship from the :ref:`inheritance tutorial<Inheritance>`. Since ``Turtle`` inherits from ``SeaCreature``, a ``Turtle`` object is *always* a ``SeaCreature`` and therefore can be cast to the type of its parent class without error. This process is called *widening* (going from a narrow class to a broader one).

This is an example of an *explicit* cast. However, we don't need to use an explicit cast in order to store a ``Turtle`` object in a ``SeaCreature``. We could have just as easily written ``SeaCreature animal = yertle;`` Doing so would have used an *implicit* cast.

Which ``swim()`` method do you think will run on **Line 3**? Even though ``animal`` is a ``SeaCreature`` variable, it doesn't change the fact that it points at an object whose dynamic type is ``Turtle``. Remember that ``cast`` only changes the static type for reference types.

Suppose we wanted to cast a ``SeaCreature`` into a ``Turtle`` as shown below. Would this compile?


.. code-block:: shadow

	SeaCreature monster = SeaCreature:create("creature", "Black Lagoon");
    Turtle myrtle = cast<Turtle>(monster); 

Although the code would compile, it would cause a runtime error, a ``CastException``, because the ``SeaCreature`` object cannot be cast to a ``Turtle``. The dynamic type of the object that ``monster`` points at is actually ``SeaCreature``, so it can't be changed into the narrower type ``Turtle``. Why? Consider the is-a relationship. While a ``Turtle`` object is always a ``SeaCreature``, this ``SeaCreature`` is not a ``Turtle``.

However, narrowing does not always cause a compiler error. Consider the example below:

.. code-block:: shadow
	:linenos:

    SeaCreature gamera = Turtle:create("Gamera", "space");
    Turtle friendToChildren = cast<Turtle>(gamera); 
		
On **Line 1**, we store a ``Turtle`` object into a ``SeaCreature`` variable, an example of widening the type. On **Line 2**, we cast ``gamera`` back to ``Turtle`` and store the result in the ``Turtle`` variable ``friendToChildren``. Although we are casting from a broader type to a narrower type, this is legal because the true dynamic type of the object is ``Turtle``. 

Note that *side-casting* in Shadow is always illegal. For example, you cannot cast a ``Turtle`` to a ``Dolphin`` or vice versa, despite the fact that they are both child classes of ``SeaCreature``.

As a final note on casting, you can always cast an object to type ``Object`` since it's the parent class for all classes. See the example below.

.. code-block:: shadow

    String message = "Help me";		
    Object object = cast<Object>(message); // Cast is unnecesary
	

Although primitive types are *not* objects, Shadow sometimes needs to wrap them up so that they can be stored in reference variables.  Surprisingly, even the following is legal:

.. code-block:: shadow

    Object number = 8;