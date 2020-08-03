Interfaces Intro
----------------
In this section we will cover another very important part of **Shadow**: interfaces. In a broad sense, an **interface** is like a contract with a class: it is made up of one or more methods that the class is required to provide implementation for. For example, consider the following simple interface. It will be used to guide our analysis for the next few sections. 

.. code-block:: shadow 
    :linenos: 

    interface tutorials:interfaces@CanVacation
    {
        vacation() => (); 
    }

Basic Syntax
^^^^^^^^^^^^

The syntax for creating interfaces is very simple. Instead of using the reserved word ``class``, we use ``interface InterfaceName`` in the header, as seen in **Line 1**. Then, in the body of the interface, there should be a collection of one or more method headers, **without any implementation provided**. 

As illustrated in **Line 3**, there are a few differences between method headers in an interface and those in regular classes. For one, interface methods cannot be marked ``public``, ``private``, or ``protected`` because they will **always be public by definition.** The whole purpose of an interface is to require a class to implement its methods, which would not be possible if a method was marked as ``private``. However, interface methods **can** be marked as ``readonly``. Lastly, the method header must end with a semicolon and should not include braces. 

Naming
^^^^^^

By convention, interface names usually begin with ``Can`` and then some word(s) which suggests the ability that the interface ensures. For example, based on the interface name ``CanVacation`` and its single method, ``vacation()``, it is reasonable to assume that the classes that implement this interface have the ability to "take a vacation." 

However, for some interfaces that have many abilities (or methods), it does not make sense to use ``Can``. The ``List`` interface, which will be covered in a later tutorial, is a perfect example of this. It has numerous methods, so naming it something like ``CanDoListyThings`` would not be super clear. 

Implementation
^^^^^^^^^^^^^^
At this point you are probably wondering *how* to implement an interface. Take a look at the two classes below. 

First, is the ``Bermuda`` class: 


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:interfaces@Bermuda is CanVacation 
    {
        public vacation() => ()
	{
	    Console.printLine("Get ready! You are going to " # this # "!"); 
	    Console.printLine("Good luck flying through the Bermuda Triangle!"); 
	}
	
	public readonly toString() => (String) 
	{
	    return "Bermuda"; 
	}

    }


Second, is the ``Madagascar`` class: 

.. code-block:: shadow 
    :linenos: 


    import shadow:io@Console;

    class tutorials:interfaces@Madagascar is CanVacation 
    {
        public vacation() => ()
	{
	    Console.printLine("Get ready! You are going to " # this # "!"); 
	    Console.printLine("Take some pictures of the lemurs!"); 
	}
	
	public readonly toString() => (String) 
	{
	    return "Madagascar"; 
	}

    }


First, let’s examine **Line 3** of both classes. As you can see, ``class ClassName`` is followed by ``is CanVacation`` in each class header. The keyword ``is`` tells the program that the class **implements** the following interface -- in this case, ``CanVacation``. What does this mean for the ``Bermuda`` and ``Madagascar`` classes? They must provide implementation for **all** methods in the interface ``CanVacation``, or else you will get a compile error. 

Examine **Lines 5-9** in both classes to see how the implementation works. First and foremost, the method header must *exactly* match the header in the interface, with one exception. Although in an interface each method is automatically marked as ``public``, you will explicitly need to include the keyword ``public`` in the class method headers (and if a method is marked ``readonly`` in the interface, you must also include it in the class method header). Lastly, there are no restrictions to what is included in the method body, but make sure that if the method has a return type, you have a correct ``return`` statement. 


Driver Program
^^^^^^^^^^^^^^


Below is a sample driver program and console output for the above interface and classes. 


.. code-block:: shadow 
    :linenos: 

    Bermuda bermuda = Bermuda:create(); 
    bermuda.vacation(); 
    Console.printLine(); 
		
    CanVacation madagascar = Madagascar:create(); 
    madagascar.vacation(); 
		

.. code-block:: console

    Get ready! You are going to Bermuda!
    Good luck flying through the Bermuda Triangle!

    Get ready! You are going to Madagascar!
    Take some pictures of the lemurs!


First and foremost, it is important to understand that **you may not create objects/instances of interfaces**. You can, and should, create instances of the classes that implement interfaces, as shown in the example above. 

Let’s look at the ``bermuda`` object first. It is an object of the ``Bermuda`` class, and the ``vacation()`` method is called on it. The syntax is the same as discussed in the :ref:`Classes: The Basics<Classes: The Basics>` tutorial. 

Now, look at the declaration of the ``madagascar`` object. The object itself is an instance of the ``Madagascar`` class, but it is stored as type ``CanVacation``, an interface. Although there is no real difference between these two different ways of instantiating an object, it is often useful to store an object in an  ``interface`` type variable. If you happen to change the object in one place, you would not need to modify any code that expects an ``interface``. 

.. note:: Although you can declare a variable to be an ``interface`` **type**, you may not write something like ``CanVacation:create();``. It would cause a compile error. 

Implementing Multiple Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another important feature of interfaces is that a class can implement multiple interfaces. The syntax for the class header is below: 

.. code-block:: shadow 

    class ClassName 
    is CanSomething
    and CanSomething2
    and CanSoOn

The order the interfaces are presented in *does not matter* so long as they are separated by ``and``. 

What does this mean for the body of the class? Now, the class must implement **every method** of every interface stated in its class header in order for the code to compile. 

For example, let’s say that we added an interface called ``CanScubaDive`` that has one method called ``scubaDive()`` and both ``Madagascar`` and ``Bermuda`` implement it. Now, look back at the driver program from the previous section. If we added the expression ``bermuda.scubaDive();`` , the ``scubaDive()`` method from the ``Bermuda`` class would execute as expected. However, what if we added ``madagascar.scubaDive();`` ? Would the code compile? **No.** It would not compile because ``madagascar`` is declared to be of type ``CanVacation``. This means that when you try to call a method from another interface (in this case, ``CanScubaDive``), the method would not be defined in this context. Therefore, when a class implements more than one interface, pay attention to the variable type when creating objects of the class. 

No Default Implementation
^^^^^^^^^^^^^^^^^^^^^^^^^

If you are familiar with Java, you are probably wondering if it is possible for an ``interface`` to provide a default implementation for some or all of its methods. In **Shadow** the answer is **no**. You will get a compile error if you try to do so. **The whole purpose of an interface is to outline methods that a class is forced to implement itself based off of the specific needs/function of the class itself**. 

















