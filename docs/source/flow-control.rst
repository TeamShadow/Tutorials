Flow Control and Looping
------------------------
So far, we have learned how to create a basic program in **Shadow**, declare and use variables, and write expressions with different kinds of operators. In the simple example programs we have analyzed thus far, it is easy to see how **control flows**. Execution starts with the first statement in the program (a variable declaration, ``Console.printLine()``, etc.) and continues to the second and third and so on. Nothing is skipped and no action repeated. Straightforward. 

However, **flow control** becomes more interesting as we begin to introduce new statements: ``if``, ``else``, ``break``, ``continue``, ``switch``, and different kinds of loops. These statements have the power to manipulate/direct the flow of a program, thus opening the door for more powerful programs. 


``if`` and ``else`` Statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although ``if`` statements were briefly mentioned in a :ref:`previous section<Logical Operators>`, they will now be covered in-depth. 

Below is the basic structure for an ``if``/``else`` statement. 


.. code-block:: shadow 


    if ( ) //some expression that evaluates to true or false 
    { 
        //do something here 
    }
    else
    {
        //do something different here
    }

There are a few things to note: 

* You cannot have an ``else`` statement without a matching ``if`` statement, but you can have an ``if`` statement without an ``else``. 
* You cannot have multiple ``else`` statements with the same ``if`` statement. 
* The expression inside the ``if`` statement must evaluate to either ``true`` or ``false``. For example, you could NOT say ``if(int x = 6)``. This would cause a compile error. 
* Logical operators (and the others) are useful when writing ``if``/``else`` statements. 

**Nested** ``if``/``else`` **Statements** 

Another important concept is nested ``if``/``else`` statements. There are many different ways to structure these, and it is very important to be mindful of your use of ``{ }`` in order to control which ``if`` matches with which ``else``.  ``else`` statements match with the **closest** ``if`` statement, so lack of attention to brace placement can lead to some unintended outputs. For example, you may have an ``if``/``else``  enclosed inside of one larger ``if``, or you may choose to have sequences of ``else if`` statements. 

Below are some possible examples: 

.. code-block:: shadow  
    :linenos: 

    //Here is a example of a nested if/else statement (inside a larger if)
    var numDonuts = 4; 
    if (numDonuts > 0)
    { 
        //pay attention to how the use of brackets directs program flow
	if (numDonuts % 2 == 0)
	{
	    Console.printLine("You have an even number of donuts left!"); 
	    Console.printLine("Now you have to share."); 
	}
	else 
	{
	    Console.printLine("You have an odd number of donuts left !"); 
	}
			
    } //Notice how there is no else statement for the outside if. This is OK. 


The console output: 


.. code-block:: console 

    You have an even number of donuts left!
    Now you have to share. 


Lastly, here is an example of ``else if``. 


.. code-block:: shadow
    :linenos:

    /*
     * For his 25th Birthday, Surya and his friends decide to go to an amusement
     * park with 3 rides. Surya has never been to an amusement park before, so it is your 
     * job to determine which ride Surya would enjoy based off of his list of 
     * attributes. Good luck!
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

**Lines 8-11** establish the "rules" for determining what ride he should go on. We know that he prefers rides that go 100 mph, don’t have loops, and have heights. Control then is passed to  **Line 13**. This expression evaluates to ``false`` because ``scaredOfHeights`` is ``false``. This means that the statement inside the first ``if`` is skipped, and execution is passed to **Line 17**. Since his ideal ride speed is not greater than or equal to 110 mph, the expression evaluates to ``false`` and control is passed to **Line 21.** Neither statement is ``true``, so the last ``else if`` evaluates to ``false``. Therefore, the statement inside the final ``else`` is printed (there is no condition), and Surya should ride Madness Mountain. 

It is important to note that if one of the earlier ``else if`` statements had evaluated to ``true``, the rest of the ``else if`` and final ``else`` would NOT be evaluated, and control would be passed to the the next line after the final ``else``. 


**One Final Note** 

Technically, if an ``if`` statement is followed by a single line of code, braces are not needed. However, this can lead to some unintended output if you are not careful. See below: 


.. code-block:: shadow

    if (1 > 2)
        Console.printLine("hey"); 
        Console.printLine("hi"); 

Since both statements following the ``if`` are indented, you might assume that both "hey" and "hi" will NOT be printed. However, even though 1 is certainly not greater than 2, "hi" is still printed because when braces are not present, only the first line after the ``if`` is considered part of it. 


``while`` Loops 
^^^^^^^^^^^^^^^

Now, we will shift to **loops**, specifically ``while`` loops. But first, we must answer a basic question: *What is a loop?* As with Shadow, and programming in general, sometimes you will need to repeat an action multiple times. For example, let's say for some random reason we wanted to write a program that outputs "I love Shadow!" 5 times in a row. We could write ``Console.printLine("I love Shadow!")`` 5 separate times. However, this can become quite tedious and inefficient. Cue **loops**.  Loops allow you to repeat code for a specified number of times, or while a certain condition is met. 

The first type of loop discussed is the ``while`` loop, which repeats code based off of some boolean expression. The basic structure is below: 


.. code-block:: shadow

    while () //boolean expression
    {
        //block of code to repeat
    }


Although not defined above, a key concept for ``while`` loops, and really any loop, is the **control variable or loop counter**. This variable controls how many times the loop will execute and prevents **infinite looping**. 

For example, let’s examine this block of code: 


.. code-block:: shadow

    var favoriteNumber = 13; 
    while (favoriteNumber > 0)
    {
        Console.printLine("Your favorite number is " # favoriteNumber); 
    }

What happens? This is a basic example of an **infinite loop**. The ``boolean`` expression ``favoriteNumber > 0`` will always evaluate to ``true``, so "Your favorite number is 13" will be printed an infinite number a times, causing the program to crash. There is, however, a way to prevent this by using a **loop counter.**

In order to see how a **loop counter** works, consider the following situation: 

You want to create some basic programming art, so you will start by "drawing" a straight, horizontal line that is 10 characters long. Here is the catch: even number characters must be represented by a "$", and odd characters must be represented by a "^". Assume that the first character in the line is labeled 1. 




.. code-block:: shadow
    :linenos:

    //This is the loop counter
    var count = 1; 
			
    while (count <= 10) //boolean expression 
    {
        if (count % 2 == 0) 
	{
	    Console.print("$"); 
	}
	else
        {
	    Console.print("^"); 
	}
	
        //This is the most important part in preventing an infinite loop		
	count += 1; 
     }

Here is the output:


.. code-block:: console

    ^$^$^$^$^$ 

If you count, you will see that there are 5 of each character! Before we move on, let’s analyze some *key elements* of this block of code. The first step is seen in **Line 2**, where the loop counter, ``count``,  is declared. It is important to note why we chose to initialize ``count`` to 1 instead of 0. A lot of times it is left up to simply programmer preference, but sometimes the choice of an initial value can make a program significantly less (or more) complicated. In this case, we started ``count`` at 1 because we are told to assume that the first character is odd. We could have made it work by starting ``count`` at 0, but there would need to be an extra step because ``0 % 2 == 0`` (which prints the even-number character). However, regardless of what value you set the counter to, **counter variables must always be initialized**.

**Line 5** is the boolean expression that drives the ``while`` loop.  As long as ``count`` is less than or equal to 10, control flows to the body of the loop, and this action is repeated until ``count`` is greater than 10. It is also important to note what we used ``<=`` instead of ``<``. If we had used ``<``, when ``count`` gets to 10, ``10 < 10`` evaluates to false, and we end up with one less character than needed. However, if ``count`` had started at 0, ``count < 10`` would be the appropriate expression. 

Lastly, **Line 16** increments ``count`` by 1 for each iteration of the ``while`` loop. If this statement had been absent, ``count`` would always equal 1, creating an infinite number of ``^`` and causing the program to crash.  As long your loop is getting closer to a case where it ends (or is ``false``), it does not matter what operations or combination of operations you perform on your **loop counter** (addition, subtraction, multiplication, division, etc.).  


``do while`` Loops
^^^^^^^^^^^^^^^^^^ 

This section covers another major type of loop, called the ``do while`` loop. The basic structure of this loop is outlined below:

.. code-block:: shadow 

    var count = 0; 
    do 
    {
        //some code to execute	
	count += 2;  //increment counter
			
    } while (/*boolean expression*/); 
    //Do NOT forget the ";" at the end of the while

Although very similar in structure and concept to the ``while`` loop, there are some key differences. The most obvious difference is in the order the ``boolean`` condition (or ``while`` statement) is checked. In a ``while`` loop, before control flows to the body of the loop and anything is executed inside of it, the ``boolean`` expression must be evaluated first. If it is initially ``false``, the loop is in essence "skipped" and control flows to the first statement outside of the loop. However, in a ``do while`` loop, **the body of the loop is guaranteed to execute at least once** before the ``boolean`` expression is evaluated.  This concept is best illustrated via an example. 


    
.. code-block:: shadow 
    :linenos: 

    /* Imagine you are at an arcade and have a gift card 
     * with a certain number of points left to play
     * pinball. Every time you swipe the card to activate the
     * game, you lose one point. This short program mimicks the 
     * messages the game would give. 
     */
		
    var points = 5; 
    do 
    {
        if (points <= 0) 
        {
             Console.printLine("I'm sorry, you don't have enough points to play!"); 
	     points -= 1; 
	}
	else 
	{
	     points -= 1; 
	     Console.printLine("You're a Pinball Wizard! Starting game...."); 
	     Console.printLine("Now you have " # points # " points!"); 
	     Console.printLine("~~~~~~~~~~~~~~~~~~~~~~"); 
	}

     } while ( points >= 0 ); 


Before you look at the consol output below, see if you can predict it!

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

The key point to make with this example is that **no matter how many points the player starts with, the body of the loop is guaranteed to execute at least once**. For example, if the user starts with 0 points, the message will still appear telling them they do not have enough points to play. Then, ``points`` is decreased by 1, and the ``boolean``	expression ``points  >=  0`` evaluates to false. Thus the loop ends, and control is passed to the next statement outside of the ``do while`` loop. 

Despite these differences, it is still important to follow the same principles discussed in the ``while`` loop section when implementing a ``do while`` loop: 

* A boolean expression that determines whether the loop will continue
* A loop counter that controls how many more times the loop will continue
* Always check to make sure to your code will not result in an infinite loop

.. note:: When determining whether you want to use a ``while`` or a ``do while`` loop, think about how you want your program to behave. Is there an initial condition required for the loop to even run in the first place? Or do you want the loop to run at least once? 


``for`` Loops
^^^^^^^^^^^^^

Another extremely useful and important kind of loop in Shadow is the ``for`` loop. There are three critical elements for any ``for`` loop. 

#. **Declaration and initialization** of the counter variable
#. **Condition** to be evaluated each pass through the loop
#. Increment/decrement/**change** of the counter variable 


Below is a very basic example of a ``for`` loop that we will break down piece-by-piece: 

.. code-block:: Shadow

    for (int i = 1; i <= 5; i += 1)  
    {
        Console.printLine("Hey you! Wake up!!"); 
    }

This code prints out "Hey you! Wake up!!" 5 separate times. 


.. code-block:: console

    Hey you! Wake up!!
    Hey you! Wake up!!
    Hey you! Wake up!!
    Hey you! Wake up!!
    Hey you! Wake up!!
    

1. **Initialization of the Counter Variable** 

``int i = 1;``

The first thing you should do when writing a ``for`` loop is declare and initialize a **counter variable**. This variable is used to dictate the number of times the program will run through the loop.  There is no requirement for the variable’s name, but typically something short is chosen, like ``i``. Usually, the variable is declared and initialized inside the loop, as seen above. 

However, ``i`` does not *have* to be initialized inside the ``for`` loop. It could look something like this instead: 


.. code-block:: Shadow

    int count; 
    for (count = 1; count <= 5; count += 1)  
    {
        Console.printLine("Hey you! Wake up!!"); 
    }

    Console.printLine(count); 

Does declaring the variable *outside* of the loop change the output? **No.**  "Hey you! Wake up!!" is still printed 5 times, like in the original example. The difference, instead, lies in the **scope of the variable.**  In Shadow, the **scope** of a variable is where the variable carries meaning in the program. Although **scope** will be discussed more in-depth in a :ref:`later tutorial<A Note on Scope>`., it is important to note the distinction here. In the first example, ``i`` is declared and initialized inside the ``for`` loop. This means that if you tried to write ``Console.printLine(i);`` outside of the loop, you would get a compile error because you are not in the *scope* of ``i``. In other words, when you declare a variable inside of a loop, it only carries meaning *in that loop*, so in essence, it does not exist/cannot be accessed outside of the loop. However, in example 2, ``count`` is declared outside of the loop. Now, not only is ``count`` within the scope of the ``main()`` method, it also can be used inside of the loop. Why would you want to do this? Sometimes when writing programs, we want to use the counter variable in later calculations or for some other purpose, and declaring the variable outside of the loop allows this to happen. 


2. **The Condition to be Evaluated** 


``i <= 5;``

The second step when creating a ``for`` loop is to define the condition that determines when the loop will end. In this example, since we want to print the message 5 times, and ``i`` starts at 1, ``i <= 5;`` is the appropriate expression. If we had initialized ``i`` to be 0, then the condition would need to be ``i < 5;`` 

.. note:: Although ``<`` , ``>`` , ``<=``, ``>=`` are probably the most common operators used in ``for`` loops, others may be used if a programer deems fit (e.g. ``!=``). 

As long as this condition is eventually reached (in order to avoid an **ifinite loop**) it is up to you to decide what that condition will be based on the problem you want to solve. 


3. **Updating the Counter Variable** 

Finally, when writing a ``for`` loop, the last expression inside the parentheses is where you update the counter variable. In this example, we said that ``i += 1;``. This means that for each pass through the loop, ``i`` will increase by 1. If we had declared ``i`` outside of the loop and then printed the value of ``i`` after the loop, it would be 6. This is because after the last fifth "Hey you! Wake Up!! " is printed, ``i`` is incremented by 1 and becomes 6, which causes the condition ``i <= 5;`` to be ``false`` and thus end the loop. 


Lastly, there are two final notes to consider: 


* Similar to ``if``/``else`` statements, a ``for`` loop does not technically need braces if the body of the loop is only one line (like in our example). However, exercise caution when doing so. 

* Although in the given example we **increment** the **counter variable** ``i``, it is also just as acceptable/correct to **decrement** the counter variable. We could have just as easily set ``i`` equal to 5 and changed the condition to ``i >= 1`` to achieve the same end result. 


Nested ``for`` Loops
^^^^^^^^^^^^^^^^^^^^

In this brief section, we will examine **nested** ``for`` loops and their applications. The general structure of this kind of loop is shown below: 

.. code-block:: Shadow
    :linenos:

    for (int i = 5; i > 0; i -= 1) //this is the outer loop
    {
        for (int j = 5; j >= i; j -= 1) //this is the inner loop
	{
	    Console.print("@"); 
	}
	Console.printLine();  
     }

The ouput is as follows: 

.. code-block:: console

    @
    @@@
    @@@@@
    @@@@@@@
    @@@@@@@@@


There are two important aspects of the nested ``for`` loop: the **outer loop** and the **inner loop**. Let’s trace through the example to see how control flows between the outer and inner loops. 

The outer loop is the "driver" of the nested ``for`` loop. For example, the goal of the block of code above is to output a 5 ``@`` tall right triangle. Since we will need five separate lines of varying length to do so, the outer loop needs to run a total of 5 times. Thus, the statement on **Line 1** ensures that will happen. 

But how do we get the different numbers of ``@`` symbols on each of the 5 lines? That is controlled by the **inner** loop. Initially, the outer loop counter variable, ``i``,  is  equal to 5. Before ``i`` is decremented by 1, control is passed to the inner loop. ``j`` is initialized to 5, so the condition that ``j >= i;``  is ``true``. Then a ``@`` is printed and ``j`` is decremented by 1, so ``j``` is no longer greater than or equal to ``i``. Once the **inner loop** has completely executed, then control flows to the statement outside the inner loop -- the empty ``Console.printLine()`` that starts the next line of ``@``’s. (If we had forgotten **Line 7**, all the ``@``’s would have been printed on the same line). 

Now, control flows back the **outer loop**, and ``i`` is decreased by one (so now ``i`` equals 4). It is important to note that when the inner loop is executed again, it is in essence "reset", so ``j`` starts as equal to 5 and two ``*``’s will be printed before ``i >= j`` becomes ``false``. This process continues until the fifth line of 5 ``*``’s is printed and ``i`` becomes 0, which causes the program to exit the outer loop. The triangle is now complete! 

.. _switch: 

``switch`` Statements
^^^^^^^^^^^^^^^^^^^^^

We will continue this section with a discussion on ``switch`` statements, which are similar in concept to ``if``/``else`` statements but syntactically very different. 

A ``switch`` statement is useful when you have input, whether it is user or program defined, and different actions to take based on the value of the input. In other words, there are many different **cases** of input that correspond to disticnt actions. For example, say you have a ``String`` variable that holds a genre of music. There are many different genres of music: hip-hop, rock, pop, alternative, etc. These different genres are called **cases**, and based on the case given, the program will recommend a specific song (e.g. a pop song for the pop genre). This example is coded below, demonstrating the general structure of a ``switch`` statement. 

.. code-block:: Shadow
    :linenos:

    var genre = "rock"; 
    switch( genre )
    {
        case( "pop", "Pop" )Console.printLine("Listen to \"Firework\" by Katy Perry!");					
	case( "alternative" )Console.printLine("Listen to \"Call Me\" by Blondie");			
	case( "rock" )Console.printLine("Listen to \"We are the Champions\" by Queen");				
	case( "country" )Console.printLine("Listen to \"Need You Now\" by Lady Antebellum");
	case( "hip-hop/rap" )Console.printLine("Listen to \"Hey Ya!\" by Outkast");
	default Console.printLine("Hmm, we don't have recomendations for that genre.");			
    }

Here the output will be, 


.. code-block:: console

    Listen to "We are the Champions" by Queen!


Why? First consider **Line 2**. Here we see the ``switch`` statement, which is being sent the ``String`` variable genre. In general, you can use any type of variable in a ``switch`` statement. In this case, the literal value of ``genre`` will be compared to 5 different cases. These cases in **Lines 4-8** represent other possible genres of music. 

The ``switch`` statement works by going through the cases, checking to see if one of the cases matches the literal value of ``genre``, which is "rock." The program stops searching when a match is found, which is on **Line 6**. Then, the ``Console.printLine()`` statement on this same line is printed and control is passed to the next line outside of the ``switch``. 

Notice the ``default case`` on **Line 9**. If none of the cases had equaled "rock", then the ``default`` statement would have printed. However, a ``default`` **is not required.** If no cases had matched, and there was no ``default`` provided, the program would exit the ``switch`` without executing anything. 


Below are some important takeaways for ``switch`` statements. 

* Any type of variable may be used in a ``switch`` statement.
* There is no limit to the number of cases.
* A ``default`` is not required, but there can only be one. 
* ``switch`` statements may be included inside loops (usually a ``for`` or a ``while`` loop).
* You may include multiple cases in one statements e.g. ``case( 1, 2, 3 )``.
* The ``default`` does not have to be the last statement in the body of the ``switch``. 
* Enclose multiple statements for one ``case`` in braces (see below).  

.. code-block:: shadow

    var someNum = 0;
    switch (someNum) 
    {
        case(0)
        {
            Console.printLine("Uh oh your number is 0."); 
            Console.printLine("Is 0 even, odd, or neither?"); 
        }
        default
        {
            Console.printLine("Your number is not zero."); 
        }
    }


``break`` and ``continue``
^^^^^^^^^^^^^^^^^^^^^^^^^^

Two statements that can alter the flow of control in a Shadow program are ``break`` and ``continue``. These statements can be useful to either exit a loop or skip statements in the body of the loop. 

First, let’s discuss ``break``. When a program reaches a break statement, it will immediately terminate the current loop, and control will flow to the next statement outside of the loop. For example, see the short block of code below: 

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


When ``i`` is 3, the statement ``i * 2 > 5`` becomes ``true``, and the ``break`` statement is executed. Thus, the program exits the loop and control is passed to **Line 9**. It is important to note that a ``break`` statement *must* be located inside of a loop, or you will get a **compile time error**. 

**Lastly, there is the**  ``continue`` **statement**. Just like with the ``break`` statement, ``continue`` must also be placed inside of a loop to avoid a compile time error. When the program reaches a ``continue`` statement, the current iteration of the loop ends, and control flows back to the conditional statement. For example, in a ``for`` loop, any statements after ``continue`` would be skipped, and the program would go straight to the incrementation/decrementation of the counter variable. A ``while`` loop would behave in much the same way -- any statements after ``continue`` would be skipped, and control would flow to the conditional statement. 

An example of a ``while`` loop with a ``continue`` statement is provided. 


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

As seen in the program above, when ``i`` is even (i.e. when ``i % 2 == 0``), the program hits a ``continue`` statement. From there, **Lines 12 and 13** are skipped, and control flows back to the initial condition. Thus, only odd numbers are printed. 

As a final note: Although ``break`` and ``continue`` can be useful for quick solutions, it is not good programming practice to rely on them. If a ``break`` or ``continue`` statement happens to be used, there should always be another way to get to the same solution. For example, in the previous example with odd numbers, a simple ``if`` statement checking if a number is odd with ``%`` would be a valid (and more efficient) solution. 



		
	
		
