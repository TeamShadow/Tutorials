Arrays 
------
This page introduces and analyzes **arrays** in Shadow. An array is a very useful data type that is able to store multiple values *of the same type*.  For example, if you had a list of ``String`` variables representing different dog breeds, instead of dealing with all of these individual variables, you could store the literal ``String`` values in a single array. See the visualization of an array below. 

+---------+---------+---------+---------+---------+
|    0    |    1    |    2    |    3    |    4    |
+---------+---------+---------+---------+---------+

Each "box"  represents the location of the data being stored in the array. The numbers demonstrate how arrays are **indexed**. *It is important to remember that the first position is indexed at 0, NOT 1.*  In the dog breed example, each numbered location would correspond to a different dog breed (e.g. At location 0, it could hold "Beagle"). 

Initializing and Displaying an Array
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There are multiple ways to **declare** and **fill** an array in Shadow.  If you would like to input literal values, or variables of the same type as the array, the declaration is as follows: 

.. code-block:: shadow 
    :linenos:   
		
    var favoriteBreed = "Beagle"; 
    String[] dogBreeds = {favoriteBreed, "Chihuahua", "Poodle", "Pomeranian", "Maltese"}; 
		
    Console.printLine(dogBreeds); 

Console output: 

.. code-block:: console 

    [Beagle, Chihuahua, Poodle, Pomeranian, Maltese]
	
**Basic Initialization** 

**Line 2** highlights the key syntax rules for declaring an array. First, the specified variable type is followed by ``[]`` and the array name. Then, to the right of the equals sign, any literal values or variable names are enclosed by ``{ }`` and separated by commas. Voilà! You have an array. 

.. note:: When you declare an array to be a certain type, all elements in that array *must be of the same type* or you will get a compile error!


**Displaying an Array** 

Finally, **Line 4** shows an easy way to nicely format and print out an array, as seen in the console output above. The ``Array`` class has a ``toString()`` method that takes an array and outputs its contents in between ``[ ]``. The statement in **Line 4** automatically invokes this ``toString()`` method. 


**Other Methods of Initialization** 

Sometimes, as programmers, we are not able to or do not want to declare and fill an array all at once. Instead, we can specify the array’s **size**: 

For example, 

.. code-block:: shadow 

    int[] golfScores = int:create[5]; 
	
Here, we have created an array called ``golfScores`` that can hold 5 values. *Once an array’s size is set, it cannot change.* Although we haven’t filled the array with golf scores yet, the array is **not empty.** Each index is given the same default value. The default values of frequently used types are listed below: 

* ``int``: ``0``
* ``double``: ``0.0``
* ``String``: ``""`` (empty ``String``)
* ``boolean``: ``false``
* ``code``: ``'\0'``

*A Brief Side Note: At this point, you may be wondering why we used the reserved word* ``create`` *when initializing the array. This is because in Shadow, arrays are designed to be "object-like." Although we will be covering objects later in the tutorials, all you need to know for now is the syntax.* 


Thus, the array ``golfScores`` holds five 0’s. Now you may ask, how do we input the golf scores? Although you cannot change the size of the array once it is created, you can change/update the values of individual elements. The following examples illustrate two possible ways to do so: 

.. code-block:: shadow 
    :linenos:   

    /*
     * You and your friends, who are extremely novice golfers, decide to go 
     * play a round of golf one afternoon. Now, you want to
     * record their scores. 
     * 
     * You: 102
     * Zizi: 104
     * Omar: 106
     * Stephen: 108
     * Daphne: 110
     */
		 
    /*
     * Here we use a for loop to fill in the scores, 
     * which happen to each increase by 2. 
     */
		 
    var index = 0; 
    for( int i = 102; i <= 110; i += 2 ) 
    { 
        golfScores[index] = i; 
	index += 1; 
    }
		 
		 
    /* 
     * Here we will manually enter the scores. 
     */
		  
    golfScores[0] = 102; 
    golfScores[1] = 104; 
    golfScores[2] = 106; 
    golfScores[3] = 108; 
    golfScores[4] = 110; 
	
Both of these examples achieve the desired result of putting the golf scores into the ``int`` array. The most important thing to take away is how we accessed specific elements of the array. As mentioned before, an array’s first element is indexed at zero. So, if you wanted to put your score as the first element, you would say ``golfScores[0] = 102;`` (or ``golfScores[index]`` when index equals 0 for the ``for`` loop example). **If you ever need to access individual elements of an array, this is the correct syntax.** e.g. ``var worstScore = golfScores[4];`` Now, ``worstScore`` holds the value 110. 

``size``
^^^^^^^^

Suppose you have an array called ``randomness`` and you want to implement a ``for`` loop that traverses the entire array. First, you must know the length of ``randomness``. Luckily, the ``Array`` class has a "built in" property called ``size`` which returns the length of a given array. Below is the syntax for using ``size``: 

``var length = randomness->size;``	

Let’s say ``randomness`` has 4 elements. Now the variable ``length`` is equal to 4. 

``default``
^^^^^^^^^^^

Another feature of arrays is the ability to fill an array with ``default`` values. This means that every element in the array will contain the same literal value.  Consider the following segment of code: 


.. code-block:: shadow 
    :linenos:   

    String[] a = String:create[5]:default("Serendipity");
		
    for( int i = 0; i < a->size; i += 1 )
    {
        Console.printLine("a[" # i # "]: " # a[i]);
    }

As seen in **Line 1** and the console output below, the addition of ``:default("Serendipity")`` to the array initialization fills each element of the array with the word "Serendipity". 

.. code-block:: console
    
    a[0]: Serendipity
    a[1]: Serendipity
    a[2]: Serendipity
    a[3]: Serendipity
    a[4]: Serendipity
		  
``copy``
^^^^^^^^

The ``Array`` class has a useful keyword called ``copy``, which *completely* copies the contents of one array into another array. This is called a **deep copy**. In addition to arrays, the ``copy`` keyword can be used with any object in order to create a deep copy of the object, including all of its members. ``copy`` will be discussed in more detail in the :ref:`Properties of Classes and Objects<Properties of Classes and Objects>` tutorial. 

Using the example from the ``default`` section above, where ``a`` is a ``String`` array with size 5, let’s examine how ``copy`` works. 


.. code-block:: shadow 
    :linenos:  

    String[] b = copy(a); 
    for (int i = 0; i < b->size; i += 1)
    {
        Console.printLine("b[" # i # "]: " # b[i]);
    }
		
    b[0] = "Oops"; 
		
    Console.printLine("a[0]:" # a[0]); 
    Console.printLine("b[0]:" # b[0]); 

Below is the console output: 

.. code-block:: console

    b[0]: Serendipity
    b[1]: Serendipity
    b[2]: Serendipity
    b[3]: Serendipity
    b[4]: Serendipity
    a[0]: Serendipity
    b[0]: Oops

The expression ``copy(a)``  in **Line 1** is the proper syntax used in order to copy everything in ``a`` to store in ``b``. However, it is important to note that when we change the value of the first element in ``b`` to “Oops” (**Line 7**), **it does not change the first element in** ``a``.  It is still “Serendipity”. The arrays do not point to the same reference. 



``subarray()``
^^^^^^^^^^^^^^

The ``subarray()`` method works in much the same way as copy, except that it allows you to copy a *part* of the array by using a range of indices. The parameters of the method are the ``start`` **index** from where you want to copy, and the ``stop`` **index**, which copies everything up to but not including this index. The result must be stored in an array of compatible type. 


.. code-block:: shadow 
    :linenos:  

    String[] a = String:create[3]; 
    a[0] = "Hola"; 
    a[1] = "Hello"; 
    a[2] = "Bonjour"; 
    
    String[] array = a.subarray(0, 2); 
    Console.printLine("a: " # a); 
    Console.printLine("array: " # array); 

The contents of the ``a`` and ``array`` are: 

.. code-block:: console

    a: [Hola, Hello, Bonjour]
    array: [Hola, Hello]

The array we are making a subarray from, ``a``, has three elements. Using ``subarray()``, we want to create an array that only has the first two elements of ``a``. As you can see in **Line 6**, the method is being called on ``a`` and the parameters ``0`` and ``2`` represent the ``start`` and ``end``, respectively. This means elements with index ``0`` and ``1`` will be made into a subarray. Most importantly, the result is being stored in a ``String`` array. Now, ``array`` contains "Hola" and "Hello", as seen in the console output. 


``index()``
^^^^^^^^^

``index()`` is a useful method for accessing/changing the elements in an array. Additionally, ``index()`` is an **overloaded** method, in this case meaning that it has two different method signatures. The first way you can use ``index()`` is to access/return an element of an array at a specific index. The only parameter is the desired index. The second way to use ``index()`` is to change the value of an element at a specific index. The parameters are the index and the new value. See the short program below for an example implementation. 

.. code-block:: shadow 
    :linenos: 
 	
    /* Imagine you are working for a news station 
     * and need to create array with this week's 
     * predicted temperatures. You will also need 
     * to update your predictions if they change.  
     * Below is the implementation of the method
     * index.
     */
		 
    double[] temperature = double:create[6]; 
    for (int i = 0; i < temperature-> size; i += 1)
    {
        temperature[i] = 40 + (i * 2.1); 
    }
    
    Console.printLine("The week's forcast in degrees fahrenheit is: "); 
    Console.printLine(temperature); 
		 
    var tuesday = temperature.index(2); 
    Console.printLine("Tuesday's temp will be " # tuesday # " degrees."); 
		 
    temperature.index(3, 55.3); 
    Console.printLine("Wednesday's new temp is " # temperature.index(3) # " degrees."); 
		 
The console output is: 

.. code-block:: console

    The week's forcast in degrees fahrenheit is: 
    [40.0, 42.1, 44.2, 46.3, 48.4, 50.5]
    Tuesday's temp will be 44.2 degrees.
    Wednesday's new temp is 55.3 degrees.


The key lines in this example are **Lines 17** and **20**. In **Line 17**, we used ``index()`` to store the value of the element at index 2 in the variable ``tuesday``. In **Line 20**, we changed the value of the element at index 3 to 55.3. 


``IndexOutOfBoundsException``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although **exceptions** will be covered in detail in a :ref:`later tutorial<Exceptions>`, it is important to note a common exception you might run into when working with arrays. In basic terms, an exception is a runtime error that is thrown when the program runs.  An ``IndexOutOfBoundsException`` is thrown when you try to access/create/use/reference an index that does not exist (i.e. a negative index or an index that is greater than the size of the array). For example, consider the code below: 

.. code-block:: shadow 
    :linenos:  

    int[] outOfBounds= int:create[3];
			
    for (int i = 0; i < outOfBounds->size; i += 1)
        outOfBounds[i] = 3*i + 1;
						
    outOfBounds[4] = 4;


This is the error statement displayed on the console: 

.. code-block:: console

    shadow:standard@IndexOutOfBoundsException: Index 4

Why is this exception thrown? The array ``outOfBounds`` is created correctly and filled without error. However, notice in **Line 6** that we try to add a 4th element to the array by stating ``outOfBounds[4] = 4;`` This will cause an ``IndexOutOfBounds`` exception to be thrown and the program to terminate with an error (displayed on the console) because there is no index of 4 in the array. Again, *once an array’s size is declared, it cannot change.* It is especially important to pay attention to indices of arrays when writing the conditions for a loop (e.g. a ``for`` loop).  


2-D Arrays
^^^^^^^^^^

Now, we will move into a discussion on 2-Dimensional arrays. A 2-D array is an array with elements that have a **row**  index and a **column** index. You can imagine a 2-D array as a checkerboard, with each row acting like a separate array. See the visual below. 


+---------+---------+---------+---------+---------+
|   0,0   |    0,1  |   0,2   |   0,3   |   0,4   |
+---------+---------+---------+---------+---------+
|  1,0    |  1,1    |  1,2    |  1,3    |  1,4    |
+---------+---------+---------+---------+---------+
|  2,0    |    2,1  |  2,2    |  2,3    |  2,4    |
+---------+---------+---------+---------+---------+

In the ordered pairs above, the first number represents the **row** number, and the second number represent the **column** number. When referring to elements of a 2-D array, the row index also comes first. But first, let’s discuss how to declare and initialize a 2-D array. 


``String[][] dimensions = {{"don’t","stop","believin"}, {"livin","lonely","world"}, {"small","town", "girl"}};``

``int[][] temp = int:create[4][5];``
			

In both examples, each grouping of words is like its own array. In the first example, there are 3 rows and 3 columns and in the second, 4 rows and 5 columns filled with ``0``.  In order to let the compiler know you are creating a 2-D array, you use 2 ``[]``. Just like with 1-D arrays, you can also declare the array and then fill it using a ``for`` loop. See below for an example. 


.. code-block:: shadow 
    :linenos:  

    int[][] speeding = int:create[4][5]; 
		
    for (int i = 0; i < speeding->size; i += 1)
    {
        for (int j = 0; j < speeding[i]->size; j += 1)
	{
	    speeding[i][j] =  i + j + 60; 
	}
    }
		
    Console.printLine(speeding); 

The array contents are as follows: 

.. code-block:: console

    [[60, 61, 62, 63, 64], [61, 62, 63, 64, 65], [62, 63, 64, 65, 66], [63, 64, 65, 66, 67]]
 
As seen in **Line 3**, in order to iterate through the 2-D array correctly, the condition for the outer loop should be ``i < speeding->size;``. ``speeding->size`` represents the number of **rows** in the array. Conversely, the condition ``j < speeding[i]->size`` traverses through the **columns** of the array (and avoids an ``IndexOutOfBoundsException`` if the array is jagged). However, instead of using ``size`` for the conditionals, if you already know the length of the columns or rows, you can use those values for the conditions instead. 

Lastly, notice how in **Line 7** we wrote ``speeding[i][j]`` in order to set the value at the specific row/column index. This is the proper syntax. 

.. note:: ``copy``, ``index()``, and ``subarray()``  also work for 2-D arrays. 

A final note: In Shadow it is possible to have 3-D arrays and really, in theory, an infinite number of dimensions. However, in practice they are not often used, as the syntax can become quite tedious and complicated. 
In fact, in reality, there is no such thing as a *true* 2-D, 3-D, 4-D, etc. array in Shadow. You really just have an array in an array. 

``foreach`` Loops
^^^^^^^^^^^^^^^^^^

For the last array topic, we will examine the ``foreach`` loop. In basic terms, a ``foreach`` loop provides an efficient way to iterate through an array (or 2-D array), and often easier/quicker to implement than a ``for`` or nested ``for`` loop.  An example is below: 


.. code-block:: shadow 
    :linenos:  

    String[] a = String:create[5]:default("Kerfuffle");
		
    foreach (String value in a)
        Console.printLine(value);

Console: 

.. code-block:: console
    
    Kerfuffle
    Kerfuffle
    Kerfuffle
    Kerfuffle
    Kerfuffle



The key statement in this block of code is **Line 3**: ``foreach ( String value in a)``. This means that the program will trace through every single element in the array, starting at the first index. The statement inside the loop will be executed for each element. 

What if my array is of a different type, and a different name than the example? The answer is simple: replace ``String`` with your array’s type, and ``a`` with your array’s name. 



			
