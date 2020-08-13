**********
Singletons
**********

In other programming languages, when a method or a variable is marked ``static``, it means that the method or variable is shared between all instances of a class. It does not "belong" to an individual object. However, there is no ``static`` keyword in Shadow. Instead, we are able to create a special type of class called a *singleton*. Like the singleton design pattern it's named for, only one object of a singleton class  can exist at a time, per thread. For example, if your program has five threads, only one copy of the object is allowed to exist in each. 

Although creating a singleton class can be helpful, it should not be used too often. Some popular applications of singletons might be to log data or to keep track of the number of times a particular object is created. In most cases, information will be put into singletons more than taken out.  Singletons should behave as aggregators of information rather than as ways to share information between otherwise unrelated code.
 

Singleton syntax
================

How do singletons work? Take a look at the example below, which contains three classes: ``CovertOperation``, ``OperationTracker`` (the singleton), and ``MissionDriver``.

Let's first consider ``OperationTracker``. Its purpose is to keep track of the number of ``CovertOperation`` objects created.  Defining a singleton is like defining any other class except that the keyword ``singleton`` is used in place of ``class``. 

.. code-block:: shadow

    singleton tutorials:singletons@OperationTracker
    {
        get int operations = 0; 
	
        public startMission() => ()
        {
            operations += 1; 
        }
    }


The singleton contains one member variable, ``operations``. We declared this member variable with an initial value instead of writing a constructor. However, a singleton *can* have an explicit constructor, but it must be the default constructor that takes no parameters.

.. note:: Just like any class, the keywords ``get`` and ``set`` can be used to mark properties for the  member variables of singletons.


Now, let's show the ``CovertOperation`` class:

.. code-block:: shadow 
    :linenos: 

    class tutorials:singletons@CovertOperation
    {
        get set String password; 
		get code secret; 
		OperationTracker track; 
		
		public create(String password, code secret)
		{
			this:password = password; 
			this:secret = secredt; 
			track.startMission(); 
		}
    }



``CovertOperation`` is a simple class with three member variables, including ``tracker`` -- a singleton. The constructor, which starts on **Line 7**, initializes ``password`` and ``secret``. Then, it calls ``startMission()`` on the ``tracker`` object on **Line 11**. This ensures that every time a ``CovertOperation`` object is created, the singleton's member variable ``operations`` is incremented by 1. Doing so allows ``tracker`` to record the number of times a ``CovertOperation`` object has been instantiated. 

But how can ``tracker`` keep track of the total number of objects created, when each ``CovertOperation`` object has its own ``tracker`` member variable? Because it's a singleton, the ``tracker`` member variable is the *same* object for every instance of the ``CovertOperation`` class. After all, the whole point of a singleton is to allow only one object of the class to exist at a time. 

In order to fully appreciate the singleton in action, let's examine an excerpt from the driver class ``MissionDriver``: 


.. code-block:: shadow 
    :linenos: 

    OperationTracker tracker; 
    Console.printLine("Number of Operations: " # tracker->operations); 
		
    CovertOperation firstMission = CovertOperation:create("password", 'k'); 
    Console.printLine("Number of Operations: " # tracker->operations); 
		
    CovertOperation secondMission = CovertOperation:create("biscuits", 'p'); 
    Console.printLine("Number of Operations: " # tracker->operations); 

Console output: 

.. code-block:: console

    Number of Operations: 0
    Number of Operations: 1
    Number of Operations: 2

On **Line 1** we declare another ``OperationTracker`` object.  The ``tracker`` in the driver program and the ``tracker`` in ``CovertOperation`` refer to the same object.  In fact, there's no need to declare a variable in either case, but doing so can be more convenient than typing ``OperationTracker`` repeatedly. Because all ``tracker`` variables refer to the same object, we can use its ``operations`` property to retrieve the total number of times that ``startMission()`` has been called.  Thus, the output reflects that 0, 1, and 2 operations have taken place, depending on the point in time that we retrieve the value from the ``OperationTracker`` singleton.



It may seem strange that we never initialized the ``OperationTracker`` object with ``create``.  The following code would cause a compiler error:

.. code-block:: shadow 

	OperationTracker tracker = OperationTracker:create();


Recall that the point of a singleton is to have one object of the class at a time. The object's creation is handled in the first method where it appears and can *never* be done explicitly.


The ``Console`` singleton
=========================

The ``Console`` class is a good example of a singleton.  The fact that only one ``Console`` object exists can be used to accept user input and produce output with minimal initialization. See the example below: 

.. code-block:: shadow 

    Console out; // No create needed (or possible)
    out.printLine("Bring rap justice!");
    Console screen; // Still the same object
    screen.printLine("Shut 'em down!");
	Console.printLine("Shut 'em, shut 'em down!"); // No variable required


Other singleton features
========================

As a wrap-up, there are two final noteworthy features of singletons. 

First, it's legal to store a singleton reference into a regular object. For example, the following code would compile:

.. code-block:: shadow

	OperationTracker tracker;
	Object o = tracker;

Second, a singleton class can implement interfaces. The syntax is the same as a normal class.