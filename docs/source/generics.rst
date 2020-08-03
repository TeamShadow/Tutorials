Generics
--------

In **Shadow** and in programming in general, generics is a very powerful tool. It not only helps to eliminate casting exceptions and other errors at compile time, but provides a framework or a blueprint that is compatible with many different data types. 

In general, generics is best understood through an example. Since there are many different aspects to generics, we will break the example down into different topics. 

Creating a Generic ``class``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following class, named ``Chest``, demonstrates how to create a generic class. 

.. code-block:: shadow
    :linenos: 

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
        public getValue() => (double)
	{
	    return object->value; 
	}
    }

Think of ``Chest`` as a literal trunk/chest that stores many different objects. There are endless possibilities as to what you can put inside of a chest: treasure, clothes, books, puzzles, etc. Thus, we can think of a generic class as a container of sorts. Notice how the only member variable is ``T object``. While it may seem like ``T`` is the name of a class, **it is not**. ``T`` is representative of a type, which will be substituted for a specific class (like ``String``) or interface when an instance of ``Chest`` is created. 
This is also why the ``class`` header says ``class Chest<T>``. The type ``T`` is included in between angle brackets and indicates that when an instance of ``Chest`` is created, a type must be specified in its place. 

The rest of the class should look familiar to you. There is a single constructor that takes in ``T`` as a parameter, and a ``getObject()`` method that turns an object of the same type ``T``. The benefits of using ``T`` will become apparent when we look at the driver program. 

Using a Generic Class
^^^^^^^^^^^^^^^^^^^^^^

Now that we have discussed how to *create* a generic ``class``, we will go over how to *use* a generic ``class``. 

Before we look at the driver program, briefly read through the 3 basic classes that will be referenced in it. ``Treasure`` is the parent, and ``Silver`` and ``Gold`` are the children. 

.. code-block:: shadow
    :linenos: 

    class Treasure
    {
        double value; 
	
        public create(double v)
        {
            value = v; 
        }
    }

.. code-block:: shadow
    :linenos: 

    class Gold is Treasure
    {
        public create(double v)
        {
	    super(v); 
        }
    }


.. code-block:: shadow
    :linenos: 

    class Silver is Treasure
    {
        public create(double v)
        {
            super(v); 
        }
    }

Now, consider the following excerpt from a driver class. 

.. code-block:: shadow
    :linenos: 

    Silver silver = Silver:create(10283.60); 
    Gold gold = Gold:create(230953.34); 

    Chest<Silver> chest1 = Chest<Silver>:create(silver); 
    Chest<Gold> chest2 = Chest<Gold>:create(gold); 

First, in **Lines 1 and 2**, we have created 2 different objects, ``gold`` and ``silver``. They both are children of the ``Treasure`` class. 

Similarly, in **Lines 4 and 5**, we see 2 different instances of the generic ``class`` ``Chest``: ``chest1`` and ``chest2``. The key thing to notice here is the **angle brackets**. In the ``Chest`` ``class`` itself, ``T`` appeared between the angle brackets. Now, when creating an object of the ``Chest`` class, we replace the type variable with a specific ``class`` or ``interface``. In this case, ``chest1`` holds a ``Gold`` object, and ``chest2`` holds a ``Silver`` object. 

However, ``Chest`` objects are not limited to storing  ``Treasure`` objects and its children. We could also just as easily replaced ``T`` with ``int`` or ``String`` or ``Object``. For example, this code is perfectly legal and would compile: 

.. code-block:: shadow

    Chest<int> numChest = Chest<int>:create(6); 
    Console.printLine(numChest.getObject()); 

Now, when we call ``numChest.getObject()``, 6 is printed to the console. This is the beauty of generics. We were able to create 3 instances of the ``Chest`` class, each acting as a "container" for a different type, while reusing the same code. 

Although the implementation is not shown, you are also able and encouraged to create generic interfaces. The ``interface`` header would appear as follows: ``interface someInterface<T>``. 

Bounds
^^^^^^^ 

Another feature of generics in Shadow is the ability to create **bounds**. In basic terms, using bounds with generics allows you specify constraints for acceptable types, ``T``. For example, in our ``Chest`` class above, let’s say we only wanted ``Chest`` to be able to "hold" instances of the ``Treasure`` class and any of its children. All we would need to do is modify the class header slightly: ``class tutorials:generics@Chest<T is Treasure>``. Now, if we tried to create ``numChest`` from the previous section, we would get a compile error because ``int`` is not a child of ``Treasure``. This is called an **upper bound**. 

Since ``T is Treasure``, we could also add the following method to ``Chest`` in order to access the member variable ``value`` of ``Treasure`` objects (and objects of its subclasses). 

.. code-block:: shadow
    :linenos: 

    public getValue() => (double)
    {
        return object->value; 
    }

However, in order for this to work, ``value`` in the ``Treasure`` class must be marked with ``get``. 



Additionally, Shadow also allows you to have **more than one** bound. For example, we could also state ``class tutorials:generics@Chest<T is Treasure and String>``. Lastly, if you also included interfaces as bounds, the only caveat is that the class (or classes) should be listed first.

Generic Arrays
^^^^^^^^^^^^^^

Although you should already be familiar with declaring and initializing arrays, it is also useful to note that the ``Array`` class is actually a generic class. Thus, you are able to create generic arrays. Consider the example below: 

.. code-block:: shadow
    :linenos:

    int[] array1 = int:create[10]; 
    for(int i = 0; i < array1->size; i += 1)
    {
        array1[i] = 7 + (2 * i); 
    }
		
    Array<int> array2 = array1; 
		
    int[] array3 = cast<int[]>(array2); 
				

In  **Lines 1-5** we have declared and initialized an ``int`` array and filled it using a ``for`` loop. If this does not look familiar to you, please revisit the previous tutorial on :ref:`arrays<Arrays>`. 

Now look at **Line 7**. Here, we created another array, ``array2``. The difference between the two ways of declaring an array is the static type, which for ``array2`` explicitly references the generic class ``Array``. However, we are still able to assign ``array1`` to ``array2`` because they both are instances of the ``Array`` class. In a similar vein, we are subsequently able to cast ``array2`` to a non-generic array, as seen in **Line 9**. 


``CanEqual`` and Operator Overloading
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a final discussion on generics, we will discuss the ``CanEqual`` interface and Operator Overloading in Shadow. Before we dive in, it is first important to be aware of the different **generic** interfaces included in the standard library of the `Shadow API <http://shadow-language.org/documentation/shadow/standard/$package-summary.html>`_. They are listed under the "Interface Summary" section of this page. 

You will notice that not all of the interfaces use the type parameter ``T``. Although ``T`` is used to represent ``Type``, there are other conventional type parameter names, and they are listed below. 

* ``K`` , Key
* ``V``, Value
* ``E``, Element

The first generic interface we will study is ``CanEqual``. If a class implements ``CanEqual``,  it means that the class can test an object of type ``T`` for equality, returning ``true`` if the two objects are identical. The interface also allows the ``==`` operator to be overloaded. The method ``equal(T)`` of ``CanEqual`` will be called when this operator is used. In order to properly implement the ``CanEqual`` interface, ``equal(T)`` must be implemented properly. 

Take a look at the class ``Surprise``, driver program excerpt, and console output below. For now, just focus on the implementation of ``CanEqual``.

``Surprise`` class: 

.. code-block:: shadow
    :linenos:

    class tutorials:generics@Surprise is CanEqual<Surprise> and CanAdd<Surprise>
    {
        get String word; 
	get int magicNumber; 
	
	public create(String w, int m)
	{
	    word = w; 
	    magicNumber = m;  
	}
	
	public equal(Surprise other) => (boolean)
	{
	    return word == other:word and magicNumber == other:magicNumber; 
	}
	
	public add(Surprise other) => (Surprise)
        {
            return Surprise:create(word # " " # other:word, magicNumber + other:magicNumber); 
        }
    
        public readonly toString() => (String) 
        {
    	    return # word # ", " # magicNumber; 
        }
    }
	
Driver program excerpt: 

.. code-block:: shadow
    :linenos:

    Surprise birthday = Surprise:create("diamond", 57); 
    Surprise party = Surprise:create("watch", 103); 
		
    Console.printLine(birthday.equal(party)); 
    Console.printLine(birthday == party); 
    Console.printLine(birthday + party); 
	
	
Console output: 

.. code-block:: console

    false
    false
    diamond watch, 160
	
``CanEqual`` **Interface**

As you can see in **Line 1**, we have included ``is CanEqual<Surprise>`` in the class header. It is important that we specify the type inside the angle brackets (ie. we could not have left it as ``T``). Now, look at **Lines 12-15**. Here, we have provided the implementation for the ``equal()`` method of ``CanEqual``. Pay close attention to method header. It *must* exactly follow this syntax in order to properly implement the method: ``public equal (T other) => (boolean)``. In this example, we have simply replaced ``T`` with ``Surprise``. The method will only return ``true`` if the member variables of the current object and the object being passed in as a parameter are equal to the same values. However, it is **up to the programmer** to define the conditions for when two objects of the same class are considered equal. For example, we could have only required the ``String`` member variable ``word`` to be the same for ``equal()`` to return ``true``. 

The excerpt from the driver program demonstrates how ``equal()`` is used. As seen in **Lines 1 and 2**, we have created two instances of the ``Surprise`` class that are not the same. Thus, it should not be shocking that the result of **4 and 5** are both ``false``. These two different ways of calling the ``equal()`` method are equivalent. However, if ``Surprise`` did not implement the ``CanEqual`` interface and you tried to use ``==`` on the same two objects, the code would not compile. 

Lastly,  for overloading arithmetic operators, the interfaces ``CanAdd<T>``, ``CanSubtract<T>``, ``CanMultiply<T>``, ``CanDivide<T>``, and ``CanModulus<T>`` can be implemented to allow overloading of the ``+``, ``-``, ``*``, ``/``, and ``%`` operators, respectively.  Our example shows how to overload the ``+`` through implementing ``CanAdd``. 

``CanAdd`` **Interface**

Look back at the ``Surprise`` class. **Lines 17-20** show how we implemented the ``add()`` method of the ``CanAdd`` interface. The method header must follow this syntax **exactly** for the code to compile: ``public add(T other) => (T)``. Once again, we have simply substituted ``Surprise`` for ``T``. 

Inside the method, it is **up to the programmer** to decide how two objects of a class are added together. In this example, we have somewhat arbitrarily decided to combine the object’s ``word`` variable with a space and add their magic numbers together and use the results as parameters for a new ``Surprise`` object. 

Lastly, focus now on the driver program excerpt.  As you can see in **Line 6**, using the ``+`` operator, we have added the objects ``birthday`` and ``party`` together and printed the resulting object (see the ``toString()`` method in the ``Surprise`` class). The ``+`` operator invokes the ``add()`` method of ``Surprise``. However, we also could have written ``birthday.add(party);``, but the whole purpose of implementing the ``CanAdd`` interface is to overload the ``+``. 

At this point in the tutorials, you are encouraged to look through the rest of the interfaces in the Shadow standard library and practice implementing them. This section should serve as a guide on how to do so. 














  












