Polymorphism and Casting
------------------------

This brief, but very important, tutorial on **polymorphism** and **casting** touches on a key **Object-Oriented** programming principle. **Polymorphism**, an often confusing term to define, is best understood in terms of an example. 

Consider the classes from the :ref:`inheritance tutorial<Inheritance>`. There is a parent class called ``Employee`` and 3 child classes: ``Waiter``, ``Chef``, and ``Manager`` (only the ``Waiter`` implementation is shown, as ``Chef`` and ``Manager`` were given as exercises). All 3 of these child classes will inherit the methods ``clockIn()`` and ``clockOut()`` from ``Employee``. Let’s say we decided to **override** ``clockIn()`` in the child classes and create a method in the driver class called ``work()``. ``work()`` takes in an ``Employee`` object as a parameter and calls the object’s ``clockIn()`` method. Since ``Chef``, ``Manager``, and ``Waiter`` are all children of ``Employee``, you could pass objects of **any** of these classes as parameters legally. 

Now, the "same" ``work()`` method calls on children of ``Employee`` give completely different results, as they all have overridden the ``clockIn()`` method . This is the  essence of polymorphism: that many different objects can be passed into the same method yet result in many different behaviors. After all, polymorphism literally means "many forms". 

The following example will hopefully solidify your understanding of polymorphism, and lead us into casting. 

Example
^^^^^^^^

First, here is our parent class, ``SeaCreature``. 

.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:polymorph@SeaCreature
    {
        get String type; 
	get String ocean; 
	
	public create(String t, String o)
	{
	    type = t; 
	    ocean = o; 
	}
	
	public swim() => ()
	{
	    Console.printLine("This " # type # " is swimming!"); 
	}
    }

The following are two child classses of ``SeaCreature``. 


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:polymorph@Dolphin is SeaCreature
    {
	public create(String t, String o)
	{
	    super(t,o); 
	}
	
	public swim() => ()
	{
	    Console.printLine("This " # this->type # " jumps above the waves!"); 
	}
    }

 

.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:polymorph@Turtle is SeaCreature
    {
        public create(String t, String o)
	{
	    super(t,o); 
	}
	
	public swim() => ()
	{
	    Console.printLine("This " # this->type # " glides through the water!"); 
	}
    }

Lastly, the driver program and console output are provided below. 

.. code-block:: shadow 
    :linenos: 

    SeaCreature creature = SeaCreature:create("Creature", "Arctic"); 
    creature.swim(); 
		
    SeaCreature dolphin = Dolphin:create("Dolphin", "Atlantic"); 
    dolphin.swim(); 
		
    SeaCreature turtle = Turtle:create("Turtle", "Pacific"); 
    turtle.swim(); 

.. code-block:: console

    This Creature is swimming!
    This Dolphin jumps above the waves!
    This Turtle glides through the water!

Before we delve into **polymorphism**, make sure to read through the classes above and the console output. If the information does not look familiar, it would be a good idea to revisit the :ref:`inheritance tutorial<Inheritance>` before continuing. 

Static vs Dynamic Type
^^^^^^^^^^^^^^^^^^^^^^
In the **driver program**, the **static type** of each object is ``SeaCreature``. An object’s static type (seen on the left side of the equals sign) is the type that is checked at **compile time**. 

When would you get a compile error? Let’s say that ``Dolphin`` has a method called ``dive()`` that ``SeaCreature`` does not, and we made the method call ``dolphin.dive()``. **This code would not compile** because the static type of ``dolphin`` is ``SeaCreature``, and ``SeaCreature`` does not have a ``dive()`` method. Even though **dynamic type** of ``dolphin`` is   ``Dolphin`` (has the ``dive()`` method), it does not matter because **static type** is what is checked at compile time. An object’s **dynamic type**, seen on the right side of the equals sign, is what is checked at **run time**. 

.. note:: The error message would be: ``Undefined symbol: Method dive not defined in this context``

This concept of **dynamic type** leads us into the next point. Look at **Lines 4-8** in the driver program. We call ``swim()`` on both ``dolphin`` and ``turtle``. You may be asking yourself, how do we know which ``swim()`` method will be executed -- the one in ``SeaCreature`` or the overridden one in ``Dolphin``/``Turtle``? Although the static type determines if the program will compile, the object’s dynamic type determines which method will run. For ``dolphin``, its dynamic type is ``Dolphin``, so the ``swim()`` method in that class will run. The same goes for ``turtle``; its dynamic type is ``Turtle``, so the swim method in ``Turtle`` will run, as seen in the console output. This is a prime example of **polymorphism** in action. Both ``turtle`` and ``dolphin`` share the same type, but perform different actions when ``swim()`` is called on them. 


Casting
^^^^^^^

**Casting** is another feature of Shadow that also demonstrates **polymorphism**. In basic terms, **casting** is when we change the type of any object to another compatible type.  
 
The general syntax for casting is as follows: 

``cast<typeCastingTo>(referenceBeingCast)``

Using the ``SeaCreature``, ``Dolphin``, ``Turtle``, and driver classes above, consider the following example: 

.. code-block:: shadow

    SeaCreature creature2 = cast<SeaCreature>(turtle); 
    creature2.swim(); 
		

Here, the first statement on the right side of the equals sign is the *cast*. We are casting a pre-existing ``turtle`` object into the type ``SeaCreature`` (This would have worked the same way if the static type of ``turtle`` had been either ``SeaCreature`` or ``Turtle``) Why does this work? Recall the idea of an **is-a** relationship from the :ref:`inheritance tutorial<Inheritance>`. Since ``Turtle`` **extends** ``SeaCreature``, a ``Turtle`` object is *always* a ``SeaCreature`` and therefore can be cast to the type of its parent class without error. This is called **widening** (going from a more narrow class to a broader one). 

This is an example of an **explicit** cast. However, we do not need to use an explicit cast in order to store a ``Turtle`` object in a ``SeaCreature``. We could have just as easily written ``SeaCreature creature2 = turtle;`` This is called an **implicit cast**.

Now look at the second statement. Which ``swim()`` method do you think will run? The one from ``SeaCreature``, or the one from ``Turtle``? Since we have cast ``turtle`` into a ``SeaCreature``, your instinct might be to say that the ``SeaCreature`` version of swim will run. However, the ``swim()`` method from ``Turtle`` is actually executed. Even though ``turtle`` has been cast to a ``SeaCreature``, it still does not change the fact that its dynamic type is ``Turtle``. For object types, ``cast`` only changes the static type.

Suppose we wanted to cast a ``SeaCreature`` into a ``Turtle`` as shown below. Would this compile?


.. code-block:: shadow

    Turtle turtle2 = cast<Turtle>(creature); 

Although the code would compile (syntax of the cast is correct), it would cause a runtime error, ``CastException``, because the type ``SeaCreature`` is not compatible with ``Turtle`` when you are trying to cast ``SeaCreature`` to ``Turtle``. This is called **narrowing**. Why? Once again think about an **is-a** relationship. While a ``Turtle`` object is always a ``SeaCreature``, a ``SeaCreature`` *could* be a ``Turtle``, but it could also be a ``Dolphin``. You are trying to go from a broad type to a more specific one.  Thus, the statement is ambiguous and we get a runtime error. 

However, **narrowing** does not always cause a compile error. Consider the example below:

.. code-block:: shadow

    SeaCreature creature2 = cast<SeaCreature>(turtle); 
    turtle = cast<Turtle>(creature2); 
		
We are using the same ``SeaCreature`` object from the first example -- we have cast a ``Turtle`` object into a ``SeaCreature`` (widening). In the second line of code, we are casting ``seaCreature2`` back to ``Turtle`` and storing the result in a ``Turtle`` object. Although we are casting from a broader type to a narrower type, this is legal because technically the dynamic type of ``seaCreature2`` is still ``Turtle``. 


It is also worth mentioning that **side-casting** in Shadow is **always illegal**. For example, you cannot cast a ``Turtle`` to a ``Dolphin`` or vice versa, despite the fact that they are both subclasses of ``SeaCreature``.

Lastly, as a final note on casting, since ``Object`` is the root class for all ``Classes``, you can always cast an object to type ``Object``. See the example below. 


.. code-block:: shadow

    String s = "Help me";		
    Object o = cast<Object>(s);

Primitive Casting
^^^^^^^^^^^^^^^

Although we have discussed casting in terms of objects so far,  it also possible to cast  **primitive types** as well. 

**Numeric Casting**

We will first discuss casting between numeric types. 

For example, consider the short segment of code below: 

.. code-block:: shadow 
    :linenos: 

    var w = cast<double>(8); 
    Console.printLine(w); 
    double x = 8; 
    Console.printLine(x);

**Lines 2 and 4** both print  8.0 to the console. However, you may be wondering what the difference is, then, between how ``w`` and ``x`` were initialized. ``w`` is initialized with an **explicit cast** from a ``int`` to a ``double``. On the other hand, ``x`` is an example of an **implicit cast**; 8 becomes 8.0 when stored in a ``double``. 

Now, let’s look another example: 

.. code-block:: shadow 
    :linenos: 
    
    var y = cast<int>(8.5); 
    Console.printLine(y); 
    
    int z = 8.0;

**Lines 1 and 2** of the above segment of code should look familiar. Now, we are simply casting a ``double`` to an ``int``. However, what do you think will be printed to the console: 8 or 9? **The answer is 9**. Although the decimal point is truncated, 8.5 is still rounded to the nearest whole number when being converted to an ``int``. (8.4 would give 8 as the result). 

Turn your attention to **Line 3**. Although this may seem like legal **implicit casting**, this line of code will cause a compile error because ``double`` is not a subtype of ``int``. 

Lastly, since ``Object`` is the root class for all classes, it is also legal to say ``Object a = 8;`` because the primitive becomes **wrapped up** into ``Integer``.


**Casting with** ``code``

In this section, we will address a common mistake/assumption that is made when casting from a ``code`` to an ``int``. 

First, look at the two examples below: 

.. code-block:: shadow 
    :linenos:
 
    //example one
    var num = '7'; 
    var anotherNum = cast<int>(num); 
    Console.printLine(anotherNum); 

    //example 2	
    var num2 = 97; 
    var anotherNum2 = cast<code>(num2); 
    Console.printLine(anotherNum2); 


In the first example, we are casting the ``code`` '7' into an  ``int`` called ``num``. You might expect that ``num`` now stores the *numeric* value 7, but this is not the case. It actually holds 55. The **character** 7, when converted to a number is 55. An `ASCII Table <http://www.asciitable.com/>`_ can be used to make these conversions. 

The same applies for converting an ``int`` to a ``code`` like in the second example. The character corresponding to the numeric value 97 is ``a``, and this is what is printed to the console. This is why it is important to be careful and intentional when casting between primitive -- and any -- types. 


.. note:: You may **not** cast a ``String`` to a ``code`` and vice versa. 


    









