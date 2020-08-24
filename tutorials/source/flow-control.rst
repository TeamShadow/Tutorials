************************
Flow Control and Looping
************************

So far, we have learned how to create a basic program in Shadow, declare and use variables, and write expressions with different kinds of operators. In the simple example programs we have analyzed thus far, the flow of program execution has only taken steps forward. Execution starts with the first statement in the ``main()`` method (a variable declaration, ``Console.printLine()``, etc.) and continues to the second and third and so on. Nothing is skipped, and no action is repeated. Straightforward. 

However, we can control the flow of execution with special statements: ``if``, ``else``, ``break``, ``continue``, ``switch``, and several kinds of loops. These statements have the power to manipulate the flow of a program, opening the door for more powerful programs that can solve more difficult problems. 


``if`` and ``else`` statements
==============================

Although ``if`` statements were briefly mentioned in a :ref:`previous section<Logical operators>`, we cover them here in depth.

Below is the basic structure of an ``if``/``else`` statement. 

.. code-block:: shadow 

	if ( ) // A boolean expression 
	{ 
		// Do something if the expression is true
	}
	else
	{
		// Do something different if the expression is false
	}

There are a few things to note: 

* You cannot have an ``else`` statement without a matching ``if`` statement, but you can have an ``if`` statement without an ``else``. 
* You cannot have multiple ``else`` statements attached to the same ``if`` statement. 
* The expression inside the ``if`` statement must evaluate to either ``true`` or ``false``. For example, you could **not** say ``if(x = 6)``. This would cause a compiler error. 
* Logical and relational operators can help you write complex conditions inside the ``if`` statements. 

Nested ``if``/``else`` statements
---------------------------------

Most Shadow control structures can be *nested* inside of each other. In other words, you can put an ``if`` statement inside of another ``if`` or ``else`` statement, resulting in arbitrarily complex decisions. When doing so, proper brace placement controls which ``if`` matches with which ``else``.

Below are some possible examples: 

.. code-block:: shadow

    var numDonuts = 4; 
    if (numDonuts > 0)
    { 
		// Note how braces determine program flow
		if (numDonuts % 2 == 0)
		{
			Console.printLine("You have an even number of donuts left!"); 
			Console.printLine("Now you have to share."); 
		}
		else 
		{
			Console.printLine("You have an odd number of donuts left!"); 
		}			
    } // Note that no else is needed for the outer if


The console output: 


.. code-block:: console 

    You have an even number of donuts left!
    Now you have to share. 


If we have a series of mutually exclusive alternatives and only want to choose one, we can start with an ``if`` statement, list the remaining alternatives with ``else if`` statements, and end with an ``else`` statement that determines what happens if none of the other alternatives matched.


.. code-block:: shadow
    :linenos:

    /*
     * For his 25th Birthday, Surya and his friends decide to go to an amusement
     * park with 3 rides. Surya has never been to an amusement park before, so it
	 * is your job to determine which ride Surya would enjoy based off of his list
	 * of attributes.
     */
		 
    var name = "Surya";  
    var scaredOfHeights = false; 
    var noLoops = true; 
    var idealRideSpeed = 100; 
		 
    if (scaredOfHeights and noLoops) 
    {
        Console.printLine("Sorry, there aren't any rides without loops and heights."); 
    }
    else if (!scaredOfHeights and idealRideSpeed >= 110) 
    {
        Console.printLine("You would love the Super Speedy Plunge!"); 
    } 
    else if (!noLoops or idealRideSpeed < 80) 
    {
        Console.printLine("Get in line for the Loop Dee Loop"); 
    }
    else
    {
        Console.printLine("Get ready to go on Madness Mountain!"); 
    }


Which ride should Surya go on? 

.. code-block:: console

    Get ready to go on Madness Mountain!


Why should Surya go on Madness Mountain? Let's trace through the code. 

**Lines 8-11** establish Surya's tastes. We know that he prefers rides that go 100 mph, don't have loops, but can be high. Control then is passed to  **Line 13**. This expression evaluates to ``false`` because ``scaredOfHeights`` is ``false``. This means that the statement inside the first ``if`` is skipped, and execution is passed to **Line 17**. Since his ideal ride speed is not greater than or equal to 110 mph, the expression evaluates to ``false`` and control is passed to **Line 21.** Neither statement is ``true``, so the last ``if`` evaluates to ``false``. Therefore, control defaults to the statement inside the final ``else``, stating that Surya should ride Madness Mountain. 

Note that if one of the earlier ``else if`` statements had evaluated to ``true``, the rest of the ``if`` statments and the final ``else`` would **not** be evaluated, and control would be passed to the the next line after the final ``else``.


Use of braces
-------------

If an ``if`` or ``else`` statement is followed by a single line of code, braces are not needed. However, this rule can lead to unintended behavior if you're not careful. See below: 


.. code-block:: shadow

    if (1 > 2)
        Console.printLine("hey"); 
        Console.printLine("hi"); 

Since both statements following the ``if`` are indented, you might assume that code printing both ``"hey"`` and ``"hi"`` is inside the ``if`` statement, meaning that neither will be printed in this case. Even though 1 is certainly not greater than 2, ``"hi"`` is still printed.  Without braces, only the first line after the ``if`` is considered part of the statement.

Some programmers *always* use braces, even for single-line ``if`` statements.  This practice is certainly safer and can avoid the frustration that comes when your program does not behave as you expect it to.

One of the reasons that braces are not required for single-line ``if`` statements  is to make writing ``else if`` statements simpler.  In fact, there is no ``else if`` construct in Shadow.  However, since the ``if`` in the ``else if`` and all of the code beneath it is treated liked a single statement, it allows us to write code like the example above:

.. code-block:: shadow

	if ( ) // First condition
	{
	
	}
	else if( ) // Second condition
	{
	
	}
	
Without this rule, Shadow would either need to define a keyword for this case (as Python does with ``elif``) or require additional braces, as in the following:

.. code-block:: shadow

	if ( ) // First condition
	{
	
	}
	else 
	{
		if( ) // Second condition
		{
		
		}
	}

From the perspective of the compiler, this version is identical to the one above that uses one fewer pair of braces.

``switch`` statements
=====================

When you have a series of mutually exclusive choices, an alternative to using a series of ``else if`` statements is to use a ``switch`` statement. 

.. note:: Although most control structures are nearly identical to those in Java and C-family languages, the syntax for ``switch`` statements in Shadow makes a number of departures.  Becauses cases no longer "fall through," the ``break`` statement is no longer used, and the bodies of cases must be surrounded by braces if they are more than a single line.

A ``switch`` statement is useful when you have a variable that can take on a fixed list of values and you need to take different actions depending on which value it is. Each value corresponds to a case with a distinct set of actions. For example, say you have a ``String`` variable that holds a genre of music. There are many different genres of music: hip-hop, rock, pop, alternative, and so on. We can map each one of these genres to a ``case`` statement and recommend a specific song in that ``case`` based on the genre given, as shown below:

.. code-block:: Shadow
    :linenos:

	var genre = "rock"; 
	switch( genre )
	{
		case( "pop", "Pop" ) Console.printLine("Listen to \"Firework\" by Katy Perry!");					
		case( "alternative" ) Console.printLine("Listen to \"Call Me\" by Blondie");			
		case( "rock" ) Console.printLine("Listen to \"We are the Champions\" by Queen");				
		case( "country" ) Console.printLine("Listen to \"Need You Now\" by Lady Antebellum");
		case( "hip-hop/rap" ) Console.printLine("Listen to \"Hey Ya!\" by Outkast");
		default Console.printLine("Hmm, we don't have recomendations for that genre.");			
	}

Here the output will be:

.. code-block:: console

    Listen to "We are the Champions" by Queen!

Why? First consider **Line 2**. Here we see the ``switch`` statement, which takes the ``String`` variable ``genre``. In general, you can use only integer primitive types or the ``String`` type as arguments for a ``switch`` statement. In this case, the value of ``genre`` will be compared to five different cases. These cases in **Lines 4-8** represent the possible genres of music. 

The ``switch`` statement works by going through the cases, checking to see if one  matches the value of ``genre``, which is ``"rock"``. The program stops searching when a match is found on **Line 6**. Then, the ``Console.printLine()`` statement on this line is printed and control is passed to the next line outside of the ``switch``. 

Notice the ``default`` on **Line 9**. If none of the cases had equaled ``"rock"``, the code after the ``default`` statement would have run. However, a ``default`` case is not required. If no cases match and there is no ``default``, the program would exit the ``switch`` without executing anything. 

Below are some important takeaways for ``switch`` statements:

* Only ``int``, ``byte``, ``short``, ``long`` (and unsigned versions of these) and ``String`` values may be used in a ``switch`` statement.
* There is no limit to the number of cases.
* A ``default`` is not required, but there can only be one. 
* You may include multiple cases in one statement, such as ``case( 1, 2, 3 )``.
* The ``default`` does not have to be the last statement in the body of the ``switch``. 
* Multiple statements for one ``case`` must be enclosed in braces (see below).  

.. code-block:: shadow

    var number = 0;
    switch (number) 
    {
        case(0)
        {
            Console.printLine("Uh oh, your number is 0."); 
            Console.printLine("Is 0 positive, negative, or neither?"); 
        }
        default
        {
            Console.printLine("Your number is not zero."); 
        }
    }
	
``switch`` statements are not as flexible as combinations of ``if`` and ``else`` statements:  They can't take a ``double``, a ``float``, or any non-``String`` object as an argument, and they can't be used to express a range of values.  However, they can be a more readable alternative to a series of ``if`` statements if there is a long list of outcomes with each outcome associated with a value.

.. note:: Support for ``enum`` types is planned in future versions of Shadow, at which time ``enum`` values will also be legal values to use in ``switch`` statements.


``while`` loops 
===============

Now, we will shift to *loops*. When programming you  will sometimes need to repeat an action multiple times. For example, let's say you wanted to write a program that outputs "I love Shadow!" five times in a row. You could write ``Console.printLine("I love Shadow!")`` five separate times, but doing so would be tedious and become even more tedious if you wanted to print it 100 times. Loops allow you to repeat code for a specified number of times, or while a certain condition is met. 

The first type of loop we discuss is the ``while`` loop, which repeats code based as long as a ``boolean`` expression is ``true``. The basic structure is below: 


.. code-block:: shadow

	while () // boolean expression
	{
		// block of code to repeat
	}

A key concept for most loops is the *control variable* or *loop counter*. This variable controls how many times the loop will execute and prevents *infinite loops*. 

For example, let's examine this block of code: 

.. code-block:: shadow

	var favoriteNumber = 13; 
	while (favoriteNumber > 0)
	{
		Console.printLine("Your favorite number is " # favoriteNumber); 
	}

What happens? This is a basic example of an infinite loop. The ``boolean`` expression ``favoriteNumber > 0`` will always evaluate to ``true``, so "Your favorite number is 13" will be printed an infinite number of times.

Normally, you want the condition that controls the loop to change as the loop progresses so that the loop eventually ends, as in the following example. 

You want to create some basic programming art, so you will start by "drawing" a straight, horizontal line that is 10 characters long. Here's the catch: Even numbered characters must be represented by ``$``, and odd numbered characters must be represented by a ``^``. Assume that the first character in the line is labeled 1. 

.. code-block:: shadow
    :linenos:

    // Loop counter
    var count = 1; 
			
    while (count <= 10) // Loop condition
    {
        if (count % 2 == 0) 
		{
			Console.print("$"); 
		}
		else
		{
			Console.print("^"); 
		}
		
		// This update prevents an infinite loop		
		count += 1; 
     }

Here is the output:


.. code-block:: console

    ^$^$^$^$^$ 

Let's analyze some key elements of this segment of code. The loop counter  ``count``  is declared in **Line 2**. Note that we chose to initialize ``count`` to 1. Programmers often start counters at 1, but they often start them at 0 as well, which is especially beneficial when dealing with :ref:`arrays <Arrays>`. In this case, we started ``count`` at 1 because we are told to assume that the first character is odd. Regardless of what value you set the counter to, counter variables must **always** be initialized.

**Line 4** is the condition that controls the ``while`` loop.  As long as ``count`` is less than or equal to 10, control flows to the body of the loop, and this action is repeated until ``count`` is greater than 10. Note that we used ``<=`` instead of ``<``. If we had used ``<``, when ``count`` got to 10, ``10 < 10`` would evaluate to false, and we end up with one fewer character than needed. However, if ``count`` had started at 0, ``count < 10`` would be the appropriate expression.

.. note:: If you want to repeat a loop *x* times, a good guideline is to repeat your loop as long as your counter is **strictly less than** *x* if your counter started at 0 or **less than or equal to** *x* if your counter started at 1. 

Lastly, **Line 16** increments ``count`` by 1 for each iteration of the ``while`` loop. If this statement had been absent, ``count`` would always equal 1, printing an infinite number of ``^`` characters.  As long as the condition of your loop eventually becomes ``false``, it doesn't matter what operations or combination of operations (addition, subtraction, multiplication, division, etc.) you perform on your loop counter.

The loop condition could also be based on user input, which can make the loop run an unpredictable number of times.  


``do while`` loops
==================

This section covers another type of loop, called the ``do while`` loop. The structure of this loop is outlined below:

.. code-block:: shadow 

    var count = 0; 
    do 
    {
        // Some code to execute	
		count += 2;  // Increment counter
			
    } while (count < 100); // Don't forget the ";" after the while

Although similar in structure and concept to the ``while`` loop, there are differences. The most obvious difference is the point at which the ``boolean`` condition is checked. In a ``while`` loop, before control flows to the body of the loop and anything is executed inside of it, the ``boolean`` expression must be evaluated first. If it is initially ``false``, the loop is in skipped and control flows to the first statement after the loop. However, in a ``do while`` loop, the body of the loop is **guaranteed** to execute at least once before the ``boolean`` expression is evaluated.  This concept is best illustrated via an example:
    
.. code-block:: shadow 

    /* Imagine you are at an arcade and have a gift card 
     * with a certain number of points left to play
     * pinball. Every time you swipe the card to activate the
     * game, you lose one point. This short program mimics the 
     * messages the game would give. 
     */
		
    var points = 5; 
    do 
    {
        if (points <= 0) 
        {
            Console.printLine("I'm sorry, you don't have enough points to play!"); 
		}
		else 
		{
			 points -= 1; 
			 Console.printLine("You're a Pinball Wizard! Starting game...."); 
			 Console.printLine("Now you have " # points # " points!"); 
			 Console.printLine("~~~~~~~~~~~~~~~~~~~~~~"); 
		}
    } while (points >= 0); 

Before you look at the console output below, see if you can predict what it will be!

.. code-block:: console

    You're a Pinball Wizard! Starting game....
    Now you have 4 points!
    ~~~~~~~~~~~~~~~~~~~~~~
    You're a Pinball Wizard! Starting game....
    Now you have 3 points!
    ~~~~~~~~~~~~~~~~~~~~~~
    You're a Pinball Wizard! Starting game....
    Now you have 2 points!
    ~~~~~~~~~~~~~~~~~~~~~~
    You're a Pinball Wizard! Starting game....
    Now you have 1 points!
    ~~~~~~~~~~~~~~~~~~~~~~
    You're a Pinball Wizard! Starting game....
    Now you have 0 points!
    ~~~~~~~~~~~~~~~~~~~~~~
    I'm sorry, you don't have enough points to play!

Note that, no matter how many points the player starts with, the body of the loop is guaranteed to execute at least once. For example, if the user starts with 0 points, the message will still appear telling them they do not have enough points to play. Afterwards, the ``boolean``	expression ``points  >=  0`` evaluates to ``false``. Thus, the loop ends, and control is passed to the next statement after the ``do while`` loop. 

Despite these differences, use the same elements for ``while`` loops when implementing a ``do while`` loop: 

* A ``boolean`` expression that determines whether the loop will continue
* A loop counter or other flag that controls how many more times the loop will continue
* Always check to make sure to your code will not result in an infinite loop

.. note:: When determining whether you want to use a ``while`` or a ``do while`` loop, think about how you want your program to behave. Is there an initial condition required for the loop to even run in the first place or do you want the loop to run at least once? 


``for`` loops
=============

The most commonly used kind of loop in Shadow is the ``for`` loop. There are three critical elements for any ``for`` loop: 

#. :ref:`Initializing the counter`
#. :ref:`Condition for continuing`
#. :ref:`Updating the counter`


Below is a basic example of a ``for`` loop we will break down piece-by-piece: 

.. code-block:: shadow

    for (int i = 0; i < 5; i += 1)  
    {
        Console.printLine("Hey you! Wake up!!"); 
    }

This code prints out "Hey you! Wake up!!" five separate times. 


.. code-block:: console

    Hey you! Wake up!!
    Hey you! Wake up!!
    Hey you! Wake up!!
    Hey you! Wake up!!
    Hey you! Wake up!!
    

Initializing the counter
------------------------ 

.. code-block:: shadow

	int i = 0;

The first thing you should do when writing a ``for`` loop is declare and initialize a counter variable. This variable is used to dictate the number of times the program will run through the loop.  There is no special requirement for the variable's name, but it is common to use ``i``, ``j``, and ``k`` for variables whose only purpose is as a counter. Usually, the variable is declared and initialized inside the loop, as seen above. 

However, ``i`` does not *have* to be declared inside the ``for`` loop. It could look something like this instead:

.. code-block:: shadow

    int count; 
    for (count = 0; count < 5; count += 1)  
    {
        Console.printLine("Hey you! Wake up!!"); 
    }

    Console.printLine(count); 

Does declaring the variable *outside* the loop change the output? No. "Hey you! Wake up!!" is still printed five times, as in the original example, but the *scope* of the variable has changed. In Shadow, the scope of a variable is where the variable is visible in the program. Although scope will be discussed in greater depth in a :ref:`later tutorial <A note on scope>`, note the distinction here. In the first example, ``i`` is declared and initialized inside the ``for`` loop. This means that if you tried to write ``Console.printLine(i);`` *outside* of the loop, it would be a compiler error because the variable ``i`` would be out of scope and no longer have meaning. In other words, when you declare a variable inside of a loop, it only has meaning *in that loop*.  In the second example, ``count`` is declared outside of the loop, making it available before, during, and after the loop.

Why would you want to do this? Sometimes when writing programs, we want to use the counter variable in later calculations or for some other purpose, and declaring the variable outside of the loop allows this to happen.  In most cases, however, declaring the variable inside the loop is safer, since the risk of introducing a meaningless value from earlier in the program is smaller.


Condition for continuing
------------------------

.. code-block:: shadow

	i < 5;

The second step when creating a ``for`` loop is to define the condition that determines when the loop will end. Since we want to print the message five times and ``i`` starts at 0, ``i < 5;`` is the appropriate expression. If we had initialized ``i`` to be 1, then the condition would need to be ``i <= 5;`` 

.. note:: Although ``<`` , ``>`` , ``<=``, ``>=`` are probably the most common operators used in ``for`` loop conditions, others such as ``!=`` may be used. 

As long as the condition eventually becomes ``false`` (in order to avoid an infinite loop), it's up to you to decide what the condition should be for your problem. 


Updating the counter
-------------------- 

.. code-block:: shadow

	i += 1

Finally, when writing a ``for`` loop, the last expression inside the parentheses is where you update the counter variable. In this example, we said ``i += 1;``. This means that for each pass through the loop, ``i`` will increase by 1. If we had declared ``i`` outside of the loop and then printed the value of ``i`` after the loop, it would be 5. This is because after the fifth "Hey you! Wake Up!! " is printed, ``i`` is incremented by 1 and becomes 5, which causes the condition ``i < 5;`` to be ``false`` and thus end the loop. 

There are a few more details to consider: 

* Similar to ``if``/``else`` statements, loops do not need braces if the body of the loop is only a single line, but you should exercise caution when leaving them off. 
* Although in the given example we increment the counter variable ``i``, we could have  *decremented* the counter variable instead (or used other operations if useful). We could have started ``i`` at 5, changed the condition to ``i >= 1``, and updated ``i`` with the statement ``i -= 1`` to achieve the same end result, although running a loop backwards might be harder to reason about.
* It's legal to leave out any of the three parts of a ``for`` loop.  If the counter variable has already been initialized, the part before the first semicolon can be empty.  If there is no condition before the second semicolon, the condition is treated like it's always ``true`` (requiring a ``break`` or ``return`` to leave the loop).  There need not be any update to the counter variable after the second semicolon if the update happens in the body of the loop.


All three kinds of loops are interchangeable.  You might notice that we discussed the same elements of initializing a counter, checking a condition, and updating the counter in both ``while`` and ``for`` loops.  The three kinds of loops are suited to slightly different problems and are provided as a convenience to the programmer.  A good set of guidelines for picking loops is the following:

* Use ``for`` loops when you know how many times you want the loop to repeat.
* Use ``while`` loops when you don't know how many times you want the loop to repeat.
* Use ``do while`` loops when you want to guarantee that the body of the loop runs at least once, often when handling user input.

Nested loops
============

In this brief section, we will examine *nested loops* and their applications. The general structure of this kind of loop is shown below: 

.. code-block:: Shadow
	:linenos:

	for (int row = 0; row < 5; row += 1) // Outer loop
	{
		for (int column = 0; column <= row; column += 1) // Inner loop
		{
			Console.print("@"); 
		}
		Console.printLine();  
	}

The ouput is as follows: 

.. code-block:: console

    @
    @@
    @@@
    @@@@
    @@@@@


Nested loops will have an outer loop and an inner loop.  For every time the outer loop runs once, the inner loop can run many times. Let's trace through the example to see how control flows between the outer and inner loops. 

In this example, the goal was to output a right triangle using the ``@`` symbol. Since we will need five separate rows of varying length to do so, the outer loop needs to run a total of five times. Thus, the statement on **Line 1** ensures that will happen. 

But how do we get the different numbers of ``@`` symbols on each of the five row? The actual printing of each symbol is controlled by the inner loop. Initially, the outer loop counter variable, ``row``,  is  equal to 0. Before ``row`` is incremented by 1, control is passed to the inner loop. Each time that happens, ``column`` is initialized to 0. We print a ``@`` for each column, as long as the column we're on is less than or equal to the row we're on. When ``column`` is greater than ``row``, the inner loop finishes executing and control flows to the statement outside of the inner loop -- the empty ``Console.printLine()`` that moves the output to a new row. If we had forgotten **Line 7**, all the ``@`` symbols would have been printed on the same line. 

Afterwards, we reach the end of the outer loop and increment ``row`` by 1, returning to the top of the outer loop as long as ``row`` is less than 5. Note that when the inner loop is executed again, it is reset, starting ``column`` back at 0. This process continues until the fifth line of 5 ``@`` symbols is printed and ``row`` becomes 5, which causes the program to exit the outer loop. The triangle is now complete!

Although this example uses ``for`` loops, any kind of loop can be nested inside of any other.  It's possible to nest arbitrary deep as well, with a loop inside of a loop inside of a loop, and so on.


``break`` and ``continue``
==========================

Two other statements that can alter the flow of control in a Shadow program are ``break`` and ``continue``. These statements can be useful to either exit a loop or skip statements in the body of the loop. 

First, let's discuss ``break``. When a program reaches a break statement, it will immediately terminate the current loop, and control will flow to the next statement outside of that loop. For example, see the short block of code below: 

.. code-block:: shadow
	:linenos: 

	for (int i = 1; i < 5; i += 1)
	{
		if (i * 2 > 5)
		{
			break;
		} 
		Console.printLine(i); 	
	}
	Console.printLine("Yay! The loop is complete!"); 

Here is the console output: 

.. code-block:: console

    1
    2
    Yay! The loop is complete!

When ``i`` is 3, the statement ``i * 2 > 5`` becomes ``true``, and the ``break`` statement is executed. Thus, the program exits the loop and control is passed to **Line 9**. It is important to note that a ``break`` statement *must* be located inside of a loop, or you will get a compiler error. 

Similar to a ``break`` statement, a ``continue`` statement must also be placed inside of a loop to avoid a compiler error. When the program reaches a ``continue`` statement, control jumps to the end of the loop. For example, in a ``for`` loop, any statements after ``continue`` would be skipped, and the program would go straight to the counter variable update, followed by the evaluation of the condition. A ``while`` loop would behave in much the same way -- any statements after ``continue`` would be skipped, and the condition would be checked. 

An example of a ``while`` loop with a ``continue`` statement is below: 

.. code-block:: shadow
	:linenos: 
    
	int i = 0; 
	Console.printLine("Odd Numbers");
		
	while (i < 10)
	{
		if (i % 2 == 0) 
		{ 
			i += 1; 
			continue; 
		}

		Console.print(i # " ");
		i += 1;  
	}


The following output is produced: 

.. code-block:: console

    Odd Numbers
    1 3 5 7 9 

As seen in the program above, when ``i`` is even (``i % 2 == 0``), the program executes an increment followed by a ``continue`` statement. From there, **Lines 12 and 13** are skipped, and control flows back to the initial condition. Thus, only odd numbers are printed. 

.. note:: Although ``break`` and ``continue`` can be useful for quick solutions, it's bad programming practice to rely on them. If you use a ``break`` or ``continue`` statement, there's always another way to achieve the same effect. For example, in the previous example with odd numbers, a simple ``if`` statement to checking if a number is odd would be a valid (and more readable) solution.