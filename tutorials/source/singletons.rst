Singletons
----------

In other programming languages, when a method or a variable is marked as ``static``, it means that the method or variable is shared between all instances of a class. It does not "belong" to an individual object. However, in **Shadow** ``static`` does not exist. Instead, we are able to create a specific type of class called ``singleton``. In a broad sense, defining a  ``singleton`` class means that **only one object of that class can exist at one time,** per thread. For example, if your program has 5 threads, only one copy of the object is allowed to exist in each. 

Although creating a ``singleton`` class can be helpful, it should not be used too often. Some popular applications of ``singleton`` would be to either log data (e.g. logging patient info in a doctor’s office database), or to keep track of the number of times a particular object is created. Overall, the goal is put a lot of information **into** the ``singleton`` (like with a logger), as opposed to taking information out of it. 

How does this work? Take a look at the example below. The ``singleton`` object keeps track of the number of times a ``CovertOperation`` object is created.
 

Example
^^^^^^^
There are three classes that make up this example: ``CovertOperation``, ``OperationTracker`` (``singleton``), and ``MissionDriver``. 

Let's first look at ``OperationTracker``, which is a ``singleton`` class. Its purpose is to keep track of the number of ``CovertOperation`` objects created. 

.. code-block:: shadow 
    :linenos: 

    singleton tutorials:singletons@OperationTracker
    {
        get int numOperations = 0; 
	
        public startMission() => ()
        {
            numOperations += 1; 
        }
    }


Notice how in the ``singleton`` header the keyword ``class`` is omitted. You will get a compile error if you try to include it. There is one **member variable**, ``numOperations``, and its purpose will be made clear with the next class example. The important thing to note is that there is no constructor for the ``singleton``. Instead, we declared and initialized the member variable at the same time. However, a ``singleton`` *can still have a constructor*. The caveat is it **cannot take in any parameters**. It must simply initialize any member variables. 

.. note:: The properties ``get`` and ``set`` can be used with member variables of ``singleton`` classes.


Now, let's break down the ``CovertOperation`` class. 

.. code-block:: shadow 
    :linenos: 

    class tutorials:singletons@CovertOperation
    {
        get set String password; 
	get code secret; 
	OperationTracker track; 
	
	public create(String p, code s)
	{
	    password = p; 
	    secret = s; 
            track.startMission(); 
	}
    }



``CovertOperation`` is a simple class with 3 member variables, including a ``singleton`` object -- ``tracker``. The constructor, which starts on **Line 7**, initializes ``password`` and ``secret``. As seen in **Line 11**, the method ``startMission()`` is called on ``tracker``, which is a  ``singleton``.  This ensures that every time a ``CovertOperation`` object is created, the ``singleton`` object’s member variable ``numOperations`` is incremented by 1. So, in basic terms, ``tracker`` represents the number of times a ``CovertOperation`` object has been instantiated. 

You might be asking, "How can ``tracker`` keep track of the total number of objects created, when each ``CovertOperation`` object has its own ``tracker`` member variable?" In reality, the ``tracker`` member variable **is actually the same object** for every instance of the ``CovertOperation`` class. After all, the whole point of a ``singleton`` is to only allow one object of the class to exist at one time. 

In order to truly see how a ``singleton`` is useful in this example, we must examine an excerpt from the driver class, ``MissionDriver``. 


.. code-block:: shadow 
    :linenos: 

    OperationTracker ot; 
    Console.printLine("Number of Operations: " # ot->numOperations); 
		
    CovertOperation firstMission = CovertOperation:create("password", 'k'); 
    Console.printLine("Number of Operations: " # ot->numOperations); 
		
    CovertOperation secondMission = CovertOperation:create("biscuits", 'p'); 
    Console.printLine("Number of Operations: " # ot->numOperations); 

Console output: 

.. code-block:: console

    Number of Operations: 0
    Number of Operations: 1
    Number of Operations: 2

In **Line 1** it *appears* that we are creating another ``OperationTracker`` object. This is not possible: both ``ot`` in the driver program and ``tracker`` in ``CovertOperation`` **are the same object**. That is why, after each time we use the ``get`` property to retrieve the value ``numOperations`` from ``ot``, it reflects the ``track.startMission()`` call from the ``OperationTracker`` constructor.  We never needed to call ``startMission()`` on ``ot`` to increment the ``numOperations``. It is kept track of "behind the scenes" as we continue to create more ``CovertOperation`` objects. See the console output above. 

As a final note, it may seem strange that we never initializd the ``OperationTracker`` object with ``create``. If you tried to write ``OperationTracker tracker = OperationTracker:create();`` you would get a compile error. This makes sense. Again, the whole point of a ``singleton`` is to have one object of the class at a time. The object’s creation is handled in the first method where it appears.


A note on ``Console``
^^^^^^^^^^^^^^^^^^^^^

The ``Console`` class is a great example of a ``singleton``.  The fact that only one ``Console`` object exists can be used as a shortcut for accepting user input and using ``Console.printLine()`` statements. See the example below: 

.. code-block:: shadow 
    :linenos: 

    Console out; // no create needed (or possible)
    out.printLine("Bring rap justice!");
    Console screen; // still the same object
    screen.printLine("Shut 'em down!");


Other Features
^^^^^^^^^^^^^^

As a wrap-up, there are 2 final noteworthy features of ``singleton``. 

For one, it is legal to store a ``singleton`` in a regular object. For example, this would compile: ``Object o = ot;`` (where ``ot`` is a ``singleton`` from the above examples). It is important to keep in mind that ``o`` will not "behave" like a regular object. 

Lastly, a ``singleton`` class **can** implement an interface. The syntax is the same. 






