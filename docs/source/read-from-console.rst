Reading from the Console
------------------------

Oftentimes when writing code, we want to prompt the user to input some value that we can use in the program. For example, what if you wanted to create a program that calculates someone’s BMI? You would need to first ask the user their height in inches and then their weight in pounds. After storing these values in separate variables, you would be able to perform calculations to output their BMI. 

How is this done? There are 4 main methods used for reading input as seen in the list below: 

* ``readByte()``, which returns the next ``byte``
* ``readCode()``, which returns the next character as a ``code``
* ``readLine()``, which returns the next line of text
* ``readString()``, which returns the next white-spaced delimited text 

In addition to what is listed above, all 4 methods also return a ``boolean`` that indicates if the end of a file being read from is reached or not. This can be ignored for user input, as it will never be true when reading input from the keyboard. 

Example
^^^^^^^

Now, let’s analyze an example. 

.. code-block:: shadow
    :linenos: 
	
    public main( String[] args ) => () 
    {
        Console.print("Enter your Zodiac sign: "); 
	(String sign, ) = Console.readString(); 
        Console.printLine("Your Zodiac sign is " # sign # '!'); 	
    }
	
Here is the output based on my input!

.. code-block:: console 

    Enter your Zodiac sign: Aquarius
    Your Zodiac sign is Aquarius!


There are a couple of important things to note syntax-wise with the code above. As you can see in **Line 3**, the first step in getting user input is some sort of prompt. Here we are asking the user to enter their Zodiac sign. Then, in order to let the program know you need the user to enter a value, **Line 4** is critical. 

As discussed in the previous page, :ref:`Methods<Methods>`, methods in Shadow can return multiple values. This is the case with the 4 aforementioned methods. Since we want to store our user input in a variable, that is why we say ``(String sign, )`` with an empty space for the second return value (a ``boolean``) to indicate we want to ignore it. Then, on the right side of the equals sign you have the ``Console.readString();``. Depending on the value you want the user to enter, substitute in any of the other four methods after ``Console``.  Once the user types in their answer and hits the enter key, the value is stored in ``sign``. Then, we can use the variable as we choose -- like in **Line 5**. 

**A note on** ``readString()`` **vs** ``readLine()``: 

Although using either of these two methods requires you to assign the input to a ``String`` variable, ``readLine()`` will read the entire line of text (including spaces) while ``readString`` will include everything up until a space, a tab, a new line, or a line feed character is reached. Thus, if I entered "Aquarius I think" as my Zodiac sign, the variable ``sign`` will be equal to "Aquarius" and not "Aquarius I think". 
	

Reading Numeric Values
^^^^^^^^^^^^^^^^^^^^^^

At this point you may be wondering, how can I read numeric types from the console? Although there is no ``readInt()`` or ``readDouble()`` method, you can still take in numbers as user input by using ``readLine()`` or ``readString()``. Then, the ``String`` method ``toInt()`` or ``toDouble`` can be used to store the input in a numeric type variable. 

Below is any example of how this can be done: 

.. code-block:: shadow
    :linenos: 
    
    Console.printLine("How much wood would a woodchuck chuck? ");
    (String wood, ) = Console.readString(); 
		
    var wood1 = wood.toInt(); 


Although not shown, if you wanted to read a ``double`` value, simply replace ``toInt()`` with ``toDouble()``. 
		



	

