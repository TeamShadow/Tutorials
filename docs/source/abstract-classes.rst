Abstract Classes
----------------

Definition
^^^^^^^^^^^

Drawing heavily on inheritance principles discussed in the previous section, we will now cover ``abstract`` **classes**. An ``abstract`` class is defined as a class that is able to have ``abstract`` methods. 

What do we mean by ``abstract``? Similar to interfaces, if a method is declared to be ``abstract``, no method body is provided, and the method header ends in a semi-colon. Any classes that extend an ``abstract`` **class** *must* provide implementation for every ``abstract`` method in the parent class.  However, not every method has to be ``abstract``. Child classes of an ``abstract`` class also inherit **concrete** (implemented) methods that can be, but do not have to be, overridden. 

How do we create an ``abstract`` class? It’s simple. ``abstract class ClassName`` is the proper syntax. Making an abstract method is similar: ``public abstract methodName() => ();``. You will get a compile error if you try to provide implementation for an ``abstract`` method. 

Now that we have covered *how* to create an ``abstract`` class, it also important to understand *why* we use ``abstract`` classes, and *how* they are different from interfaces. 

In general, programming is about **abstraction**, meaning the goal is to write loosely coupled code that works in multiple places. ``abstract`` classes help us to achieve that end, as ``abstract`` methods provide a general framework that subclasses are forced to implement. 

In addition, ``abstract`` classes are different from interfaces for a couple of reasons. For one, a class may extend only one ``abstract`` class, but it can implement numerous interfaces. Interfaces are **not** allowed to provide default implementation for their methods, but ``abstract`` classes can for any concrete methods. While ``abstract`` classes are able to store data, interfaces **cannot**. 

.. note:: Interfaces and ``abstract`` classes do share something in common: you can not instantiate either using the keyword ``create``. 

Take a look at the example below to see how an ``abstract`` **class** works. 

Example
^^^^^^^^

The first class is ``Vehicle``, the abstract class. 

.. code-block:: shadow 
    :linenos: 
 
    import shadow:io@Console;

    abstract class tutorials:absclass@Vehicle
    {
        get String type; 
	get set int year; 
	get set int miles; 
	get double price; 
	
	public create(String t, int y, int m, double p)
	{
	    type = t; 
	    year = y; 
	    miles = m; 
	    price = p; 
	}
	
	public abstract takeATrip(int mph) => (); 
	
	public buyAuto(double offer) => () 
	{
	    if ( (price - offer) <= 1000 )
	    {
	        Console.printLine("Your offer is accepted! The " # type # " is yours!"); 
	    }
	    else 
	    {
		Console.printLine("Sorry, your offer is too low"); 
	    }
		
	} 
    }

The second is ``Motorcycle``, which extends ``Vehicle``. 


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:absclass@Motorcycle is Vehicle
    {
	
        public create(String t, int y, int m, double p)
        {
            super(t, y, m, p);  
        }
	
        public takeATrip(int mph) => ()
        {
	    Console.printLine("Buckle Up!"); 
	    Console.printLine("Your " # this->type # " is going " # mph); 
	}

    }

Lastly, here is an excerpt from the brief driver class, ``AutoDriver``, and the console output. 


.. code-block:: shadow 
    :linenos:

    Motorcycle harley = Motorcycle:create("Motorcycle", 2012, 8000, 30000.50); 
    harley.buyAuto(29500.50);  
    harley.takeATrip(75);  


.. code-block:: console

    Your offer is accepted! The Motorcycle is yours!
    Buckle Up!
    Your Motorcycle is going 75 mph 
    

 
First, before we get into any explanations, take a few minutes and examine the three classes above. See if you can trace through the driver program and predict the output without looking ahead. 

Now that you have a general idea how the program works, we will first touch on the ``abstract`` class ``Vehicle``. Aside from the word ``abstract`` in the class header and the ``abstract`` method ``takeATrip()`` , ``Vehicle`` does not appear to be any different than the classes we have studied previously. It still has a constructor, member variables, and one concrete method, ``buyAuto()``. 

The second class, ``Motorcycle``, extends ``Vehicle``, as you can tell from the keyword ``is`` in the class header. ``Motorcycle`` does not override ``buyAuto()``, but it must provide default implementation for ``takeATrip()``, as seen in **Lines 11-15**. Notice how in **Line 8** we use the ``super()`` call to invoke the ``Vehicle`` constructor. Using ``super()`` was covered in a :ref:`previous section<Implementation>`. 

Lastly, the driver program should not look any different from any of the examples we have used thus far. We have created a ``Motorcycle`` object and called methods on it. However, it is important to note we could have declared ``harley`` like this as well:  

.. code-block:: shadow 

    Vehicle harley = Motorcycle:create("Motorcycle", 2012, 8000, 30000.50); 


Here, the **type** of the variable ``harley`` is ``Vehicle``, but it is still an instance of the ``Motorcycle`` class. You would get a compile error if you tried to write ``Vehicle:create``. 









