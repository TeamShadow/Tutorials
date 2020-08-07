*************************
Operators and Expressions
*************************

Assignment
==========

We touched on assigning a variable a particular value in the :ref:`Variables` tutorial. For example, consider the following line of code:  

.. code-block:: shadow 

    var height = 5.4; 

In this instance, the variable ``height`` is *assigned* the value 5.4. Another example would be:

.. code-block:: shadow

    var total = 6 + 6; 

The variable ``total`` is assigned the result of the *expression* ``6 + 6``, which is ``12``. 

While these two examples constitute the basics of assignment, Shadow also has some unique features assigning more than one value at once. 


.. code-block:: shadow 
    :linenos: 

    int x; 
    int y;
    int z; 
    (x, y) = (3, 6); 
    (x, y) = (y, x); 
    (x, y, z) = 10; 

The above section of code demonstrates a few Shadow syntactic structures: *sequences* and two of its subtypes, *swaps* and *splats*. In the first three lines of code, the variables ``x``, ``y``, and ``z``  are declared but not *initialized*. However, in **Line 4**, variables ``x`` and ``y`` are initialized in a single line using the basic sequence notation. **Line 5** is an example of a swap because now ``x`` has a value ``6`` and ``y`` has value ``3``. A swap works because all of the values on the right side are computed before they are stored on the left side. Lastly, **Line 6** is called a splat because all three variables are set to ``10`` in the same line. 

Arithmetic operators
====================


Arithmetic operators in Shadow appear mostly as they would in an elementary math class. These are the high-precedence arithmetic operators:

* ``*`` is used for multiplication
* ``/`` is used for division 
* ``%`` is used for modular division

These are the low-precedence arithmetic operators:

* ``+`` is used for addition
* ``-`` is used for subtraction


Precedence with arithmetic operators
------------------------------------

In Shadow, multiplication, division, and modulus take precedence over addition and subtraction, but you can use parentheses to group operations together. The short programs below shows basic expressions using Shadow arithmetic operators.  


First, let's examine some nuances of Shadow division. 


.. code-block:: shadow
	
	import shadow:io@Console;  

	class OperatorsExamples
	{
		public main( String[] args ) => () 
		{
			/*
			 * When using / for division, if either the operator or operand is a
			 * double, the result will be a double (double division). 
			 */
			var divide = 7.0 / 2; 
			Console.printLine("Result 1: " # divide);
			
			/* 
			 * If the operator and operand are both ints, the result will 
			 * be an integer with everything after the decimal point cut off. 
			 */
			var divide2 = 7 / 2; 
			Console.printLine("Result 2: " # divide2);
			
			/* 
			 * Although both the operator and operand are ints, the variable
			 * divide3 is a double. What happens? First, the expression to the
			 * right of the equals sign is evaluated. Since both numbers are
			 * ints, the result is also an int: 3. Assignment happens second.
			 * Shadow recognizes that the result must be stored as a double, so
			 * now divide3 holds the value 3.0, not 3.5 as some would expect. 
			 */
			double divide3 = 7 / 2; 
			Console.printLine("Result 3: " # divide3); 	 
		 }
	}


Below is the console output for the above program: 

.. code-block:: console
    
	Result 1: 3.5
	Result 2: 3
	Result 3: 3.0

.. warning:: You will cause a compile error if you try to store the result of ``double`` division in an ``int``. 

The program below provides a few extra examples of using the arithmetic operators. 

.. code-block:: shadow 

	import shadow:io@Console;  

	class ArithmeticOperators
	{
		public main( String[] args ) => () 
		{	
			// Order of operations: (6/3) == 2; (2*2) == 4; (1+4) == 5
			// expression1 == 5
			var expression1 = 1 + 6 / 3 * 2; 

			// expression2 == 0
			var expression2 = 10 % 2; 
			
			// expression3 == 1 
			var expression3 = 10 % 3; 			
		}
	}


.. note:: Modular division is useful when trying to determine if a number is even or odd. 


Negation
--------

In addition to being used for subtraction, the ``-`` operator can also be used for negation of a single item as shown below.

.. code-block:: shadow
    
    var x = 6; 
    x = -x; // Now the variable x holds the value -6 
	
When an operator can be used between two operands, it's called a *binary* operator (which has nothing to do with binary numbers).  When an operator can be used with only a single operand, it's called a *unary* operator.  In this case, the ``-`` operator has both binary and unary forms.


Relational operators
====================

Relational operators in Shadow are used to make comparisons and evaluate to one of two values: ``true`` or ``false``. See the list below.

* ``==`` equal to
* ``!=`` not equal to
* ``>`` greater than 
* ``<`` less than
* ``>=`` greater than or equal to
* ``<=`` less than or equal to


A note on ``==``
----------------

When comparing two numeric values, ``==`` works in the way you would expect. For example:

.. code-block:: shadow 

    var test = (6 == 6); 

The variable ``test`` is assigned ``true``. However, suppose you wanted to compare two ``String`` variables using ``==``. What would the result be?  Consider: 

.. code-block:: shadow 

    var want = "coffee"; 
    var need = "coffee";
    var compare = (want == need); 
    Console.printLine(compare); 

Here, the variables ``want`` and ``need`` both are equal to the literal ``String`` value ``"coffee"``, so the result is ``true``. While the ``==`` compares values, Shadow also has the ``===`` operator which compares *references*. Let's say we assign ``want`` and ``need`` to new ``String`` objects (see :ref:`Classes` for more on objects) that both contain the same value: 

.. code-block:: shadow 

    want = String:create("coffee");
    need = String:create("coffee");

    Console.printLine(want === need); 

Although their contents are the same, ``false`` is printed because the variables now point to two distinct objects. 

The following short program provides examples and explanations for the remaining relational operators. 

.. code-block:: shadow

	import shadow:io@Console;  

	class Comparisons
	{
		public main( String[] args ) => () 
		{ 
			/* 
			 * The following code illustrates the use of "not equal to", or !=. 
			 * You may use this operator to compare Strings or numeric values (and 
			 * even objects). If the values being compared are not equal, 
			 * "true" is returned. 
			 */

			var sport1 = "polo"; 
			var sport2 = "water polo";
			// Should print true, as sport1 and sport2 are not equal. 
			Console.printLine("Polo is NOT the same as water polo: " # (sport1 != sport2)); 
			
			/* 
			 * The following code uses >= to make comparisons. Using >, <, and <=
			 * follows the same guidelines as shown below. If the the variable 
			 * yourAge is greater than or equal to myAge, true will be printed.
			 */
			var myAge = 20; 
			var yourAge = 19; 
			// Should print false, as 19 is NOT >= 20
			Console.printLine("You are older or the same age as me: " # (yourAge >= myAge));
			
			/* 
			 * Note: When you compare Strings with these relational operators, 
			 * they are compared lexicographically, meaning with a dictionary ordering.
			 */ 
			
			// Should print true, as "a" comes before "b" in the dictionary
			Console.printLine("a is less than b: " # ("a" < "b"));
		}
	}

The console output is here for reference. 

.. code-block:: console

    Polo is NOT the same as water polo: true
    You are older or the same age as me: false
    a is less than b: true 

Logical operators
=================

Logical operators in Shadow, like relational operators, evaluate to either ``true`` or ``false`` when used in expressions. They are commonly used in ``if``/ ``else`` statements, which are discussed in the :ref:`next tutorial <Flow Control and Looping>`. See below for a list of logical operators: 

* ``and``
* ``or``
* ``xor`` 
* ``!``

When two ``boolean`` values are combined with ``and``, the result is ``true`` if and only if both the values are ``true``.  When two ``boolean`` values are combined with ``or``, the result is ``true`` if either (or both) the values are ``true``.  When two ``boolean`` values are combined with ``xor``, the result is ``true`` if the two values are different (one ``true`` and the other ``false``).  The ``!`` operator is a unary operator that logically negates its operand, turning ``true`` to ``false`` and vice versa.  

The following basic program outlines how to use these logical operators: 

.. code-block:: shadow

	import shadow:io@Console;  

	class LogicalOperators
	{
		public main( String[] args ) => () 
		{ 
			/* 
			 * As seen below, in order for the expression "withCream and !withSugar" 
			 * to evaluate to true, each operand must also be true. In this case, we 
			 * can see that withCream was assigned true and withSugar is assigned
			 * false but negated. Since both operands are true, the output "I like my
			 * coffee with cream but NOT sugar!" is printed.
			 */
			var withCream = true; 
			var withSugar = false; 
			
			if(withCream and !withSugar) 
				Console.printLine("I like my coffee with cream but NOT sugar!");
			
			/* 
			 * In order for the expression "withCream or withSugar" to evaluate to
			 * true, only one of the operands needs to be true. Although withSugar is
			 * assigned false, withCream is declared true, so the statement "I like
			 * cream OR sugar in my coffee. Surprise me!" is printed. 
			 */
			if(withCream or withSugar) 
				Console.printLine("I like cream OR sugar in my coffee. Surprise me!");
		}    	      
	}

Although the program outlines their basic functionality, there are a few more points to note when dealing with complex expressions of logical operators. 

* ``and`` takes precedence over ``xor``, ``xor`` takes precedence over ``or``, and ``!`` takes precedence over all of them.
* It's legal to have an expression with more than one ``and``, ``or``, or ``xor``. When mixing logical operators, it's wise to use parentheses to make your meaning clear. 
* If you have an expression with ``and`` and the first part evaluates to ``false``, Shadow performs *short circuit evaluation*. In this situation, the second part will not even be evaluated because the whole thing will be ``false``.  If the second part contains a method, it will not be called.  The same idea applies to ``or`` when the first part evaluates to ``true``.

Combined assignment operators
=============================

In addition to ``=``, there are a handful of other operators that give shortcuts for another operation combined with assignment. See the list below: 

* ``+=``
* ``-=``
* ``*=``
* ``/=``
* ``%=``
* ``#=``

Each of these operators performs the operation (``+``, ``-``, ``*``, ``/``, ``%``, or ``#``) with the values on the left and right sides of the operator and the assigns the result to the variable on the left.

.. code-block:: shadow
	:linenos:

	var x = 10; 
	x %= 2;		//Now x == 0  

	var y = 10; 
	y = y % 10;	// Now y == 0 


Although **Lines 2** and **5** effectively do the same thing, line 2 is shorter way to write the operation followed by assignment.

.. note:: The ``++`` and ``--`` operators used in Java and C-family languages to increment and decrement variables do not exist in Shadow.  Instead, you can use ``+= 1`` and ``-= 1``, respectively, to achieve the same effects.


Cat operator
============

As mentioned in the earlier :ref:`Declaring variables` section, ``#`` is called the *cat* operator in Shadow. It's Shadow's version of the concatenation operator. 

The purpose of ``#`` is to concatenate values with ``String`` values. For example, we can use ``#`` to combine the values of variables with formatting text in ``Console.printLine()`` statements. Another example is below. It's important to note that this operator has a lower precedence than addition. In other words, the addition ``1 + 1`` will happen before the result is combined into a ``String`` with ``#``. 

.. code-block:: shadow

    var name1 = "R"; 
    var name2 = "D"; 
    Console.printLine(name1 # 1 + 1 # name2 # 2);

When the program runs, ``R2D2`` will be displayed on the console.  

You can also use a unary form of ``#`` by putting it in front of any value, which will call its ``toString()`` method. Take this example:

.. code-block:: shadow

	String number = #25;
  
Now, ``number`` contains a ``String`` with the value ``"25"``.






















