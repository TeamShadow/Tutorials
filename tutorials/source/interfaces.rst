**********
Interfaces
**********

In this tutorial we will cover another very important part of Shadow: *interfaces*. In a broad sense, an interface is like a contract a class must follow: It's made up of methods that the class is required to provide implementations for. For example, consider the following simple interface. It will be used to guide our examples for the next few sections. 

.. code-block:: shadow 
    :linenos:

    interface tutorials:interfaces@CanVacation
    {
        vacation() => (); 
    }

	
Interface syntax
================

The syntax for creating interfaces is simple. Instead of using the reserved word ``class``, we use ``interface`` before the interface's name, as seen on **Line 1** above. Then, in the body of the interface, there should be a collection of one or more method headers, without any implementation provided. 

As illustrated on **Line 3**, there are a few differences between method headers in an interface and those in regular classes. For one, interface methods cannot be marked ``public``, ``private``, or ``protected`` because they will *always* be public by definition. The purpose of an interface is to require a class to provide a series of methods for use by other code, which would not be possible if a method was marked ``private``. However, interface methods *can* be marked ``readonly``. Lastly, the method header must end with a semicolon and should not include braces. 

Interface naming
================

By convention, Shadow interface names often begin with ``Can`` and then some words which suggests the ability that the interface ensures. For example, based on the interface name ``CanVacation`` and its single method ``vacation()``, it's reasonable to assume that the classes that implement this interface have the ability to take a vacation. 

However, for some interfaces that have many methods, it doesn't make sense to name them starting with ``Can``. The ``List`` interface, which will be covered in a later tutorial, is a perfect example. It has numerous methods, so naming it something like ``CanDoListyThings`` would be needlessly wordy. 

Implementing interfaces
=======================

At this point you are probably wondering *how* to implement an interface. Take a look at the two classes below. 

First, the ``Bermuda`` class: 


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


Second, the ``Madagascar`` class: 

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


First, let's examine **Line 3** of both classes. In each case, the class name is followed by ``is CanVacation``. The keyword ``is`` tells the program that the class *implements* the following interface -- in this case, ``CanVacation``. What does this mean for the ``Bermuda`` and ``Madagascar`` classes? They *must* provide implementations for *all* methods in the interface ``CanVacation`` or else there will be a compiler error. 

Examine **Lines 5-9** in both classes to see how the implementation works. First and foremost, the method header must *exactly* match the header in the interface, with one exception: Although each method in an interface is implicitly marked ``public``, you will need to explicitly include the keyword ``public`` in the class method headers.  If a method is marked ``readonly`` in the interface, it must also be marked ``readonly`` in the class method header. Lastly, there are no restrictions on what's included in the method body.  A class is free to implement interface methods however it wants, as long as it conforms to the expectations for the parameters and return types. 

Below is a sample driver program and console output for the above interface and classes:

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


Note that you can *never* create instances of interfaces. An interface is not a template for objects; it's a list of promises to write methods. You can, and should, create instances of the classes that implement interfaces, as shown in the example above. 

Let's look at the ``bermuda`` variable first. It stores an object of the ``Bermuda`` class, and we call its  ``vacation()`` method on **Line 2**. The syntax for creating the object and calling methods is the same as discussed in the :ref:`Classes` tutorial. 

Now, look at the declaration of the ``madagascar`` variable. The object itself is an instance of the ``Madagascar`` class, but it's stored in a variable with type ``CanVacation``, an interface. If you don't care about the specific type of the object, merely its ability to do certain things, it can be useful to store such an object in an  ``interface`` variable that reflects the abilities you care about. One of the benefits of this approach is that you can easily change the type of the object that's stored in the ``interface`` variable, yet no other code will need to change.

.. note:: Although you can declare a variable to be an ``interface`` type, it is illegal to write code that instantiates an interface, such as ``CanVacation:create()``.

Implementing multiple interfaces
================================

Another important feature of interfaces is that a class can implement *multiple* interfaces. The syntax for such a class header is below: 

.. code-block:: shadow 

    class ClassName 
    is CanSomething
    and CanSomethingElse
    and CanYetAnotherThing

The order the interfaces are presented in doesn't matter, but they must be separated by the ``and`` keyword. 

What does this mean for the body of the class? Now, the class must implement *every* method of *every* interface stated in its class header in order for the code to compile. 

For example, let's say that we added an interface called ``CanScubaDive`` that has one method called ``scubaDive()`` and both ``Madagascar`` and ``Bermuda`` implement it. Now, let's update the driver program from a previous section, adding ``scubaDive()`` to both objects as follows:

.. code-block:: shadow 
    :linenos:

    Bermuda bermuda = Bermuda:create(); 
    bermuda.vacation();
	bermuda.scubaDive();
    Console.printLine(); 
		
    CanVacation madagascar = Madagascar:create(); 
    madagascar.vacation();
	madagascar.scubaDive();

Adding the ``scubaDive()`` method on **Line 3** works fine, but adding the ``scubaDive()`` method on **Line 7** prevents the code from compiling.  The problem is that ``madagascar`` is declared to be of type ``CanVacation``. We know that the object itself has the ability to call the ``scubaDive()`` method, but the compiler sees a ``CanVacation`` variable storing an object that may or may not include the ``scubaDive()`` method. 

.. note:: In Java 8 and higher, it's possible for an ``interface`` to provide a default implementation for some or all of its methods. In Shadow, this is not possible since the purpose of an interface is only to outline methods that a class must implement. 

















