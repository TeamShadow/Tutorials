**********
Exceptions
**********

Although we are officially covering *exceptions* now, you have most likely encountered exceptions while working through earlier tutorials. An exception is an object associated with an unusual situation, usually an error.  This object is *thrown* by the code that caused the error, and it can be *caught* by other code that knows how to deal with the error.  If no code catches the exception, execution will crash with a message printed on the console.

Common exceptions 
=================

Most of the time, you won't be creating your own exceptions.  Instead, you'll be writing code that interacts with exceptions thrown by library code or the Shadow run-time environment itself.  Some of these exceptions aren't expected to be caught.  Instead, they indicate that there's a bug in your code.

Consider the following code that throws an exception: 

.. code-block:: shadow 

    String[] nonsense = {"Chicken", "Pot", "Pie", "Yum"}; 
    Console.printLine(nonsense[4]); 
    Console.printLine("Continue?"); 

If the exception thrown by this code is uncaught, the console will print:, 

.. code-block:: console

    shadow:standard@IndexOutOfBoundsException: Index 4

This console output is an example of an ``IndexOutOfBoundsException``, which belongs to the Shadow ``standard`` package.  An ``IndexOutOfBoundsException`` is thrown if you try to access a position that  does not exist in an array, ``String``, ``LinkedList``, ``ArrayList``, or other ``List``. In this case, our ``String`` array ``nonsense`` has indices 0-3, so trying to print the value at index 4 results in this exception. We are referencing a position that is out of bounds of the array, and the exception message displays this illegal index number. Once the exception is thrown, the program terminates, so ``Continue?`` will *not* be printed to the console. 

Although this exception is thrown automatically at run time, we could explicitly throw exceptions ourselves. The typical syntax for throwing an exception is:

.. code-block:: shadow
	
	throw ExceptionName:create();
	
Exceptions can be created like any other object, but there's usually no reason to keep them lying around until they need to be thrown.  That's why it's common to use the syntax above that creates the exception and throws it at the same time.

Like other classes, some exceptions have a constructor that takes parameters.  For example, to get exactly the same output as our initial example, we could create an ``IndexOutOfBoundsException`` with parameter ``4``:

.. code-block:: shadow
	
	throw IndexOutOfBoundsException:create(4);

This statement would produce the same output as the first example in which we tried to access an illegal index in an array of ``String`` values.  In that situation, the Shadow run-time environment itself called the constructor with the appropriate index and threw the ``IndexOutOfBoundsException``. 

Of course, ``IndexOutOfBoundsException`` is just one of several fundamental exceptions provided by the Shadow ``standard`` package. Other exceptions and brief explanations from the `Shadow API <http://shadow-language.org/documentation/shadow/standard/$package-summary.html>`__ are below: 

* ``CastException``: Thrown when casting to an incompatible type
* ``Exception``:  Parent class of all exceptions
* ``IllegalArgumentException``: Thrown when an argument with an illegal type or value is supplied to a method
* ``InterfaceCreateException``: Thrown when trying to instantiate an interface at run time
* ``NumberFormatException``: Thrown when parsing a ``String`` or other representation of a number that is incorrectly formatted
* ``UnexpectedNullException``: Thrown when a ``nullable`` value is checked, found to be ``null``, and has no matching ``recover`` block 

Custom exceptions
=================

When creating your own code, especially library code, you may need to write your own exceptions.  These exceptions are usually short and very much like normal classes, with constructors, methods, and member variables.  Although the standard exceptions provided by Shadow will seldom be caught, these custom exceptions usually *will* be.  They are created so the the programmer can write code that reacts to error cases that are likely to crop up.

Writing exceptions
------------------

Writing your own exception is almost the same as writing any other class except that you use the ``exception`` keyword instead of the ``class`` keyword.

Let's start an extended example using custom exceptions by writing some exceptions of our own. In the midst of a global pandemic, you realize that you have a lot of free time on your hands. Naturally, you decide to fill this time by learning how to cook. Although you've mastered mac 'n' cheese and toast, you're ready to move on to more advanced recipes. Just in case, you decide to outline some things that could go wrong in the kitchen by defining three different exceptions. 

The first exception is called ``BurnedFoodException``: 

.. code-block:: shadow

    exception tutorials:exceptions@BurnedFoodException
    {
        public create()
        {
            super("Oh no! You burned the food!");
        }
    }

The second is ``MeasuringMistakeException``: 

.. code-block:: shadow

    exception tutorials:exceptions@MeasuringMistakeException
    {
        public create()
        {
            super("Brush up on your fractions! You measured wrong!"); 
        }
    }

The last is ``OutOfIngredientsException``: 

.. code-block:: shadow

	exception tutorials:exceptions@OutOfIngredientsException
    {
        public create()
        {
            super("Whoops! You ran out of ingredients!"); 
        }
    }


Note that each of these exceptions has a single constructor that calls the parent class's constructor via ``super``. If no other parent is specified, the parent of an exception is the ``Exception`` class.  ``Exception`` has two constructors, one that takes no parameters (creating an exception without a message) and one that takes a ``String`` representing a human-readable explanation for the exception.  For the three exception classes above, we have invoked the parent constructor that takes a ``String``.

These messages are displayed if the exception crashes the program. For instance, if in a ``MeasuringMistakeException`` is thrown and never caught, the console output for the crashed program would be:

.. code-block:: console

	tutorials:exceptions@MeasuringMistakeException: Brush up on your fractions! You measured wrong!

Now that we have established how to create our own exceptions, it's time to move on to catching exceptions. 

Catching exceptions
-------------------

When an exception is thrown, the program's normal execution stops.  The execution begins to return from the methods that are currently executing, looking for code that can handle the current exception. *Catching* an exception handles the exception and allows the program to return to normal execution.

Let's revisit our cooking example by looking at the driver program ``ExceptionTest`` below. 

.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;
    import shadow:utility@Random; 

    class tutorials:exceptions@ExceptionTest   
    {
        public main( String[] args ) => ()
        {
			boolean success = false;
			Random random = Random:create();
			
			while(!success)
			{
				try
				{					
					var number = random.nextInt(4);				
					switch (number)
					{
						case(0) 
						{
							Console.printLine("No cooking errors!");
							success = true;
						}
						case(1)
							throw BurnedFoodException:create(); 
						case(2)
							throw OutOfIngredientsException:create(); 
						case(3)
							throw MeasuringMistakeException:create(); 
					}
				} 
				catch (BurnedFoodException e) 
				{
					Console.printLine("Warning: Turn down the heat on the stove!"); 
				}
				catch (OutOfIngredientsException e)
				{
					Console.printLine("Warning: Make a trip to the grocery store!"); 
				}
				catch (MeasuringMistakeException e)
				{
					Console.printLine("Warning: Double check your math"); 
				}
			}
			
			Console.printLine("Dinner is served!");
        }
    }
	
Before we discuss the ``try`` block in the example, note that we import ``shadow:utility@Random``.  This class allows the generation of pseudorandom numbers using the Mersenne Twister algorithm. We create a ``Random`` object on **Line 9** and use its ``nextInt()`` method on **Line 15** to generate a random ``int`` between zero and the parameter passed in (excluding this value). Thus, ``number`` will hold an integer between 0 and 3.

.. note:: To learn more about the different methods in ``Random``, visit its `documentation page <http://shadow-language.org/documentation/shadow/utility/Random.html>`_. 

Now, based on the value stored in ``number``, various outcomes can happen, selected with a ``switch`` statement.  If ``number`` was ``0``, everything went fine with our cooking, and setting ``success`` to ``true`` will cause the loop to end.  Unfortunately, an exception will be thrown in the other three cases. If nothing caught these exceptions, an error message would be printed to the console, and the program would crash. This would not be useful, especially if we wanted the program to keep running until we successfully cooked dinner.

Wouldn't it be better if we got a warning that we were about to burn our food or run out of ingredients? This is where we can use ``try-catch`` blocks. The syntax is as follows: 

.. code-block:: shadow

    try
    {
        // Some dangerous code
    }
    catch (MatchingException e)
    {
        // Action to resolve the error
    }

For the sake of the example, let's say that ``number`` holds the value 2. Look at **Line 26** of ``ExceptionTest`` which throws an ``OutOfIngredientsException``. Once this exception is thrown, we say that it is *in flight*. In other words, the program starts running through  ``catch`` statements following the ``try`` block, from first to last, until it finds an exception of compatible type. 

In this example, the first ``catch`` block has the type ``BurnedFoodException``.  Since that type doesn't match ``OutOfIngredientsException``, the second ``catch`` block will be checked. Since the second ``catch`` *does* match, the program will enter this ``catch`` block and execute the statements inside, printing ``Warning: Make a trip to the grocery store!`` Afterwards, control flows to the first statement after the ``catch`` blocks.  In our example, execution will jump back up to the top of the ``while`` loop. Thus, the entire ``try`` will run again until dinner is cooked without an error.

By using a ``try-catch`` block, we were able to handle the exceptions instead of letting them crash the program.


Exception catching details
--------------------------

Although we have covered the basics of creating a ``try-catch`` block, there are some important nuances and rules outlined below:

* There is no limit to how many ``catch`` blocks you can have.
* There are no restrictions on the number or type of statements we can put inside the ``try`` block. We can call methods, declare variables, instantiate objects, run loops, and even nest more ``try-catch`` blocks inside.
* If you include multiple ``catch`` blocks, the *most specific* exceptions should be put first, getting more general as they go. For example, let's say we added the ``catch`` statement -- ``catch (Exception e)`` -- as the first ``catch`` after the ``try`` block. Since all exceptions are children of ``Exception``, any exception that could be thrown would match with this first ``catch`` block. Thus, none of the other ``catch`` blocks could ever be reached, leading to unreachable code and a compiler error. 
* If none of the ``catch`` blocks have a matching exception type, the in-flight exception will look for an outer ``try`` with matching ``catch`` statements.  If there are no more outer ``try`` blocks, the exception will leave the method and continue the process, unwinding to the previous method call and the one before that.
* If an exception is thrown and never caught, the program crashes, displaying the exception on the console.

It's common to call the variable in the header of the ``catch`` block ``e`` or ``ex``, but it can have any legal variable name.  Usually, this variable isn't important because the real value of the exception is knowing which ``catch`` block matches.  However, some exceptions carry important information about the errors that caused them.  In these situations, it can be useful to access the variable, which points to the exception that was thrown.  It's also possible to re-throw this exception variable to propagate the error out to another handler. 

Exception messages
------------------

Since all exceptions inherit from the ``Exception`` class, all exceptions have a ``message`` property that provides a ``String`` with more information about the exception and the error that caused it.

Consider the following code that creates a ``BurnedFoodException`` exception, defined above: 

.. code-block:: shadow 
    :linenos: 

    BurnedFoodException burn = BurnedFoodException:create(); 
    Console.printLine(burn->message);
	Console.printLine(burn.toString()); 
     

On **Line 1** we create a ``BurnedFoodException`` object. On **Line 2** we print out this object's ``message`` property, which outputs ``Oh no! You burned the food!`` to the console.  The ``BurnedFoodException`` always has this message, but some exceptions have more specifics about the cause of the error.  Recall that the message of the ``IndexOutOfBoundsException`` will say which illegal index the code was attempting to access.

Like all objects, exceptions have a ``toString()`` method.  Although it can be be overridden, the default implementation of the ``toString()`` method produces the full name of the exception's type followed by a colon and the message stored in its ``message`` property.  Thus, the output for **Line 3** will be: 

.. code-block:: console 

	tutorials:exceptions@BurnedFoodException: Oh no! You burned the food!

The ``recover`` block 
=====================

We briefly mentioned ``nullable`` variables in an :ref:`earler tutorial <\`\`nullable\`\` and \`\`check\`\`>`.  Recall that a programmer must use the ``check`` keyword to convert a ``nullable`` reference into a regular reference or to call methods on it.  However, if the ``nullable`` reference contains ``null``, there will be an error.  If the ``check`` occurs outside of a ``try`` block, an ``UnexpectedNullException`` will be thrown.  However, there's an alternative designed to make handling ``nullable`` variables simpler.

If the ``check`` occurs inside of a ``try`` block with a matching ``recover`` block, execution will flow to the ``recover`` block. In the example below, the ``check`` command is used in this way.

.. code-block:: shadow 
    :linenos: 

    nullable Object keys = null; 

    try
    {
        Object object = check(keys); 
        Console.printLine("Found our keys!"); // Never printed 
    }
    recover
    {
        Console.printLine("Our keys are lost!"); 
    }

As you can see in **Line 1**, we store ``null`` into a variable named ``keys``. This assignment is legal because ``keys`` is declared ``nullable``. However, in the ``try`` block, we use the ``check`` command on ``keys``. Unfortunately, ``keys`` is ``null``, so this ``check`` fails.  Without a matching ``recover`` block, an ``UnexpectedNullException`` would be thrown.  In this cause, however, controls flows to the ``recover`` block which prints ``Our keys are lost!`` to the console.

While this syntax is similar to catching an ``UnexpectedNullException``, it's much more efficient.  Throwing and catching exceptions has significant computational overhead.

.. note:: A ``recover`` block must appear after all ``catch`` blocks, if there are any.  There can only be a single ``recover`` block.

The ``finally`` block
=====================

In addition to ``catch`` blocks, another feature of exception handling is the ``finally`` block.  A ``finally`` block is code that is *guaranteed* to run before you exit a ``try-catch``.  Although it's legal to have multiple ``catch`` blocks, you may only have one ``finally`` block for every ``try`` block.

.. note:: A ``finally`` block must appear after all ``catch`` and ``recover`` blocks, if there are any.  There can only be a single ``finally`` block.

For example, let's say we added the following ``finally`` block at the end of our cooking example: 


.. code-block:: shadow 
    :linenos: 

    finally 
    {
        Console.printLine("Cooking is tough!"); 
    }

Now, after catching the ``OutOfIngredientsException`` and printing ``Warning: Make a trip to the grocery store!``, the program will print ``Cooking is tough!`` This message will also be printed even if there are no exceptions. Even if the only statement in the ``try`` block is ``return;``, the ``finally`` block would *still* execute before exiting the ``try-catch``.

In addition, ``catch`` blocks are not required following a ``try`` block. As long as there is at least one ``catch``, ``recover``, ``finally``, or any combination of the three, the code will compile. So, what would happen if we got rid of all the ``catch`` blocks in our cooking example above, and only included the ``finally`` block? What would be the console output? 


.. code-block:: console

    Cooking is tough!
    tutorials:exceptions@OutOfIngredientsException: Whoops! You ran out of ingredients!

As you can see, there is no longer a matching ``catch`` block to handle the ``OutOfIngredientsException``. Note that the ``finally`` block still executes *before* the exception crashes the program.

Only use ``finally`` blocks when necessary, since they have some overhead.  They are most useful when you want to guarantee that a file or other resource is closed or cleaned up before moving on, even if an exception is thrown.

.. warning:: You cannot put a ``break``, ``continue``, or ``check`` inside of a ``finally`` block if it would cause execution to leave the ``finally`` block.  Likewise, you cannot put a ``return`` statement inside of a ``finally`` block.  Fortunately, there is always a more reasonable place to put any of these constructs.

Unwinding
=========

In order to understand how an an exception *unwinds* once it has been thrown, consider the following more complicated example. Although they are not shown, assume ``ExceptionA`` and ``ExceptionB`` are correctly defined exceptions.


.. code-block:: shadow 
    :linenos: 

    immutable class tutorials:exceptions@AdvancedExceptionTest
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
			catch (ExceptionA e)
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
			catch (ExceptionA e)
			{
				Console.printLine("test2 caught ExceptionA");
			} 
			catch (ExceptionB e) 
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
			catch (Exception e) 
			{
				Console.printLine("test3 caught Exception");
			}
		}

		public main( String[] args ) => () 
		{
			test3();
		}
    }


Let's start at **Line 50** in the ``main()`` method. Here we see a method call to ``test3()``. Control flows to this method and inside the ``try`` block on **Line 40** where we see a method call to ``test2()``. Once we enter ``test2()``, we see a method call to ``test1()``  on **Line 24**. Inside ``test1()``, there is a call on **Line 12** to ``test()``.

Now, control has shifted to ``test()``, and on **Line 5** we see that ``ExceptionB`` is thrown. At this point, we say that the exception is in flight and begins the unwinding process. Starting with the ``try-catch`` block in ``test1()``, the exception will propagate backwards through the methods that were called until the exception is caught by one of the ``catch`` blocks. If control was passed back to the ``main()`` method with the exception still in flight, the program would terminate with the exception message printed to the console. 

However, this is not the case in our example. First, execution returns to ``test1()``. In this method, only an exception of type ``ExceptionA`` can be caught. Thus, the exception keeps unwinding to ``test2()``. Here, the first ``catch`` handles only ``ExceptionA``, but the second ``catch`` handles an  ``ExceptionB`` -- a match! Now, ``test2 caught ExceptionB`` is printed to the console, and control flows back to the ``main()`` method. Since the exception was caught, the program ends normally.



    

