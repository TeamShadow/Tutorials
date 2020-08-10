******
Arrays 
******


This tutorial introduces *arrays* in Shadow. An array is a simple but powerful data structure that allows you to store a large, fixed number of  values *of the same type*.  For example, if you had a list of ``String`` variables representing different dog breeds you could store all of these ``String`` values in a single array, instead of creating an individual variable for each breed. Consider the visualization of an array below:

+---------+---------+---------+---------+---------+
|    0    |    1    |    2    |    3    |    4    |
+---------+---------+---------+---------+---------+

Each box represents a location for the data in an array of size 5. The numbers show how arrays are *indexed*. Like most programming languages, arrays and other lists in Shadow are indexed starting at 0 *not* 1.  Consequently, the largest index in your array will always be one *less* than the size of the array, in this case a largest index of 4 for an array with size 5.


Initializing and displaying an array
====================================

Because an array is a list of values that all have the same type, that type's name is part of the type of an array variable.  To declare an array variable to hold a list of ``int`` values, the type name will be ``int[]``.  In general, the type of an array is the name of the type it holds, followed by a pair of square brackets.  Here are declarations of array variable intended to hold lists of ``int`` values and ``String`` values, respectively:

.. code-block:: shadow

	int[] numbers;
	String[] songs;
	
Explicit initializer
--------------------

Declaring an array variable does *not* create a list.  Instead, it creates a variable that can hold a list.  There are a couple of ways to create such a list.  One possibility is an explicit initializer, where all the values in the list are written in curly braces (``{}``). Doing so creates a list with a size equal to the number of items in the curly braces, as shown below:

.. code-block:: shadow 
    :linenos:   
		
    var favoriteBreed = "Beagle"; 
    String[] dogBreeds = {favoriteBreed, "Chihuahua", "Poodle", "Pomeranian", "Maltese"}; 
		
    Console.printLine(dogBreeds); 

**Line 2** highlights the key syntax rules for declaring an array. First, the specified variable type is followed by ``[]`` and the array name. Then, to the right of the equals sign, any literal values or variable names are enclosed by ``{ }`` and separated by commas. Voilà! You have an array.


.. note:: When you declare an array to be a certain type, all elements in the initializer *must* have the same type or you will get a compiler error.

Displaying an array
-------------------

**Line 4** above shows an easy way to format and print out an array. The ``Array`` class has a ``toString()`` method that takes an array and outputs its contents between brackets. Passing an array to the ``printLine()`` method in ``Console`` automatically invokes this ``toString()`` method, giving the following output:

.. code-block:: console 

    [Beagle, Chihuahua, Poodle, Pomeranian, Maltese]


Creating an empty array
-----------------------

Another possibility is to create an empty list using the ``create`` keyword.  This option is more common than using an explicit initializer because it allows for much longer arrays whose values need not be known ahead of time.

Instead of intializing the array variable with an explicit initializer, we use the name of the type stored in the array followed by a colon (``:``) followed by the ``create`` keyword followed by the size of the array we want to create in square brackets.  This value can be an ``int`` (or ``long``) literal or  variable or any expression that evaluates to a non-negative integer value.


.. code-block:: shadow 

    int[] golfScores = int:create[5]; 
	
Here, we have created an array called ``golfScores`` that can hold 5 values. Whether creating an empty array or using an explicit initializer, the size of an array is fixed and cannot change.  If you need an array of a different size later, you can point the array variable at an array of a different size. Although we haven't filled the array with golf scores yet, a *default* value is stored at every index in the array.  The default values of frequently used types are listed below:

* ``int``: ``0``
* ``double``: ``0.0``
* ``String``: ``""`` (empty ``String``)
* ``boolean``: ``false``
* ``code``: ``'\0'``

.. note:: When we cover the creation of objects in a :ref:`later tutorial <Classes>`, we will again use the ``create`` keyword to instantiate objects.  In both cases, the ``create`` keyword indicates that memory is being allocated on the heap to store values, whether for an object or for an array.

As you can see, the array ``golfScores`` holds 5 ``int`` values, all of which contain ``0``. Although we can't change the size of the array once it's created, we *can* update the values of individual elements inside. The following examples illustrate two possible ways to do so: 

.. code-block:: shadow 

	/*
	 * You and your friends, who are novice golfers, decide to go 
	 * play a round of golf one afternoon. Now, you want to
	 * record your scores. 
	 * 
	 * You: 110
	 * Zizi: 106
	 * Omar: 104
	 * Stephen: 108
	 * Daphne: 102
	 */
		  
	golfScores[0] = 110; 
	golfScores[1] = 106; 
	golfScores[2] = 104; 
	golfScores[3] = 108; 
	golfScores[4] = 102;
	
Although there's nothing wrong with storing values using explicit array indices, it can become tedious when the array is long.  As an example, let's consider *triangular numbers*. A triangular number is a positive integer that can be drawn to look like an equilateral triangle by arranging a number of dots equal to the value of the number.  Although the definition sounds complex, the value of the *i*:superscript:`th` triangular number is (*i* × (*i* + 1))/2.

The following code stores the first 100 triangular numbers into an array.  Note that the loop runs from 1 to 100, but the indexes of the array are from 0 to 99.  That's why we subtract 1 when specifying the index.

.. code-block:: shadow 

	int[] triangular = int:create[100];
	
	for(int i = 1; i <= 100; i += 1)
	{
		triangular[i - 1] = (i * (i + 1))/2;
	}	
	
Both of these examples achieve the desired result of storing values into an ``int`` array. The most important thing to take away is how we access specific elements of the arrays. You can read from as well as write to indexes using the same syntax.  For example, after the previous code has run, we can find out the 42\ :superscript:`nd` triangular number with the following code:

.. code-block:: shadow 

	var number = triangular[41];  // index 41 is the 42nd location
	Console.printLine("42nd triangular number: " # number);
	
This code should have the following output:

.. code-block:: console 

	42nd triangular number: 903

Array size
==========

There are many situations where your code must deal with an array created elsewhere.  How do you know the size of such an array?  In Shadow, every array knows its size, which you can find out by using the ``size`` property.  A *property* is a special method that can be called using the arrow operator (``->``).

For example, if you wanted to implement a ``for`` loop that iterates over an array called ``randomness``, you can use its ``size`` property to find out how long it is, as follows:

.. code-block:: shadow 

	var length = randomness->size;

If ``randomness`` has 947 elements, the variable ``length`` would then contain  947.  It doesn't matter what kind of values are stored in an array; its ``size`` property will always return an ``int`` value. 

Creating arrays with a default value
====================================

Although arrays are normally created with a default value, you can specify your own default value using the ``default`` keyword.  When doing so, every element in the array will contain the same value -- whatever you choose.  Consider the following segment of code: 


.. code-block:: shadow 
    :linenos:   

    String[] a = String:create[5]:default("Serendipity");
		
    for(int i = 0; i < a->size; i += 1)
    {
        Console.printLine("a[" # i # "]: " # a[i]);
    }

As seen in **Line 1** and the console output below, the addition of ``:default("Serendipity")`` to the array initialization fills each element of the array with the ``String`` ``"Serendipity"``. 

.. code-block:: console
    
    a[0]: Serendipity
    a[1]: Serendipity
    a[2]: Serendipity
    a[3]: Serendipity
    a[4]: Serendipity


``subarray()`` method
=====================

The ``subarray()`` method allows you to create a new array that is a copy of part of an existing array, very much like the ``substring()`` method described in an :ref:`earlier tutorial <Substrings>`. This copy is a *shallow copy*, which means that a reference to an object inside of one array will be copied to the other array, making the two references point at the same object.  Later, changing what is stored inside one array will not affect the other, but making internal changes to an object that both arrays point at will be reflected in both arrays. In this way, using ``subarray()`` is different from the *deep copy* technique discussed in a :ref:`later tutorial <Deep Copying and \`\`copy\`\`>`.

The parameters of the ``subarray()`` method are the start index, which is the first index you want to copy, and the stop index, which is one location *after* the last index you want to copy. The result must be stored in an array of compatible type.

.. code-block:: shadow 
    :linenos:  

    String[] trilingual = String:create[3]; 
    a[0] = "Hola"; 
    a[1] = "Hello"; 
    a[2] = "Bonjour"; 
    
    String[] bilingual = trilingual.subarray(0, 2); 
    Console.printLine("trilingual: " # a); 
    Console.printLine("bilingual: " # array); 

The contents of ``trilingual`` and ``bilingual`` are: 

.. code-block:: console

    trilingual: [Hola, Hello, Bonjour]
    bilingual: [Hola, Hello]

The array we are making a subarray from, ``trilingual``, has three elements. Using ``subarray()`` we are creating an array that only has the first two elements of ``trilingual``. As you can see in **Line 6**, the parameters ``0`` and ``2`` represent the start (inclusive) and end (exclusive), respectively. This means elements with index ``0`` and ``1`` will be made into the subarray.

.. note:: Although it seems strange to specify a subarray (or other range) using two indices where the start index is included in the result and the end index is not, this convention is very common in many programming languages.  A useful mnemonic tool is that the size of the resulting range is equal to the end index minus the start index.



``index()`` method
==================

Although it is rarely useful, the ``index()`` method is equivalent to using square brackets (``[]``) to read and write elements in an array. Because both reading and writing are required, ``index()`` is an *overloaded* method. The first way you can use ``index()`` is to read an element of an array at a specific index. The only parameter is the desired index. The second way to use ``index()`` is to change the value of an element at a specific index. The parameters are the index and the new value. See the short program below for an example:

.. code-block:: shadow 
    :linenos: 
 	
    /* Imagine you are working for a news station 
     * and need to create array with this week's 
     * predicted temperatures. You will also need 
     * to update your predictions if they change.
     */
		 
    double[] temperature = double:create[6]; 
    for (int i = 0; i < temperature-> size; i += 1)
    {
        temperature[i] = 40 + (i * 2.1); 
    }
    
    Console.printLine("The week's forecast in degrees Fahrenheit is: "); 
    Console.printLine(temperature); 
		 
    var tuesday = temperature.index(2); 
    Console.printLine("Tuesday's temp will be " # tuesday # " degrees."); 
		 
    temperature.index(3, 55.3); 
    Console.printLine("Wednesday's new temp is " # temperature.index(3) # " degrees."); 
		 
The console output is: 

.. code-block:: console

    The week's forcast in degrees Fahrenheit is: 
    [40.0, 42.1, 44.2, 46.3, 48.4, 50.5]
    Tuesday's temp will be 44.2 degrees.
    Wednesday's new temp is 55.3 degrees.


On **Line 16** we used ``index()`` to read the element at index 2 and to store it into the variable ``tuesday``. On **Line 19** we changed the value of the element at index 3 to 55.3.  On **Line 20** we used ``index()`` again to read the value we just changed.


``IndexOutOfBoundsException``
=============================

Although *exceptions* will be covered in detail in a :ref:`later tutorial <Exceptions>`, there is one common exception you might run into when working with arrays. An exception is a runtime error that is can be *thrown* and must be *caught* by an appropriate handler or it will cause your program to crash.  An ``IndexOutOfBoundsException`` is thrown when you try to access an index that does not exist inside of an array. This index could be a negative index or an index that is greater than or equal to the size of the array. For example, consider the code below: 

.. code-block:: shadow 
    :linenos:  

    int[] outOfBounds= int:create[3];
			
    for (int i = 0; i < outOfBounds->size; i += 1)
        outOfBounds[i] = 3*i + 1;
						
    outOfBounds[3] = 10;


This is the error statement displayed on the console: 

.. code-block:: console

    shadow:standard@IndexOutOfBoundsException: Index 3

Why is this exception thrown? The array ``outOfBounds`` is created correctly and filled without error. However, on **Line 6** we tried to store a value at index 3.  Because arrays are indexed starting at 0, an array of size 3 only has indices 0, 1, and 2.  Thus, an ``IndexOutOfBoundsException`` will be thrown, and the program will terminate with an error displayed on the console. It's especially important to pay attention to the indices of arrays when writing the conditions for a loop.  Below is code that will have the same error but might be harder to notice because the problem is in the condition of the ``for`` loop:

.. code-block:: shadow  

    int[] outOfBounds= int:create[3];
			
    for (int i = 0; i <= outOfBounds->size; i += 1)
        outOfBounds[i] = 3*i + 1;
		
.. note:: It is possible to catch an ``IndexOutOfBoundsException``, but it's rarely useful to do so.  An ``IndexOutOfBoundsException`` usually indicates that a mistake was made programming.  While one can imagine scenarios where some kind of array range checking is done through exception handling, it's *much* slower to create, throw, and catch exceptions than it is to do proper range checking with ``if`` statements or careful loop conditions.

2-D arrays
==========

A 2-D array is an array whose elements have both a *row*  index and a *column* index. You can imagine a 2-D array as a table, with each row acting like a separate array. Consider the table below, showing the row and column indices of each element. 

+---------+---------+---------+---------+---------+
|   0,0   |    0,1  |   0,2   |   0,3   |   0,4   |
+---------+---------+---------+---------+---------+
|  1,0    |  1,1    |  1,2    |  1,3    |  1,4    |
+---------+---------+---------+---------+---------+
|  2,0    |    2,1  |  2,2    |  2,3    |  2,4    |
+---------+---------+---------+---------+---------+

Although the choice is arbitrary, it's convention to treat the first index as the row and the second as the column. Now, let's discuss how to declare and initialize a 2-D array.  As with regular arrays, it's possible to use either explicit initialization or to create empty arrays: 

.. code-block:: shadow
	:linenos:  
	
	String[][] dimensions = {{"don't","stop","believin"}, {"livin","lonely","world"}, {"small","town", "girl"}};
	int[][] temp = int:create[4][5];

On **Line 1**, each grouping of words behaves like a row, forming a 2-D array with 3 rows and 3 columns.  On **Line 2**, a 2-D array is created with 4 rows and 5 columns, all filled with ``0``.  In order to let the compiler know you're declaring a 2-D array variable, you use two pairs of brackets (``[][]``) instead of the single pair you would use with a normal array.

Just as it's often valuable to access every index of a normal array using a ``for`` loop, this idea can be extended to 2-D arrays as well. Instead of a single ``for`` loop, we can use nested ``for`` loops where the outer loop iterates over the rows and the inner loop iterates over the columns. See below for an example: 


.. code-block:: shadow 
    :linenos:  

    int[][] speeding = int:create[4][5]; 
		
    for (int i = 0; i < speeding->size; i += 1)
    {
        for (int j = 0; j < speeding[i]->size; j += 1)
		{
			speeding[i][j] =  10*i + j + 60; 
		}
    }
		
    Console.printLine(speeding); 

The array contents are as follows: 

.. code-block:: console

    [[60, 61, 62, 63, 64], [70, 71, 72, 73, 74], [80, 81, 82, 83, 84], [90, 91, 92, 93, 94]]
 
**Line 3** shows a ``for`` loop iterating through the ``speeding->size`` rows in the array. **Line 5** shows a ``for`` loop iterating through the number of columns on row ``i``, which is ``speeding[i]->size``.  It's possible to create a 2-D array where each row has a different number of columns -- a *ragged* array.  Whether or not the array is ragged,  ``speeding[i]->size`` will always give the correct number of elements on row ``i``.

Note that **Line 7** indexes both the row ``i`` and the column ``j`` to store a value at a specific location in ``speeding``.

In Shadow it is possible to have 3-D arrays or higher, up to an unlimited number of dimensions. However, they are not often used in practice, as a high-dimensional table becomes difficult to think about and use. In fact, there is no such thing as a *true* 2-D array in Shadow. It is equally valid to think of a 2-D (or higher-dimensional) array as an array of arrays.

``foreach`` loops
=================

For the last array topic, we will examine the ``foreach`` loop, a fourth kind of loop closely related to a ``for`` loop. A ``foreach`` loop provides an efficient way to iterate through an array that is both safer and simpler to implement than a ``for`` loop.  An example is below: 

.. code-block:: shadow 
    :linenos:  

    String[] a = String:create[5]:default("Kerfuffle");
		
    foreach (String value in a)
        Console.printLine(value);

Console output: 

.. code-block:: console
    
    Kerfuffle
    Kerfuffle
    Kerfuffle
    Kerfuffle
    Kerfuffle
	
The loop header on **Line 3** is ``foreach (String value in a)``. This means that the program will step through every single element in the array, starting at the first index. Each time the loop runs, the next element in the array will be stored into ``value``. Any statements inside the loop will be executed for each element.

Note that you must always specify a type name followed by a variable name followed by the keyword ``in`` followed by the name of the array.  The type name must always be the type of the elements *inside* the array, but you can choose any legal variable name, as long as it isn't already in use.

``foreach`` loops are a popular alternative to ``for`` loops when dealing with arrays because the programmer doesn't have to worry about initialzing, updating, or checking an index variable.

.. note:: ``foreach`` loops are convenient, but they are less flexible than ``for`` loops.  For one thing, they are read only: Assigning a different value to the loop variable (``value`` in the example above) will *not* change the contents of the array.  Also, there is no way to leave the loop early without a ``break``, ``continue``, or ``return`` statement.


			
