*********
Variables
*********

A key concept common in almost every programming language is *variables*. Just like in mathematics where you might say 3\ *x* = 24 (where *x* is a variable equal to 8), variables in Shadow hold values. However, unlike in mathematics (where variables have fixed and sometimes unknown values), Shadow uses *imperative assignment*. This means that when a variable is *assigned*, its value (or what it points at) changes. 

Numeric types
=============

Key *numeric type* variables, which are examples of *primitive variables*, are listed with their sizes and ranges below:

+----------------------------+------------------------+----------------------------+-------------------+
|                                            Signed Types                                              |
+=========+==================+========================+============================+===================+
| **Type**|**Size (Bytes)**  |    **Minimum Value**   |   **Maximum Value**        |**Example Literal**|
+---------+------------------+------------------------+----------------------------+-------------------+
| ``byte``|     1            |          -128          |         127                |       ``64y``     |
+---------+------------------+------------------------+----------------------------+-------------------+
|``short``|     2            |         -32768         |        32767               |      ``1000s``    |
+---------+------------------+------------------------+----------------------------+-------------------+ 
| ``int`` |     4            |      -2147483648       |      2147483647            |       ``15``      |
+---------+------------------+------------------------+----------------------------+-------------------+       
| ``long``|     8            |  -9223372036854775808  |  9223372036854775807       |       ``0L``      |
+---------+------------------+------------------------+----------------------------+-------------------+

The rightmost column of this table shows example *literals* for each of these types.  A literal is a concrete value stored into a variable.  In Shadow, ``int`` literals are written as regular numbers (optionally marked with an ``i`` at the end), but literals for the ``byte``, ``short``, and ``long`` types are marked with an uppercase or lowercase ``y``, ``s``, or ``L``, respectively, at the end of the literal.

In addition to integer types, Shadow also has two types of primitive variables for storing *floating-point values* like 98.6 or -204.418: ``double`` and ``float``.  Typically, ``double`` is the appropriate type for floating-point values, since it has much more precision than ``float``.  If you want to use literals of type ``float``, write them ending in ``f`` or ``F``, as in ``98.6f``.  Floating-point values can be written in scientific notation for especially large or especially small numbers.  For example ``6.02E23`` means 6.02 × 10\ :superscript:`23` .

.. warning:: Neither integer nor floating-point literals should be written with commas to separate multiples of 1,000 as is typically done in mathematics.  For example, the number 3,238,461 must be written ``3238461`` in Shadow.

Unlike Java, Shadow has *unsigned types* for primitive variables as well. For example, the unsigned version of ``int`` is ``uint``. Unsigned values can never be negative. Due to strict Shadow type-checking, explicit :ref:`casting <Primitive casting>` is needed if you want to store an ``uint`` in an ``int`` or vice versa.  Exercise caution when using unsigned variables because their behavior can be unexpected when the value would normally become negative.

.. note:: There is no ``udouble`` or ``ufloat`` type!


+-----------------------------+------------------------+-------------------------+
|                               Unsigned Types                                   |
+==========+==================+========================+=========================+
| **Type** |**Size (Bytes)**  |  **Maximum Value**     |**Example Literal**      |
+----------+------------------+------------------------+-------------------------+
|``ubyte`` |     1            |          255           |         ``128uy``       |      
+----------+------------------+------------------------+-------------------------+
|``ushort``|     2            |         65535          |         ``1000us``      |      
+----------+------------------+------------------------+-------------------------+
| ``uint`` |     4            |      4294967295        |          ``15u``        |    
+----------+------------------+------------------------+-------------------------+    
| ``ulong``|     8            |  18446744073709551615  |          ``0uL``        |
+----------+------------------+------------------------+-------------------------+


As an example, a simple variable declaration of type ``int`` looks like this: 

.. code-block:: shadow

    int age = 20; 

The variable ``age`` is of primitive type ``int`` and holds the literal value ``20``. If you had a birthday and wanted to update your age, you could write the following line of code: 

.. code-block:: shadow

    age = 21; 

Now, the variable ``age`` is updated and holds the literal value ``21``. Notice that you would **not** write :

.. code-block:: shadow

    int age = 21; 

This code would not compile because the ``age`` variable is already declared and **cannot be declared twice**. You are not trying to create a new ``age`` variable; you are simply changing its value. 

The ``boolean`` type
====================

Outside of the numeric primitive variables, there is a type called ``boolean``.  A ``boolean`` variable can hold one of two values -- ``true`` or ``false``. 

For example, 

.. code-block:: shadow

    boolean isBeautiful = true; 

The variable ``isBeautiful`` is of primitive type ``boolean`` and holds the literal value ``true``. It might seem strange to use a whole type just to hold ``true`` and ``false``, but such a type can be useful when making choices or repeating an action, as discussed in :ref:`Flow Control and Looping`.

The ``code`` type
=================

There is one other primitive type: ``code``. Similar to ``char`` in Java, a ``code`` represents a single character.  The declaration of a ``code`` variable is as follows: 

.. code-block:: shadow

	code grade = 'd';

The variable ``grade`` is of primitive type ``code`` and holds the literal value ``'d'``.  Make sure you put the character in single quotes in order for it to be recognized as a ``code``. 

If you're familiar with Java, you may be wondering how ``code`` is different from ``char``. It all comes down to Unicode, which is a collection of standards for encoding characters. Java uses the UTF-16 standard, meaning that each character is represented using two bytes, while Shadow uses UTF-8, which is a variable-size encoding. Even though a variable number of bytes are used, a single ``code`` variable always takes up four bytes in order to ensure the largest characters can be stored in it.  When a group of characters is stored in a ``String``, however, they only use as many bytes as needed. 

.. note:: ``code`` characters do not have to be letters. They could be digits, punctuation, or special characters like ``'$'``. 

The ``String`` type
===================

The ``String`` type is not a primitive type, but it is still fundamental to Shadow programming.  While a ``code`` value holds exactly one character, a ``String`` can hold a list of characters.  This list can be as short as no characters -- what is called the empty ``String``, written ``""`` -- or as long as millions of characters.

In other words, the ``String`` type is used to hold arbitrary amounts of text.  Note that ``code`` literals are marked with single quotes (``'``), but ``String`` literals are marked with double quotes (``"``), as show below.

.. code-block:: shadow

    String name = "Olivia"; // You must put the characters in double quotes

Unlike an ``int`` or ``double`` variable, a ``String`` variable holds a *reference* (a location in memory) pointing at an object.  Thus, two or more different ``String`` variables could point at the same ``String`` object.  Every reference type (which is any type other than the 12 primitive types) behaves in this way.


Declaring variables
===================

The following short example program demonstrates basic principles for declaring and assigning variables, as well as some information on formatting output with ``Console.printLine()``.


.. code-block:: shadow
 
    import shadow:io@Console;  

    /* This is a short program that demonstrates how to the declare the variable 
     * types defined above. 
     */

    class VariableExample
    {
		public main( String[] args ) => () 
		{	
			String restaurantName = "Taco Tuesday"; 
			boolean isHungry = true; 
		
			String meal = "Meat and Bean Burrito"; 
			int quantity = 2; 
			double price = 5.50; 
			
			Console.printLine("I love eating at " # restaurantName # "."); 
			Console.printLine("I would like " # quantity # " " # meal # "(s).");  
		}
	
    }

The output is as follows: 

.. code-block:: console

    I love eating at Taco Tuesday.
    I would like 2 Meat and Bean Burrito(s).


Let's consider a few different Shadow features and conventions demonstrated by this program.

Camel case notation
-------------------

.. code-block:: shadow

    String restaurantName = "Taco Tuesday"; 
    boolean isHungry = true; 

Note how these variables are named. For example, ``restaurantName`` is a ``String`` variable. We did not name it ``RestaurantName`` or ``restaurantname``. Although using these names would not cause a compiler error, it is good programming practice to use *camel case* notation in which the first word in a variable name begins with a lowercase letter and the rest begin with uppercase letters. This practice is used in Shadow because variable names **cannot** contain spaces, so capitalization is used to make each word in the variable name distinct. The ``boolean`` variable ``isHungry`` is declared in the same way. In addition to using camel case notation, make sure your variable names are descriptive of their purpose. In this case, if this was a program for a restaurant, ``isHungry`` might be used to tell if a certain customer is hungry. 
  
.. warning:: Your code will not compile if you have spaces in variable names, such as ``restaurant name``.
 
More naming conventions
-----------------------

.. code-block:: shadow

    String meal = "Meat and Bean Burrito"; 
    int quantity = 2; 
    double price = 5.50; 

There are a few more key naming conventions for Shadow. 

* Starting a variable name with a digit will cause a compiler error, but using digits after the first letter is acceptable. 
* Single-word names should be all lowercase (``price``, ``meal``, or ``quantity``), but is not a compiler error to do otherwise.
* Using other symbols in variable names (``#``, ``_``, ``@``, ``%``, ``+``, etc.) will cause a compiler error.
* Variable names cannot be reserved words (see :ref:`next section<Reserved Words>`). 


Formatting output
----------------- 

.. code-block:: shadow 

    Console.printLine("I love eating at " # restaurantName # "."); 
    Console.printLine("I would like " # quantity # " " # meal # "(s).");
    
``Console.printLine()`` is used to display text on the console. Literal text goes inside quotations marks (``" "``), but you are able to print variable values as well. If you want to join together text with the values of variables, you can use the cat operator (``#``) to do so.  As seen above, ``"I love eating at " # restaurantName # "."`` joins together the ``String`` literal ``"I love eating at "`` with the contents of the variable ``restaurantName`` and finally joins the short ``String`` literal ``"."`` to the end of the result.

Later, you could change the value of ``restaurantName`` as follows:

.. code-block:: shadow

    restaurantName = "Taco Wednesday"; 

Then, using ``Console.printLine("I love eating at " # restaurantName # ".");`` will output ``I love eating at Taco Wednesday.``  


Reserved words
==============

In Shadow, as with most programming languages, there are *reserved words*. Reserved words inherently have meaning in Shadow. For example, ``double`` is a reserved word because Shadow recognizes this as a primitive type -- it has meaning. Thus, you will get a compiler error if you try to name a variable with a reserved word. See the chart below for a full list of reserved words in Shadow. 


+-------------+-------------+-------------+--------------+-------------+-------------+-------------+  
|``abstract`` |``and``      |``assert``   |``boolean``   |``break``    |``byte``     |``case``     |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+ 
|``cast``     |``catch``    |``check``    |``class``     |``code``     |``constant`` |``continue`` |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+ 
|``copy``     |``create``   |``default``  |``destroy``   |``do``       |``double``   |``else``     |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+
|``enum``     |``exception``|``false``    |``finally``   |``float``    |``for``      |``foreach``  |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+ 
|``freeze``   |``get``      |``if``       |``immutable`` |``import``   |``in``       |``int``      |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+ 
|``interface``|``is``       |``locked``   |``long``      |``null``     |``nullable`` |``or``       |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+         
|``private``  |``protected``|``public``   |``readonly``  |``receive``  |``recover``  |``return``   |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+     
|``send``     |``set``      |``short``    |``singleton`` |``skip``     |``spawn``    |``super``    |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+
|``switch``   |``this``     |``throw``    |``true``      |``try``      |``ubyte``    |``uint``     |
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+       
|``ulong``    |``ushort``   |``var``      |``weak``      |``while``    |``xor``      |             | 
+-------------+-------------+-------------+--------------+-------------+-------------+-------------+


The ``var`` keyword
===================

In all examples in this section, the variables are declared with an explicit type and name. Like C# (and similar to the ``auto`` keyword in C++11), Shadow provides a ``var`` keyword that can be used to declare local variables as long as they are assigned an initial value. This can be done because a variable's type is generally obvious, and the compiler will not confuse a ``double`` value with a ``String``. 

.. code-block:: shadow

    var milesRun = 26.2; 
    var marathonCity = "Boston" 

As you can see, ``milesRun`` is clearly a ``double``, and ``marathonCity`` is a ``String``. Going forward with the tutorials, variables will usually be declared using ``var`` in examples.  Note that there is no type ``var``!  The variable ``milesRun`` has type ``double``, but the programmer used ``var`` as a shorthand instead of stating the type explicitly.


Primitive casting
=================

Shadow is a *strongly typed* language, which means that it usually isn't possible to store values of one type into variables of a different type.  For example, it's not permitted to store a ``double`` value like ``8.316`` into an ``int`` variable.  The compiler shows an error if you try to do this because you'd lose the digits after the decimal point.

There are exceptions to this rule.  It's legal to store a narrower type into a broader type.  In other words, you *could* store an ``int`` value like ``-37`` into a ``double`` variable.  The ``double`` type is broader than the ``int`` type, so there's no risk you'll lose information.

There are, however, situations where you have a broader type and *need* to store it into a variable of a narrower type.  In these situations, Shadow provides a tool called *casting* that allows you to change the type of an expression into a different type.  By using the ``cast`` keyword, you are overriding the rules of Shadow, so there are risks that you will lose information or end up with a value whose meaning is different.

The syntax for casting is as follows:

.. code-block:: shadow 

	cast<resultType>(expression)
	
The ``resultType`` is the type you want to change ``expression`` to.

Numeric casting
---------------

Consider the short segment of code below: 

.. code-block:: shadow 
    :linenos: 

    double a = cast<double>(8); 
    Console.printLine(w); 
    double b = 8; 
    Console.printLine(x);

**Lines 2 and 4** both print ``8.0`` to the console. In both cases, we're converting the ``int`` value ``8`` into the ``double`` value ``8.0``.  On **Line 1** we're performing an *explicit cast* by using the cast syntax shown above, using the ``cast`` keyword.  On **Line 3**, we're using an *implicit cast* where Shadow automatically converts the ``int`` value into a ``double`` value, because it knows that no data will be lost.

Now, let's look another example: 

.. code-block:: shadow 
    :linenos: 
    
    int x = cast<int>(8.7); 
    Console.printLine(y); 
    
    int y = 8.0;

On **Line 1** of this code segment, we're using an explicit cast to convert the ``double`` value ``8.7`` to an ``int`` value.  **Line 2** will print ``8`` to the console because the conversion *truncates* the value instead of rounding it.

.. note:: If you want to round a ``double`` value instead of truncating it, you must call its ``round()`` method before coverting to an ``int``.

**Line 3** of this code segment, however, doesn't work.  Mathematically, there's no difference between 8.0 and 8, but for Shadow, ``8.0`` is a ``double``, which can't be stored into an ``int`` variable without an explicit cast.  Storing a signed type into an unsigned type will also always require an explicit cast, and storing an unsigned type into a signed type will require one unless the signed type is large enough to hold the unsigned type without overflowing.

Casting ``code`` values
-----------------------

Both a ``code`` and an ``int`` are stored as 4-byte quantities inside the computer.  However, the compiler treats these values differently, as either a character or an integer. 

Consider the code below: 

.. code-block:: shadow 
 
	var digit = '7'; 
    var number = cast<int>(digit); 
    Console.printLine(number); 

In this example, we are casting the ``code`` ``'7'`` into an  ``int`` and storing it in ``number``. You might expect that ``number`` now holds the numeric value ``7``, but it actually holds ``55``. The *character* ``'7'``, when converted to a number, is ``55``. Programmers rarely need to know the numerical values of characters, but it is possible to look them up in `Unicode reference documentation <https://en.wikipedia.org/wiki/List_of_Unicode_characters>`__.

A similar issue applies when converting an ``int`` to a ``code`` as in this example:
	
.. code-block:: shadow 

	var anotherNumber = 97; 
    var letter = cast<code>(anotherNumber); 
    Console.printLine(anotherNum2); 

The character corresponding to the numeric value ``97`` is ``'a'``, so ``a`` is what's printed to the console. Always be careful and intentional when casting between primitive types. 

.. note:: You may *not* cast a ``String`` to a ``code`` or vice versa.

It can be useful to remember that the numerical values of the uppercase Latin letters ``'A'`` through ``'Z'`` are sequentially numbered.  Thus, the value of ``'B'`` is larger than the value of ``'A'`` by exactly 1, and the value of ``'C'`` is larger than the value of ``'A'`` by exactly 2.  Similarly, the lowercase Latin characters ``'a'`` through ``'z'`` are also sequentially numbered (and are, perhaps strangely, larger than the values of the uppercase Latin letters).  Finally, the numerical values of the digits ``'0'`` through ``'9'`` are also sequentially numbered.  Using ``if`` statements, which will describe in a :ref:`future tutorial <Flow Control and Looping>`, a programmer can employ this knowledge to see if a particular character belongs to one of these three categories.

.. code-block:: shadow

    public printCharacterType(code character)
	{
		if(character >= 'A' and character <= 'Z')
			Console.printLine("Uppercase"); 
		else if(character >= 'a' and character <= 'z')
			Console.printLine("Lowercase"); 
		else if(character >= '0' and character <= '9')
			Console.printLine("Digit"); 
		else
			Console.printLine("Something else"); 
	}

``nullable`` and ``check``
==========================

To conclude this section on variables, we'll mention the ``nullable`` modifier and the associated ``check`` command. Many programming languages like C, C++, and Java allow reference types, including ``String``, to be assigned the special value ``null``, which means that the reference isn't pointing at any object. However, those who are familiar with such languages will know that ``null`` can cause many unintended errors in a program, leading to a ``NullPointerException`` in Java, for example. Shadow deals with this issue with the ``nullable`` modifier. If a reference is marked as ``nullable``, it means that it's able to store the value ``null``. For example:

.. code-block:: shadow 

	nullable String word = null;

The variable ``word`` is a ``nullable`` ``String`` reference that contains ``null``.  However, what if we tried to write a similar assignment without the ``nullable`` keyword?

.. code-block:: shadow 

	String word2 = null;

This assignment would cause a compiler error because ``word2`` is a non-``nullable`` reference. Although creating ``nullable`` references can circumvent some issues with using ``null``, the goal is to have as few ``nullable`` references as possible -- using them only when absolutely necessary.

Since you cannot store a ``nullable`` reference into a regular reference or call any methods on it, we use the ``check`` command to convert a ``nullable`` reference into a regular reference. The ``check`` command takes one ``nullable`` expression as a parameter and returns a non-``nullable`` object. For example, consider the following lines of code:

.. code-block:: shadow

    nullable String hint =  "machine";
    String mystery = check(hint);
 
What's stored in the non-``nullable`` ``String`` variable ``mystery``? The literal value ``"machine"``. The ``check`` command took in the ``nullable`` variable ``hint`` and returned a non-``nullable`` version of it. But what would have happened if ``hint`` had contained ``null``? The program would have crashed with an error, displaying ``shadow:Standard@UnexpectedNullException`` on the console. Exceptions will be covered in a :ref:`later tutorial<Exceptions>` where we will also show how to create a block of code to handle a ``nullable`` variable in a safe way.