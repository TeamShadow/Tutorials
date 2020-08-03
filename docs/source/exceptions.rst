Exceptions
----------

Although we are officially covering **exceptions** now, you have most likely come across exceptions in earlier tutorials. In basic terms, an **exception** is like an official error message, an indication that something has gone wrong in a program. In other words, you have violated some Shadow "rule" or principle, and an exception is subsequently thrown.  

Common Exceptions 
^^^^^^^^^^^^^^^^^

Consider the following instance of an exception being thrown: 

.. code-block:: shadow 

    String[] nonsense = {"Chicken", "Pot", "Pie", "Yum"}; 
    Console.printLine(nonsense[4]); 
    Console.printLine("Continue?"); 

The console displays, in red text, 

.. code-block:: console

    shadow:standard@IndexOutOfBoundsException: Index 4

This console output is an example of an ``IndexOutOfBoundsException``, which belongs to the Shadow ``standard`` package (information before the ``@``).  An ``IndexOutOfBoundsException`` is thrown if you try to access a position in an array, ``String``, ``LinkedList``, or ``ArrayList`` that  does not exist. In this case, our ``String`` array, ``nonsense``, only has indices 0-3, so trying to print the value at index 4 results in this specific exception. We are referencing a position that is "out of bounds" of the array, and the exception message actually displays this index number. Once the exception is thrown, the program terminates, so "Continue?" will not be printed to the console. 

Although this exception is thrown automatically at run time, we are also able to explicitly throw exceptions ourselves. The syntax is as follows: 

``throw IndexOutOfBoundsException:create();`` 

This statement would produce the same output as the example above, excluding the ``Index 4``. 

Overall, an ``IndexOutOfBoundsException`` is just one exception in the Shadow ``standard`` package. Other exceptions and brief explanations from the `Shadow API <http://shadow-language.org/documentation/shadow/standard/$package-summary.html>`_ are below. 

* ``CastException`` (trying to cast one type to an incompatible type)
* ``Exception`` (parent type of all exceptions) 
* ``IllegalArgumentException`` (an argument with an illegal type or value is supplied to a method)
* ``InterfaceCreateException`` (trying to create an ``interface`` at run time) 
* ``NumberFormatException`` (parsing a ``String`` or other representation of a number and illegal characters are encountered)
* ``UnexpectedNullException`` (a ``nullable`` value is checked, found to be ``null``, and is not within a ``try`` block with a matching ``recover`` block) 

Writing and Catching Exceptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Writing Exceptions** 

While we have covered "built-in" exceptions in Shadow, you are also able to create your own exceptions using the ``exception`` keyword. In order to understand **writing** and **catching** exceptions, consider the extended example outlined below: 

In the midst of a global pandemic, you realize that you have a lot of free time on your hands. Naturally, you decide to fill this time by learning how to cook. Although you have mastered mac ‘n cheese and toast, you are ready to move on to some more "advanced" recipes. Just in case, you decide to outline some things that could go wrong in the kitchen by defining 3 different **exceptions**. 

The first exception is called ``BurnedFoodException``: 

.. code-block:: shadow 
    :linenos: 

    exception tutorials:except@BurnedFoodException
    {
        public create()
        {
            super("Oh no! You have burned the food!");
        }
    }

The second is ``MeasuringMistakeException``: 

.. code-block:: shadow 
    :linenos: 

    exception tutorials:except@MeasuringMistakeException
    {
        public create()
        {
            super("Brush up on your fractions! You measured wrong!"); 
        }
    }

The last is ``OutOfIngredientsException``: 


.. code-block:: shadow 
    :linenos: 
    
    exception tutorials:except@OutOfIngredientsException
    {
        public create()
        {
            super("Whoops! You ran out of ingredients!"); 
        }
    }


Upon examining these 3 different ``Exception`` classes, there are a few key things to take away. For one, instead of the keyword ``class``, they are all created with the following syntax: ``exception ClassName``. 

In addition, each has a single constructor that calls the parent class’ constructor via ``super()``. As for all exceptions, the parent class is called ``Exception``. ``Exception`` has 2 constructors, one that takes no parameters (creating an exception without a message) and one that takes a ``String`` representing an explanation for the exception. In all 3 examples, we have invoked the parent constructor that takes in a ``String``. These ``String`` values are the messages displayed when the specific exception is thrown. For instance, if in a driver class we stated, ``throw MeasuringMistakeException:create();``, the console output would have been ``except@MeasuringMistakeException: Brush up on your fractions! You measured wrong!``

Now that we have established **how** to create our own exceptions, it is time to move on to **catching exceptions**. 

**Catching Exceptions**

Although knowing how to create and throw exceptions is important, it is even more useful to know how to **catch** them. As you have seen from the previous examples, when an exception is thrown, the program stops running at that point. **Catching** an exception circumvents this issue by identifying and "handling" the exception that may or may not result when a given action is taken. 

Let’s revisit our cooking example by looking at the driver program, ``ExceptionTest`` below. 

.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;
    import shadow:utility@Random; 

    class tutorials:except@ExceptionTest   
    {
        public main( String[] args ) => ()
        {
            try
            {
                Random random = Random:create();
	        var number = random.nextInt(4); 
			
		switch (number)
		{
		    case(0)  
		    { 
		        Console.printLine("No cooking errors!"); 
		    }
		    case(1)
	            {
		        burnFood(); 
		    }
		    case(2)
		    {
		        runOut(); 
		    }
		    case(3) 
		    {
		         measureMistake(); 
		    }
	         }
            } 
	    catch (BurnedFoodException ex) 
	    {
	        Console.printLine("Warning: Turn down the heat on the stove!"); 
	    }
	    catch (OutOfIngredientsException ex)
	    {
	        Console.printLine("Warning: Make a trip to the grocery store!"); 
	    }
	    catch (MeasuringMistakeException ex)
	    {
	        Console.printLine("Warning: Double check your math"); 
	    }
        }         
	
        public burnFood() => ()
	{
	    throw BurnedFoodException:create(); 
	}
	
	public runOut() => ()
	{
	    throw OutOfIngredientsException:create(); 
	}
	
	public measureMistake() => ()
	{
	    throw MeasuringMistakeException:create(); 
	}
    } 

First, ignore the ``main()`` method and look at **Lines 47-61**. Here we see 3 methods: ``burnFood()``, ``runOut()``, and ``measureMistake()``. These methods represent 3 different actions you could take to ruin your cooking, so it makes sense that each of these methods throws a corresponding exception (defined above). If you simply called ``burnFood()`` in the ``main()`` method, you would get an exception with the message "Oh no! You have burned the food!", and the program would terminate. This is not very useful, especially if you want the program to keep running.

Wouldn’t it be better if you got a warning that you were about to burn your food or run out of ingredients? This is where the **try-catch** block comes in. The syntax is as follows: 

.. code-block:: shadow

    try
    {
        //some action
    }
    catch (Exception ex)
    {
        //action to take
    }

    .
    .
    .

Before we discuss the ``try`` block in the example, it is important to touch on the new import statement ``import shadow:utility@Random;``, you probably noticed in ``ExceptionTest``. This imports the ``Random`` class from the Shadow utility package, which allows the generation of pseudorandom numbers using the Mersenne Twister algorithm. Look at **Lines 10 and 11**. Here, inside the ``try`` block, we have created a ``Random`` object. Then, we call the ``nextInt()`` method on it, which returns an ``int`` between zero and the parameter passed in (excluding this value). Thus, ``number`` will hold an integer between 0 and 3. 

.. note:: To learn more about the different methods in ``Random``, visit this page on the `Shadow API <http://shadow-language.org/documentation/shadow/utility/Random.html>`_. 

Now, based on the number stored in ``number``, a method will be called that could produce a certain exception. This is done through a ``switch`` :ref:`statement<switch>`. However, ``case(0)`` indicates it is possible for no cooking mistake to be made. There is a ¼ chance that this will happen.

For the sake of the example, let’s say that ``number`` holds the value 2. Look at **Line 23** of ``ExceptionTest``. For this case, we are calling the method ``runOut()``, which throws an ``OutOfIngredientsException``. Once this exception is thrown, we say that it is **in flight**. In other words, the program goes back to the try-catch block and runs through each ``catch`` statement (from top to bottom) until it finds an exception of compatible type. 



In this example, the first ``catch`` block has the type ``BurnedFoodException``, so then the second ``catch`` block is checked. It is of type ``OutOfIngredients``, which matches the type of exception thrown by ``runOut()``. Subsequently, the program enters this ``catch`` block and executes all statements inside of it. Thus, "Warning: Make a trip to the grocery store!" is printed to the console. Then, the try-catch block is exited completely and any statements after the ``runOut()`` method call will **not** execute. Control then flows to the first statement outside of the try-catch block. 

Overall, by using a try-catch block, we were able to handle the ``OutOfIngredients`` exception ourselves, as opposed to letting the exception simply be thrown by the program. That is, instead of "running out of ingredients" (i.e. getting the exception error message), you got a "warning" instead. 


More on Catching Exceptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although we have covered the basics of creating a try-catch block in the previous example, there are some important nuances and rules that are outlined below. 

* There is no limit to how many ``catch`` blocks you can have 
* If you do include **multiple** ``catch`` **blocks**, the **most specific** exceptions should be put first, getting more general/broad at the end. For example, let’s say we added the ``catch`` statement -- ``catch (Exception ex)`` -- as the first ``catch`` after the ``try`` block. Since all exceptions are children of ``Exception``, any exception that could be thrown would match with this first ``catch`` block. Thus, none of the other ``catch`` blocks could ever be reached, **leading to a compile error** ( ``Unreachable code:`` ). 
* If an exception is thrown from a ``try`` block and is never caught, the program simply terminates and the exception is displayed on the console. 
* There are no restrictions on the number or type statements we can put inside the ``try`` block. We can call methods, create variables, create objects, etc. 


The ``finally`` Block
^^^^^^^^^^^^^^^^^^^^^

In addition to ``catch`` blocks, another feature of exceptions is the ``finally`` block.  A ``finally`` block is code that is **guaranteed to run** before you exit the try-catch.  Although it is legal to have multiple ``catch`` blocks, you may only have **1** ``finally`` block for every ``try`` block. It also must be the **very last** block in a try-catch, or your code will not compile. 

For example, let’s say we added the following ``finally`` block at the end of our cooking example: 


.. code-block:: shadow 
    :linenos: 

    finally 
    {
        Console.printLine("Bon Appetit!"); 
    }

Now, after "Warning: Make a trip to the grocery store!" is printed, the next line will display "Bon Appetit!" Even if the only statement in the ``try`` block had been ``return;``, the ``finally`` block **would still execute** before exiting the try-catch.

In addition, ``catch`` blocks are technically not even required following a ``try`` block. As long as there is at least one ``catch``, ``finally``, ``recover`` (covered next), or any combination of the 3, the code will compile. So, what would happen if we got rid of all the ``catch`` blocks in our cooking example above, and only included the ``finally`` block? What would be the console output? 


.. code-block:: console
    Bon Appetit!
    default@OutOfIngredientsException: Whoops! You ran out of ingredients!

As you can see, the ``OutOfIngredientsException`` is thrown because there is no longer a matching ``catch`` block to handle it. However, it is important to note that **before the exception is thrown**, the ``finally`` block still executes. This is always the case. 

When implementing a ``finally`` block, it is important to keep these nuances in mind. Although they should not be overused, ``finally`` blocks prove to be very useful when you are trying to guarantee some behavior before the end of a try-catch. 

The ``recover`` Block 
^^^^^^^^^^^^^^^^^^^^^^ 


This brief section will analyze the ``recover`` block, which is used to handle an ``UnexpectedNullException``. In the example below, the ``check()`` method call causes this type of exception to be thrown and subsequently caught by the ``recover`` block. In case you need a refresher on how ``check()`` works, it can be found in an :ref:`earlier tutorial<nullable-check>`.  

.. code-block:: shadow 
    :linenos: 

    nullable Object keys = null; 

    try
    {
        Object object = check(keys); 
        Console.printLine("This will never be printed"); 
    }
    recover
    {
        Console.printLine("Found it!"); 
    }

As you can see in **Line 1**, we have a ``nullable`` ``Object`` named ``keys``, and it stores the value ``null``. This will not cause an exception on its own, as we declared the type to be ``nullable``. However, in the ``try`` block, notice how we use ``check()`` on ``keys``. This will cause an ``UnexpectedNullException`` because it is not possible to return a non-``nullable`` version of ``null``. Thus, the ``recover`` block catches and  handles this exception by printing "Found it!" to the console. 

Unwinding
^^^^^^^^^

In order to understand how an an exception **unwinds** once it is **in flight**, consider the following more complicated example. Although they are not shown, assume ``ExceptionA`` and ``ExceptionB`` were defined correctly and exist. Read through the code first, and then we will break it down line-by-line. 


.. code-block:: shadow 
    :linenos: 

    immutable class tutorials:except@ExceptionAdvancedTest
    {
        public test() => () 
        {		
	    throw ExceptionB:create();
	}
	public test1() => () 
        {
	    try 
            {			
	        test();						
	    } 
            catch (ExceptionA ex)
            {
	        Console.printLine("test1 caught ExceptionA");
            }		
	}

	public test2() => () 
        {
	    try 
            {
	        test1();
            }
            catch (ExceptionA ex)
            {
	        Console.printLine("test2 caught ExceptionA");
	    } 
            catch (ExceptionB ex) 
            {
	        Console.printLine("test2 caught ExceptionB");
	    }
	}

	public test3() => () 
        {
	    try 
            {
	        test2();
	    } 
            catch (Exception ex) 
            {
	        Console.printLine("test3 caught Exception");
	    }
	}

	public main( String[] args ) => () 
        {
	    test3();
	}
    }


Let’s start at **Line 49** in the ``main()`` method. Here we see a method call, ``test3();`` Control flows to this method and inside the ``try`` block (**Line 39**), we see another method call to ``test2()``. Once we enter ``test2()``, we see yet another method call in a ``try`` block (**Line 23**). This time, the method call is to ``test1()``. Inside ``test1()`` , there is a call to ``test()`` within the ``try`` block (**Line 11**).

Now, control has shifted to ``test()``, and at **Line 5** we see that an exception, ``ExceptionB``, is explicitly thrown. At this point, we say that the exception is **in flight** and begins the unwinding process. In other words, starting with the try-catch block in ``test1()``, the exception will propagate downwards through the methods that were called until the exception is caught by one of the ``catch`` blocks (from the top of the stack). If control is passed back to the ``main()`` method and the exception has not been caught (still in flight), then the program will terminate with the exception message printed to the console. 

However, this is not the case in our example. First, we go back to ``test1()``. In this method, only an exception of type ``ExceptionA`` can be caught. Thus, the exception keeps unwinding to ``test2()``. Here, the first ``catch`` handles only ``ExceptionA``, but the second ``catch`` handles an  ``ExceptionB`` -- a match! Now, "test2 caught ExceptionB" is printed to the console, and control flows back to the ``main()`` method. The exception is no longer in flight; it has unwound and been handled. 

``toString()`` and ``message``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will conclude the tutorial on exceptions with a brief note on the ``toString()`` method and ``message`` property of the ``Exception`` class. 

Consider the following ``BurnedFoodException`` object (see above for the full class): 

.. code-block:: shadow 
    :linenos: 

    BurnedFoodException burn = BurnedFoodException:create(); 
    Console.printLine(burn.toString()); 
    Console.printLine(burn->message); 

As seen in **Line 1**, we create an ``BurnedFoodException`` object just as we would create an object of any other ``class``. Thus, we are also able to call the ``toString()`` method on an ``Exception`` object. What will be printed to the console? ``except@BurnedFoodException: Oh no! You have burned the food!`` Notice how ``toString()`` returns the same message that is printed when an exception is thrown. 

Additionally, all ``Exception`` objects have a ``message`` property. When invoked, this property returns just the message (or lack of message) of the exception. Thus, only "Oh no! You have burned the food!" will be printed. 















    

