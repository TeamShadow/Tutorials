************************
Reading from the Console
************************

When writing programs, we often want to prompt the user to input a text or numerical value. Let's look at the ways to read text first.

Reading text
============

There are four fundamental methods used for reading characters and text as seen in the list below: 

* ``readByte()``, which returns the next ``ubyte``
* ``readCode()``, which returns the next character as a ``code``
* ``readString()``, which returns the next whitespace-delimited text 
* ``readLine()``, which returns the next line of text

The first two methods are relatively low-level, reading individual bytes or characters of text at a time.  You will usually read a whole word or an entire line at once.

All four methods also return a ``boolean`` value that indicates if the end of the file being read from has been reached or not. This value can often be ignored for user input, as it will never be true when reading input from the keyboard.


Reading a word
--------------

Now, let's analyze an example: 

.. code-block:: shadow
    :linenos: 
	
    public main( String[] args ) => () 
    {
        Console.print("Enter your zodiac sign: "); 
		(String sign, ) = Console.readString(); 
        Console.printLine("Your zodiac sign is " # sign # "!"); 	
    }
	
Here is the output if a user entered ``Aquarius``.

.. code-block:: console 

    Enter your zodiac sign: Aquarius
    Your zodiac sign is Aquarius!


As you can see on **Line 3**, it's helpful to prompt the user for input before trying to read any.  Otherwise, the program will simply sit there, waiting for input while the user is waiting for information from the program. In this case, we ask the user to enter their zodiac sign. On **Line 4** the program reads the input and stores it into a ``String`` variable. 

As discussed in the :ref:`Methods tutorial <Methods>`, methods in Shadow can return multiple values. Since the ``readString()`` method returns both a 	``String`` value and a ``boolean``, we can type ``(String sign, )`` with an empty space for the second return value to indicate we want to ignore it. \Once the user types in their answer and hits the enter key, the value is stored in ``sign``. Then, we can use the variable as we choose -- printing it out on **Line 5** in our case. 

Reading a whole line
--------------------

Although the ``readString()`` and ``readLine()`` methods both return a ``String``, the ``readLine()`` method will read an entire line of text (including spaces) while the ``readString()`` method will read everything up to the first space, tab, new line, or line feed character it reaches. Thus, in the previous example, if the user entered ``Aquarius I think`` as their zodiac sign, the variable ``sign`` would only contain ``"Aquarius"``.

In some cases, like when reading a sentence, it might be valuable to read a whole line.  The syntax is the same as reading a single word, with the substitution of ``readLine()`` for ``readString()``:

.. code-block:: shadow
	
    public main( String[] args ) => () 
    {
		Console.print("Enter your first and last name: ");
		(String name, ) = Console.readLine();
        Console.print("Enter a line of Shakespeare: "); 
		(String line, ) = Console.readLine();
		if(line == "To be, or not to be, that is the question:")
			Console.printLine(name # " likes Hamlet!");
		else
			Console.printLine(name # "'s knowledge of the Bard transcends Hamlet.");
    }
	
Here is the output if a user named David Bowie entered ``Now is the winter of our discontent``.

.. code-block:: console 

	Enter your first and last name: David Bowie
    Enter some Shakespeare: Now is the winter of our discontent
    David Bowie's knowledge of the Bard transcends Hamlet.
	
.. note:: Some programmers can become frustrated when mixing calls to ``readLine()`` with calls to ``readString()``.  The ``readString()`` method will ignore whitespace until it reaches real characters, read the characters, and then *stop* before the next whitespace.  However, the ``readLine()`` method will read in everything and *consume* the newline at the end of the line.  This means that using ``readString()`` to read in a name, for example, might leave a newline after the name still waiting to be processed.  In that case, calling ``readLine()`` immediately afterward will return the empty ``String`` (``""``) because there are no characters left before the end of the line.  When mixing ``readLine()`` with ``readString()`` (or the numerical input methods described below that internally call ``readString()``), it's sometimes necessary to add an extra ``readLine()`` after other input methods before trying to read a line of real input.
	

Reading numeric values
======================

Programs often need to read numeric input from a user.  Using the methods covered above, it is possible to read in a ``String`` and convert it to an ``int``, ``double``, or other numeric type.  For convenience, however, two ``Console`` methods have been created that do this process for you:

* ``readInt()``, which returns the next whitespace-delimited text, converted to an ``int``
* ``readDouble()``, which returns the next whitespace-delimited text, converted to a ``double``

Below is any example of how this can be done: 

.. code-block:: shadow
  
    Console.print("How much wood would a woodchuck chuck? ");
    var wood = Console.readInt(); 

If you wanted to read a ``double`` value, simply replace ``readInt()`` with ``readDouble()``.

.. note:: If the next whitespace-delimited piece of text is not a correctly formatted representation of ``int`` or ``double`` (depending on which method you're using), the method will throw a ``NumberFormatException``.

Example reading both text and numbers
-------------------------------------

What if you wanted to create a program that calculates someone's BMI? For formatting purposes, you can prompt for their name. Then, you would need to ask the user their height in inches and their weight in pounds. After storing these values in separate variables, you would be able to perform calculations to output their BMI.  For maximum accuracy, we'll read the height as a ``double``.  Below is a segment of code that performs these steps:

.. code-block:: shadow

	Console.print("Enter your first and last name: ");
	(String name, ) = Console.readLine();
	Console.print("Enter your height in inches (with up to two decimal places of accuracy): "); 
	double height = Console.readDouble();
	Console.print("Enter your weight in pounds: ");
	int weight = Console.readInt();
	double bmi = 703.0 * weight / (height * height); // Formula for BMI
	Console.printLine(name # " has a BMI of " # bmi # ".");
	
Sample output for Ryan Gosling follows.  He is reported to be 6 feet tall and to weigh 180 pounds.

.. code-block:: console

	Enter your first and last name: Ryan Gosling
	Enter your height in inches (with up to two decimal places of accuracy): 72.0
	Enter your weight in pounds: 180
	Ryan Gosling has a BMI of 24.40972222222222.
	

