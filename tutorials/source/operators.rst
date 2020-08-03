Operators and Expressions
-------------------------

Assignment
^^^^^^^^^^

In the :ref:`Variables Introduction<Variables Introduction>` page, assigning a variable a particular value is briefly touched on. For example, consider the following line of code:  

.. code-block:: shadow 

    var height = 5.4; 

In this instance, the variable ``height`` is *assigned* the value 5.4. Another example would be 

.. code-block:: shadow

    var total = 6 + 6; 

The variable ``total`` is *assigned* the result of the evaluated **expression** ``6 + 6``, which is 12. 

While these two examples constitute the basics of assignment, Shadow also has some unique features that help streamline the more complicated examples of assignment. See below. 


.. code-block:: shadow 
    :linenos: 

    var x; 
    var y;
    var z; 
    (x, y) = (3, 6); 
    (x, y) = (y, x); 
    (x, y, z) = 10; 

The above section of code demonstrates a few Shadow syntactic structures: **sequences** and two of its subtypes, **swaps** and **splats**. In the first three lines of code, the variables ``x``, ``y``, and ``z``  are declared but not **initialized**. However, in **Line 4**, variables ``x`` and ``y`` are initiated in a single line. This is a basic **sequence**. **Line 5** is an example of a **swap** because now ``x`` has a value 6 and ``y`` has value 3. Lastly, **Line 6** is called a **splat** because all three variables are set to 10 in the same line. 

Arithmetic Operators
^^^^^^^^^^^^^^^^^^^^ 


Arithmetic operators in Shadow appear mostly as they would in an elementary math class. See the list below (in order of precedence).

* ``*`` is used for multiplication
* ``/`` is used for division 
* ``%`` is used for modular division
* ``+`` is used for addition
* ``-`` is used for subtraction


**Precedence with Arithmetic Operators Examples**

In Shadow, multiplication and division take precedence over addition and subtraction. In order to avoid unintended output, it is good programming practice to use parentheses to manipulate the order of operations. The short programs below shows basic expressions using Shadow arithmetic operators.  


First, let's examine some nuances of **Shadow division**. 


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;  

    class OperatorsExamples
    {
	 public main( String[] args ) => () 
         {
	 	
	     /*
              * When using the "/" for division, if either the operator or operand is a 
	      * double, the result will be a double (double division). 
              */
             var divide = 7.0 / 2; 
	     Console.printLine("Result 1: " # divide); 
	 	
	 	
	     /* 
              * If the operator and operand are both ints, then the result will 
	      * by a non-rounded whole number (decimal point is "cut off"). 
	      */
             var divide2 = 7 / 2; 
	     Console.printLine("Result 2: " # divide2); 
	 
	 	
	     /* 
              * Although both the operator and operand are ints, the variable
	      * divide3 is a double. What happens? First, the expression to the right 
	      * of the equals sign is evaluated. Since both numbers are ints, 
	      * the result is also an int: 3. Assignment happens SECOND. Shadow recognizes
	      * that the result must be stored as a double, so now divide3 holds the value 3.0, 
	      * not 3.5 -- which is a common mistake. 
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
    
    

.. note:: You will cause a compile error if you try to store the result of ``double`` division in an ``int``. 

Lastly, this program below provides a few extra examples of using the arithmetic operators. 

.. code-block:: shadow 
    :linenos:

    import shadow:io@Console;  

    class ArithmeticOperators
    {
	public main( String[] args ) => () 
	{
	    var expression1 = 6 / 3 * 2 + 1; 
	    //expression1 = 5
	    //Evaluated from left to right: (6/3) = 2; (2*2) = 4; (4+1) = 5  
		
	    var expression2 = 10 % 2; 
	    //expression2 = 0
		
	    var expression3 = 10 % 3; 
	    //expression3 = 1 
	}
    }


.. note:: Modular division is useful when trying to determine if a number is even or odd. 

Relational Operators
^^^^^^^^^^^^^^^^^^^^

Relational operators in Shadow are used to make comparisons and when used in expressions, evaluate to one of two values: ``true`` or ``false``. See the list below (in order of precedence)

* ``==`` "equal to". *See note below.*
* ``!=`` "not equal to" 
* ``>`` "greater than" 
* ``<`` "less than"
* ``>=`` "greater than or equal to" 
* ``<=`` "less than or equal to" 


**A note on** ``==``

When comparing two numeric values, ``==`` works in the way you would expect. For example, 

.. code-block:: shadow 

    var test = (6 == 6); 

The variable ``test`` is assigned ``true``. However, suppose you wanted to compare two ``String`` variables using ``==``. What would the result be?  Consider: 

.. code-block:: shadow 
    :linenos:

    var want = "coffee"; 
    var need = "coffee";
    var compare = (want == need); 
    Console.printLine(compare); 

Here, the variables ``want`` and ``need`` both are equal to the literal ``String`` value "coffee," so the result is ``true``. While the ``==`` compares literal values, Shadow also has the ``===`` operator which compares **references**. Let’s say we assign ``want`` and ``need`` to new ``String`` objects (see :ref:`Classes: The Basics<Classes: The Basics>`) that have the same literal value: 

.. code-block:: shadow 

    want = String:create("coffee");
    need = String:create("coffee");

    Console.printLine(want === need); 

Although their **literal** values are the same, ``false`` is printed because the variables’ now point to different references (created two distinct objects). 

The following short program provides examples and explanations for the remaining relational operators. 


.. code-block:: shadow 
    :linenos:

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
	    Console.printLine("Polo is NOT the same as water polo: " # (sport1 != sport2)); 
            //"true" should be printed, as sport1 and sport2 are not equal. 


		
	    /* 
             * The following code uses >= to make comparisons. Implementing >, <, and <=
	     * follows the same guidelines as shown below. If the the variable 
             * yourAge is greater than or equal to myAge, true will be printed.
             */
	    var myAge = 20; 
	    var yourAge = 19; 
	    Console.printLine("You are older or the same age as me: " # (yourAge >= myAge));
            //"false" should be printed, as 19 is NOT >= 20

	    /* 
             * Note: When you compare Strings with these relational operators, 
	     * they are compared **lexicographically.**
             */ 
                
            Console.printLine("a is less than b: " # ("a" < "b")); 
            // "true" should be printed because lexicographically, "a" is less than "b"
 	}
    }

The console output is here for reference. 

.. code-block:: console

    Polo is NOT the same as water polo: true
    You are older or the same age as me: false
    a is less than b: true 

Logical Operators
^^^^^^^^^^^^^^^^^

Logical operators in Shadow, like relational operators, evaluate to either ``true`` or ``false`` when used in expressions. They are commonly used in ``if``/ ``else`` statements, which are discussed in detail on the :ref:`next page<Flow Control and Looping>`. See below for a list of logical operators: 

* ``and``
* ``or`` 
* ``!``

The following basic program outlines how to use these logical operators: 

.. code-block:: shadow
    :linenos:

    import shadow:io@Console;  

    class LogicalOperators
    {
	public main( String[] args ) => () 
        { 
             /* 
	      * As seen below, in order for the expression "withCream and !withSugar" 
	      * to evaluate to true, each operand must also be true. In this case, we 
	      * can see that withCream was declared to be true. Then we look at the 
	      * second statement. 
	      *
	      * Although withSugar is declared to be false, in the 
	      * expression, there is a "!" in front of withSugar. This is commonly 
	      * called the logical NOT, which evaluates to the opposite of a given
	      * expression. Since withSugar is false intially, the ! then evaulates 
	      * to true. Thus, since both operands are true, the statement "I like my
	      * coffee with cream but NOT sugar!" is printed.
	      */
          
	     var withCream = true; 
	     var withSugar = false; 
	    
	     if (withCream and !withSugar) 
	     {
	     	Console.printLine("I like my coffee with cream but NOT sugar!" ); 
	     }
	      
	    
             /* 
              * In the above lines of code, we see how to use "or." In order for the 
	      * expression "withCream or withSugar" to evaluate to true, only ONE of the 
	      * operands needs to be true. Although withSugar is declared to be false, 
	      * withCream is declared true, so the statement "I like cream OR sugar in my 
	      * coffee. Surprise me!" is printed. 
	      */

	     if (withCream or withSugar) 
	     { 
	     	Console.printLine("I like cream OR sugar in my coffee. Surprise me!"); 
	     }
	}    	      
    }

Although the program outlines the basic functionality of ``and`` and ``or``, there are a few more points to note when dealing with complex expressions using logical operators. 

* ``and`` takes precedence over ``or``, but ``!`` takes precedence over both 
* It is legal to have an expression with more than one ``and``/``or``, but make sure to pay attention to precedence rules (e.g. ``true and true and false``)
* If you have an expression with ``and``, and the first statement evaluates to ``false``, then Shadow performs **short circuit evaluation.** This means that, since the first operand evaluates to ``false``, it does not matter whether the second operand is ``true`` or ``false``.  *Its evaluation is "skipped"*. The same applies to ``or`` when the first operand evaluates to ``true``. The overall expression will evaluate to ``true`` regardless of the second operand, so its evaluation is again, "skipped."  

Unary and Assignment Operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To continue our analysis of the major types of operators in Shadow, we will discuss unary and assignment operators. 

**Unary Operators**

This type of operator has only one operand. 

* ``-`` negative value
* ``+`` positive value 
* ``!`` can also be considered a unary operator 

**Example**

.. code-block:: shadow
    
    var x = 6; 
    x = -x; 
    //Now the variable x holds the value -6 


**Assignment Operators** 

When you think of assignment operators, the ``=`` probably comes to mind. The ``=`` is, of course, an assignment operator. In a statement such as ``int x = 7;``, the variable ``x`` is **assigned** the literal value 7. However, in addition to the ``=``, there are a handful of other operators that help simplify (or give shortcuts) for assignment. See the list below: 

* ``+=``
* ``-=``
* ``*=``
* ``/=``
* ``%=``

Let’s examine the following segments of code to see why these operators are useful. 


.. code-block:: shadow
    :linenos: 

    var x = 10; 
    x %= 2;
    //Now x = 0  
	 
		
    var y = 10; 
    y = y % 10; 
    // Now y = 0 


Although **Lines 2 and 7** effectively do the same thing, line 2 is a more simple way to get to the same answer. 


The Concatenation Operator
^^^^^^^^^^^^^^^^^^^^^^^^^^

As mentioned in the previous :ref:`Code Example and Variable Names<Code Example and Variable Names>` section, ``#`` is called the **octothorpe**. It is **Shadow’s** version of the concatenation operator. 

The main function of ``#`` is to concatenate other types onto string values. For example, we use ``#`` to include literal values of variables in ``Console.printLine()`` statements. Another example is below. It is important to note that this operator has a lower precedence than addition (i.e. 1+1 will be added before it is connected with a ``String``). 

.. code-block:: shadow
    :linenos: 

    var name1 = "R"; 
    var name2 = "D"; 
    Console.printLine(name1 # 1 + 1 # name2 # 2);

The ``String`` "R2D2" will be displayed on the console.  

Lastly, if you put ``#`` in front of any value, it will call its ``toString()`` method. Take this example. 

``String someNum = #25;``
  
Now, ``someNum`` contains a ``String`` with a literal value "25". 






































