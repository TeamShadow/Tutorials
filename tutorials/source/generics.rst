********
Generics
********

*Generics* are a language feature that appears in Shadow, Java, C#, and other languages.  They allow for greater abstraction of code.  While parameters can take on different values in a method call, generics use *type parameters* to take on different types.  In this way, code can be written with a type parameter such as ``T`` that can represent some arbitrary type that is unknown when the code is written.

Generic classes reduce the number of explicit casts needed to write code that can be used in many situations.  They are particularly useful when writing *container classes*, classes like lists or queues that contain collections of other objects.  Using generic classes, it's possible to write a list that can hold elements of type ``T``, which can be instantiated as a list holding ``String`` values, ``Wombat`` values, or values of any arbitrary type.
  
As with many advanced features of Shadow, generics are most easily understood through examples. Since there are several aspects to using generics, we will examine them through an extended example with multiple sections. 

Creating a generic class
========================

The following class, named ``Chest``, demonstrates how to create a generic class. 

.. code-block:: shadow

    class tutorials:generics@Chest<T>
    {
        T object; 
	
        public create(T value)
        {
            object = value; 
        }
	
        public getObject() => (T)
        {
            return object; 
        }
    }

Think of ``Chest`` as a literal chest that could store different kinds of objects. There are endless possibilities as to what you can put inside of a chest: treasure, clothes, books, puzzles, and so on. Notice how the only member variable is ``T object``. While it may seem like ``T`` is the name of a class, it is not. ``T`` is a type parameter that represents a type that will be substituted for a specific class or interface (like ``String``) when an instance of ``Chest`` is created.

We signal to the compiler that ``T`` is a type parameter for ``Chest`` by writing ``class Chest<T>`` in the class header. Putting the type parameter ``T`` between angle brackets indicates that, when an instance of ``Chest`` is created, a type must be specified in its place.  Most generic classes only have a single type parameter, but some have two or three.  Several different type parameters can be specified between the angle brackets and separated by commas.

The rest of the class should look familiar to you. There is a single constructor that takes in an object of type ``T`` as a parameter, and a ``getObject()`` method that returns an object of the same type ``T``.

Note that type parameters are often called ``T``, but there is no requirement for a particular name. Although any legal Shadow variable name can be used, a single capital letter is conventional. While ``T`` is a widely used type parameter because it stands for "type," other common type parameter names are listed below:  

* ``E``: element
* ``K``: key
* ``V``: value

It's also possible to create generic interfaces in the same way that you create generic classes. You simply specify one or more type parameters in angle brackets after the interface name and then use those type parameters in the interface method headers as if they were actual types instead of placeholders for types.
 

Using a generic class
=====================

Now that we have discussed how to *create* a generic class, we'll go over how to *use* a generic class. 

Most programmers write generic classes infrequently but use them often.  For example, the ``shadow:utility`` package contains many generic classes like ``ArrayList<V>`` and ``HashSet<V>`` that are useful for holding lists or sets of objects with arbitrary types.  For more information about these classes, visit the  `documentation page <http://shadow-language.org/documentation/shadow/utility/$package-summary.html>`__ for this package.


Look over the three non-generic classes below. ``Treasure`` is a parent class, and ``Silver`` and ``Gold`` are its children. 

.. code-block:: shadow

    class tutorials:generics@Treasure
    {
        get double value; 
	
        public create(double v)
        {
            value = v; 
        }
    }

.. code-block:: shadow

    class tutorials:generics@Gold is Treasure
    {
        public create(double v)
        {
			super(v); 
        }
    }


.. code-block:: shadow

    class tutorials:generics@Silver is Treasure
    {
        public create(double v)
        {
            super(v); 
        }
    }

Now, consider the following excerpt from a driver class that uses the generic ``Chest`` class:

.. code-block:: shadow
    :linenos: 

    Silver silver = Silver:create(10283.60); 
    Gold gold = Gold:create(230953.34); 

    Chest<Silver> chest1 = Chest<Silver>:create(silver); 
    Chest<Gold> chest2 = Chest<Gold>:create(gold); 

First, in **Lines 1 and 2**, we have created two different objects, ``gold`` and ``silver``, whose types are ``Gold`` and ``Silver``, respectively.

Similarly, in **Lines 4 and 5**, we create two different instances of the generic class ``Chest``: ``chest1`` and ``chest2``. Look carefully at the angle brackets. Recall that ``T`` appeared between the angle brackets in the definition of the ``Chest`` class. When creating an object of the ``Chest`` class, we replace this type parameter with a specific class or interface. In this case, ``chest1`` is a ``Chest`` where ``T`` takes on the class ``Silver``,  and ``chest2`` is a ``Chest`` where ``T`` takes on the class ``Gold``.

Using generic classes gives us both flexibility and type safety.  The object ``chest1`` can *only* store objects of type ``Silver``.  The object ``chest2`` can *only* store objects of type ``Gold``.  Furthermore, when you call ``getObject()`` on ``chest1``, the return type will be ``Silver``, and when you do the same on ``chest2``, the return type will be ``Gold``.

For the sake of clarity, we are typing out explicit type names for ``chest1`` and ``chest2``, but using ``var`` is particularly well suited to declaring variables with generic types since it reduces the number of times you need to write out complex type names.

However, ``Chest`` objects are not limited to storing  ``Treasure`` objects and its children. We could have replaced ``T`` with ``int`` or ``String`` or ``Object``. For example, the following code is perfectly legal: 

.. code-block:: shadow

    Chest<int> numberChest = Chest<int>:create(6); 
    Console.printLine(numberChest.getObject()); 

This code prints ``6`` to the console. Although the ``Chest`` class is simple, it illustrates the beauty of generics. We were able to create three instances of the ``Chest`` class, each acting as a container for a different type, while reusing the same code.

.. note:: Unlike in Java, it's legal to supply a primitive type such as ``int`` as an argument for a type parameter in Shadow.  However, the compiler creates code to wrap the primitive type in an object, which has some performance penalties.  Special optimizations are done when the generic class contains a generic array that happens to contain primitive types.    


Type bounds
=========== 

Another feature of generics in Shadow is the ability to create *type bounds*. Using bounds with generics allows you specify constraints for acceptable types that can be substituted for a particular type parameter. For example, in our ``Chest`` class above, let's say we wanted ``Chest`` to hold only instances of the ``Treasure`` class and its children. All we would need to do is modify the class header slightly:

.. code-block:: shadow

    class tutorials:generics@Chest<T is Treasure>


Now, if we tried to create ``numberChest`` from the previous section, we would get a compiler error because ``int`` is not a child of ``Treasure``.


Since ``T is Treasure``, we could also add the following method to ``Chest`` in order to access the member variable ``value`` of ``Treasure`` objects (and objects of its children). 

.. code-block:: shadow

    public getValue() => (double)
    {
        return object->value; 
    }

This code would work because every ``Treasure`` object has a ``get`` property for its ``value`` member.  Since we have stipulated ``T is Treasure``, we can treat ``T`` as if it's ``Treasure`` (or one of its children).  Adding a bound on a type parameter means that code inside the generic class knows more about objects of the type parameter and can interact with them in more complex ways, but this complexity comes with the cost of reduced flexibility, since fewer classes are permitted as arguments to the type parameter. 


Additionally, Shadow also allows you to have more than one bound on a type parameter, separated by the keyword ``and``, as in ``T is Treasure and CanHash``. It's illegal to have more than one class bound, since it would be impossible for a single class to be the child of two unrelated classes, but any number of interface bounds can be added.

Generic arrays
==============

Although you should already be familiar with declaring and initializing arrays, arrays can be thought of as instances of a generic ``Array<T>`` class, where ``T`` is the type of element stored in the array.  This definition is primarily to make certain aspects of the compiler and type system simpler. Consider the example below: 

.. code-block:: shadow
    :linenos:

    int[] array1 = int:create[10]; 
    for(int i = 0; i < array1->size; i += 1)
    {
        array1[i] = 7 + (2 * i); 
    }
		
    Array<int> array2 = array1; 
		
    int[] array3 = array2; 
				

In  **Lines 1-5** we have declared and initialized an ``int`` array and filled it using a ``for`` loop. If this syntax doesn't look familiar to you, please revisit the earlier tutorial on :ref:`arrays<Arrays>`. 

Examine **Line 7**. Here, we created another array variable, ``array2``, whose type is ``Array<int>``. On **Line 9**, we are able to store ``array2`` back into the variable ``array3``, whose type is ``int[]``.

As you can see, these assignments did not require an explicit cast.  For most purposes, the compiler treats the generic ``Array`` type and the type declared with square brackets as interchangeable.  Most programmers will find the normal square bracket declaration style to be more convenient in almost all circumstances.


Operator overloading
====================

As a final discussion on generics, we will touch on *operator overloading* in Shadow. Operator overloading is a tool that allows a programmer to define special meanings for common operators (such as ``+``, ``-``, ``*``, ``%``, and ``==``, among others) when those operators are applied to classes the programmer wrote.  Operator overloading doesn't provide any capabilities that could not be accessed via methods, but it can make code more readable if the operators are used in meaningful ways.

Although generic interfaces are useful for many purposes, a few special, pre-defined interfaces are useful because they allow operator overloading.  Before we dive in, you may want to look over the generic interfaces included in the standard library of the `Shadow API <http://shadow-language.org/documentation/shadow/standard/$package-summary.html>`__. They are listed under the "Interface Summary" section of this page.


The ``CanEqual`` interface
--------------------------

The first generic interface we will consider is ``CanEqual<T>``. If a class implements ``CanEqual<T>``,  it means that the class can test an object of type ``T`` for equality with itself, returning ``true`` if the two objects are identical. The interface also allows the ``==`` operator to be overloaded, calling the method ``equal()`` when this operator is used. Here is the entirety of the ``CanEqual`` interface:

.. code-block:: shadow

	interface shadow:standard@CanEqual<T>
	{
		readonly equal(T other) => (boolean);
	}

In order to implement the ``CanEqual`` interface, ``equal()`` must be implemented with the appropriate type argument.

The class ``Surprise`` implements (among other things) the ``CanEqual<Surprise>`` interface.  Doing so allows two objects of type ``Surprise`` to be compared with the ``==`` operator. 

.. code-block:: shadow
    :linenos:

    class tutorials:generics@Surprise is CanEqual<Surprise> and CanAdd<Surprise>
    {
        get String word; 
		get int magicNumber; 
		
		public create(String word, int number)
		{
			this:word = word; 
			magicNumber = number;  
		}
		
		public readonly equal(Surprise other) => (boolean)
		{
			return word == other:word and magicNumber == other:magicNumber; 
		}
		
		public readonly add(Surprise other) => (Surprise)
        {
            return Surprise:create(word # " " # other:word, magicNumber + other:magicNumber); 
        }
    
        public readonly toString() => (String) 
        {
    	    return # word # ", " # magicNumber; 
        }
    }
	
On **Line 1** we included ``is CanEqual<Surprise>`` in the class header, specifying that a ``Surprise`` object can compare itself for equality with another ``Surprise`` object.  On **Lines 12-15** we provided the implementation for the ``equal()`` method necessary to implement ``CanEqual<Surprise>``. Note that we have replaced ``T`` with ``Surprise`` in the definition of ``equal()``. The method will only return ``true`` if both member variables of the current object and the object passed in as a parameter are equal. However, it's up to the programmer to define the conditions for two objects of the same class to be considered equal. For example, we could have only required the ``String`` member variable ``word`` to be the same for ``equal()`` to return ``true``. 
	
Driver program excerpt: 

.. code-block:: shadow
    :linenos:

    Surprise birthday = Surprise:create("diamond", 57); 
    Surprise party = Surprise:create("watch", 103); 
		
    Console.printLine(birthday.equal(party)); 
    Console.printLine(birthday == party); 
    Console.printLine(birthday + party); 
	
This code shows how ``equal()`` is used. As seen in **Lines 1 and 2**, we have created two instances of the ``Surprise`` class that are not the same. Thus, it should not be shocking that the output for **Lines 4 and 5** are both ``false``. These two different ways of calling the ``equal()`` method are equivalent. However, if ``Surprise`` did not implement the ``CanEqual`` interface and you tried to use ``==`` on these two objects, the code would not compile.	
	
Console output: 

.. code-block:: console

    false
    false
    diamond watch, 160
	


Arithmetic overloading
----------------------

When overloading arithmetic operators, the interfaces ``CanAdd<T>``, ``CanSubtract<T>``, ``CanMultiply<T>``, ``CanDivide<T>``, and ``CanModulus<T>`` can be implemented to allow overloading of the ``+``, ``-``, ``*``, ``/``, and ``%`` operators, respectively.   We'll give an example of how to overload the ``+`` operator by implementing the ``CanAdd<T>`` interface, shown below:

.. code-block:: shadow

	interface shadow:standard@CanAdd<T>
	{
		readonly add(T other) => (T);
	}


Look back at the ``Surprise`` class, which overloads the ``+`` operator. **Lines 17-20** show how we implemented the ``add()`` method of the ``CanAdd`` interface. It contains a public method matching the method header ``readonly add(T other) => (T)``, substituting ``Surprise`` for ``T``. 

Inside this method it's up to the programmer to decide how two objects of a class are "added" together. In our example, we have arbitrarily decided to concatenate the objects' ``word`` variables and add their magic numbers together, using the results as parameters for a new ``Surprise`` object. 

As you can see on **Line 6** of the driver code, we added the objects ``birthday`` and ``party`` together using the ``+`` operator and printed the resulting object, all with a single line of code. Here, using the ``+`` operator is exactly equivalent to writing ``birthday.add(party)``, but using operator overloading is arguably more readable.

.. note:: Operator overloading should be used sparingly.  Defining the ``+`` operator so that "adding" a ``Wombat`` object to a ``Lunchbox`` object creates another ``Lunchbox`` object, for example, would decrease readability instead of enhancing it.  Overloading numerical operators makes the most sense for classes that behave like numbers. Classes representing matrices, vectors, and complex numbers are good candidates.

The other arithmetic operators can be overloaded with similar syntax.













  












