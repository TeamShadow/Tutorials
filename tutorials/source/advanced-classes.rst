****************************
Advanced Features of Classes
****************************

Now that we have covered the basics of classes in Shadow, we can move on to some of their more advanced features. 

Deep copying
============

Shadow has the ability to create *deep copies* of objects. Making a deep copy means not only copying the object but making deep copies of all members of the object as well.  With a few exceptions, making a deep copy of an object means that every member variable inside the object will have the same contents yet be a new object stored in a new location.

The process of deep copying is built into Shadow and is intended to be a central part of thread communication in Shadow.  Although threading is not yet fully implemented, the intention is that sending an object from one thread to another will automatically involve creating a deep copy so that that threads don't share data, preventing data races.

Shadow uses the keyword ``copy`` to create a copy of an object.  Although the syntax is simple, care should be taken when using the ``copy`` command because it will deeply copy *everything* inside of the object.  If the object only contains a few primitive member variables, the process will be quick and efficient.  However, if the object is a list that contains millions of objects, all of those objects (and references to objects they contain) will be copied as well.

See below for an example of using ``copy``, which references the ``Otter`` class from the :ref:`previous tutorial <Classes>`: 

.. code-block:: shadow 

    Otter oliver = Otter:create("Oliver", "ocean"); 
    Otter oscar = copy(oliver); 

As you can see, you simply write ``copy(objectName)`` and store the result in an appropriate type. The ``Otter`` ``oscar`` is now a deep copy of ``oliver`` -- including deep copies of all of its members. Any changes to ``oscar`` will not be reflected in ``oliver``. Internally, the ``copy`` command keeps track of all new objects allocated. If a circular reference would cause an object to be copied a second time, the ``copy`` command instead uses the first copy. An exception to the rule is ``immutable`` objects, which cannot be changed anyway. References to such objects are assigned directly, without making copies of the underlying objects.

The ``copy`` keyword can be used on arrays as well.  Because it's a deep copy, making changes to objects inside of a copy won't change the objects inside of the original. Let's see an example using ``copy`` on an array.  First, let's make a very short class called ``Number`` that holds an ``int`` called ``value``:

.. code-block:: shadow 
	
	class tutorials:advanced@Number
	{
		get set int value;
		
		public create(int value)
		{
			this:value = value;
		}
	}

Then, we can create an array of ``Number`` objects containing the values ``3``, ``5``, and ``7``, respectively.
	
.. code-block:: shadow 
    :linenos:
	
	Number[] original = {Number:create(3), Number:create(5), Number:create(7)};
    Number[] copied = copy(original); 
    for(int i = 0; i < copied->size; i += 1)
    {
        Console.printLine("copied[" # i # "]: " # copied[i]->value);
    }
		
    copied[0]->value = 9; 
		
    Console.printLine("original[0] :" # original[0]->value); 
    Console.printLine("copied[0]: " # copied[0]->value); 

Below is the console output: 

.. code-block:: console

    copied[0]: 3
	copied[1]: 5
	copied[2]: 7
	original[0]:3
	copied[0]:9

The expression ``copy(original)``  on **Line 2** creates an entirely new array with fresh copies of all the ``Number`` objects from ``original`` and stores the result into ``copied``. When we change ``value`` inside of the first element in ``copied`` to 9 on **Line 8**, it does *not* change the ``value`` inside the first element in ``original``.  If we had made a copy of ``original`` using the ``subarray()`` method, for example, the ``value`` *would* have changed in the ``original`` because the first element in a *shallow* copy of the array would still point at the same object.


Immutable classes and references
================================

In a :ref:`previous tutorial <\`\`String\`\` and Numerical Methods>`, we mentioned that the ``String`` class is *immutable*. An immutable object is one whose value *cannot* be changed after it's been created.

In Shadow, the ``String`` class is not the only thing that's ``immutable`` -- other classes and references can be as well. We will start by looking at ``immutable`` classes. Consider the example below: 


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    /* Imagine you own a restaurant and you are looking to hire a 
     * another server. You use this class to create application 
     * objects. Once an object is created, which represents one
     * application, its contents can never change. Thus, we declare 
     * the class to be immutable.
     */

    immutable class tutorials:advanced@JobApplication
    {
        get String name; 
        get int age; 
        get boolean experience; 
        get String skill; 

        public create(String name, int age, boolean experience, String skill) 
        {
            this:name = name;
            this:age = age; 
			this:experience = experience; 
			this:skill = skill; 
        }
	
        public evaluate() => () 
        {
            if (age <= 18 or experience == false) 
			{
				Console.printLine(name # " is not qualifed for the job."); 
			}
			else 
			{
				Console.printLine(name # " would be a great employee!"); 
			}	
        }
    }

In order to declare a class to be ``immutable``, we simply have to put the ``immutable`` modifier before the ``class`` keyword as we do on **Line 10**.  The constructor and other methods within the class *cannot* be marked ``immutable``, just the class header. 

Aside from the keyword ``immutable``, the ``JobApplication`` class does not appear to be any different from the the regular classes we have written. However, notice how none of the member variables are marked with the keyword ``set``. If you tried to do so, you would get a compiler error because data inside an ``immutable`` object cannot be changed after the object is created. Furthermore, any method (other than the constructor) that tries to change the contents of an object of an ``immutable`` class will result in a compiler error. Yet the method ``evaluate()`` is valid because it only uses the values of some member variables without trying to change them.

Using an ``immutable`` class is no different from any other class, as seen in the driver code below:

.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:advanced@ApplicationDriver
    {
        public main( String[] args ) => ()
		{
			JobApplication chris = JobApplication:create("Chris", 20, true, "positive attitude"); 
			chris.evaluate(); 	
		}
    }

The console output is: 

.. code-block:: console
    
    Chris would be a great employee! 

Syntax aside, why is it beneficial to create ``immutable`` classes, and why would we want to create ``immutable`` objects and references? The answer is program safety.  You can pass around ``immutable`` objects with confidence that they won't be changed.  This knowledge allows the compiler to make some optimizations that it otherwise wouldn't be able to. 

This idea becomes even more important when it's extended to *thread safety*. If  you have a program that is multi-threaded in another programming language, it's possible that more than one thread could be trying to change a single object at the same time. This could lead to unintended results or errors in the program.  Shadow doesn't allow threads to share mutable data, requiring deep copies of all objects passed from one thread to another.  However, ``immutable`` objects do not need to be copied because they can't be changed. Thus, by creating as many ``immutable`` objects as possible, you make your programs safer and your multi-threaded programs faster.


The ``freeze`` keyword
----------------------

It's possible to declare an entire class with the ``immutable`` keyword, but what if you only need a particular reference to be ``immutable``?  You can declare any local or member variable with the ``immutable`` keyword.  If you try to store an object whose class is ``immutable`` into an ``immutable`` reference, everything will work fine.

However, you can't store a normal object into an ``immutable`` reference without using the ``freeze`` keyword.  The ``freeze`` command creates an ``immutable``, deep copy of the object it's called on. 

Here's an example in which we freeze an instance of the ``Number`` class we defined earlier in this tutorial:

.. code-block:: shadow 
    
	immutable Number number = freeze(Number:create(42));
	Console.printLine(number->value);

Using ``freeze`` creates an ``immutable`` reference to a non- ``immutable`` object, allowing us to store it in the ``immutable`` reference ``number``.  We are able to use the ``value`` ``get`` property to print out the value ``42``.  However, if we had tried to use the ``set`` version of the ``value`` property to change ``value`` to something else, the code would not have compiled.

The ``readonly`` keyword
------------------------

When an object is stored in an ``immutable`` reference, only its ``readonly`` methods can be called.  These are the methods that are guaranteed not to change values inside of the object.  In an ``immutable`` class, all methods are implicitly ``readonly``.  In a regular class, methods must be explicitly marked ``readonly``.  By default, ``get`` properties for primitive types and ``immutable`` member variables are implicitly ``readonly``.

In addition to methods, references can be marked ``readonly`` as well.  Like an ``immutable`` reference, only ``readonly`` methods can be called from a ``readonly`` reference.  The key difference is that a ``readonly`` reference only guarantees that the object won't be changed through this particular reference while an ``immutable`` reference guarantees that the object won't be changed *ever*.  One way to think about it is that an ``immutable`` reference behaves as if *all* references to that object are ``readonly``.

We use ``readonly`` references to resolve a problem: An ``immutable`` reference can't be stored into a regular reference, and (without using ``freeze``) a regular reference can't be stored into an ``immutable`` reference.  To mediate between the two different kinds of references, ``readonly`` references are used. You can store either a normal reference or an ``immutable`` reference in a ``readonly`` reference.

Although methods and references can be marked ``readonly``, classes can't be, since a ``readonly`` class would really be the same as an ``immutable`` class.


The ``toString()`` method
=========================

Every object has a ``toString()`` method that returns a ``String`` representation of that object.  This method is defined in the ``Object`` class, and other objects get that default implementation through a process called *inheritance*, which will be discussed in detail in the :ref:`Inheritance` tutorial.

This default implementation of the ``toString()`` method isn't very useful:  All it does is return the full type name of the object as a ``String``.  However, you can write your own ``toString()`` method to give a more meaningful ``String`` representation for the objects of any class you create.

For example, let's pretend we have a simple class representing guests visiting Shadow State Park, located in the Method Mountains. The member variables represent the guest's name, length of stay, and preferred activity, respectively. See below for the full class: 

.. code-block:: shadow 
    :linenos:  
    
    import shadow:io@Console;

    class tutorials:advanced@Guest
    {
        get String name; 
		get set int days; 
		get set String activity; 
		
		public create(String name, int days, String activity) 
		{
			this:name = name; 
			this:days = days; 
			this:activity = activity; 
		}
		
		public readonly toString() => (String)
		{
			String part1 = name # " is staying for " # days # " days"; 
			String part2 = " and would like to go " # activity; 
			
			return part1 # part2; 			
		}	
    }


Here's an excerpt from the driver program and its console output: 

.. code-block:: shadow 

    ShadowPark guest1 = ShadowPark:create("Natasha", 3, "rock climbing"); 
    Console.printLine(guest1); 

.. code-block:: console

    Natasha is staying for 3 days and would like to go rock climbing

The ``toString()`` method is overridden on **Lines 16-22**. If a programmer decides to override the ``toString()`` method in any class, the method header *must* match ``public readonly toString() => (String)`` exactly. Omitting ``readonly`` will cause a compile error, as the ``toString()`` method cannot make changes to the object it's called on. 

Using ``Console.printLine(objectName)``, ``objectName.toString()``, or ``#objectName`` will produce the ``String`` value returned by the ``toString()`` method for ``objectName``.  If the programmer overrode the ``toString()`` method for its class, the output will be a customized ``String`` representing that object.  Otherwise, the output will just be the type name.