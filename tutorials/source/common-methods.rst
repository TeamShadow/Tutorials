********************************
``String`` and Numerical Methods
********************************

This brief tutorial will cover some commonly used methods of the ``String`` and  numeric types, focusing on the ``int`` class. Each explanation is followed by a coded example. Note that these examples are not exhaustive. To see a complete list of all ``String`` and numerical methods, visit the `Shadow API <http://shadow-language.org/documentation/$overview.html>`__.
 

``String`` methods
==================

Below are listed some of the most commonly used ``String`` methods. For an explanation of all ``String`` methods, visit the `documentation page <http://shadow-language.org/documentation/shadow/standard/String.html>`__ for ``String``. 


Conversions to numeric types
----------------------------

In order to convert a ``String`` value into a numeric type, there are specific methods for each type. The most commonly used are the ``toInt()`` and ``toDouble()`` methods. The ``toInt()`` method converts a ``String`` representation of an ``int`` into the value of that ``int``. The ``toDouble()`` method works in the same way, except it returns a ``double``.  In all cases, a ``NumberFormatException`` will be thrown if the ``String`` is not a legally formatted version of the numeric type it is being converted to.

.. code-block:: shadow 

    var value1 = "6"; 
    var count = value1.toInt(); // count now holds 6
	var value2 = "7.61";
	var amount = value2.toDouble(); // amount now holds 7.61

Changing case
-------------

There are two ``String`` methods used when trying to convert to either uppercase or lowercase characters. Note that these methods only affect alphabetic characters. For example, the uppercase version of the character ``%`` is still ``%``. 

The  ``toLowerCase()`` method returns a new ``String`` with *all* characters converted to lowercase. There is also a ``toUpperCase()`` method that returns a new ``String`` with all characters converted to uppercase. 


.. code-block:: shadow 
    
    var yell = "YELLING"; 
    Console.printLine(yell.toLowerCase()); // "yelling" is printed to the console
	
	
Note that ``String`` values are *immutable*.  This means that it's impossible to change them by calling a method on a ``String`` reference.  In this case, ``yell.toLowerCase()`` does not change ``yell``, meaning that the following code has no effect:

.. code-block:: shadow 
    
    yell.toLowerCase(); // Does nothing unless you use the result

Size of a ``String``
--------------------

The ``size()`` method for ``String`` returns the number of bytes used to store the characters of the ``String``.  This number is the length of the ``String`` in characters if all of the characters in the ``String`` are ASCII.  This method is also a property, so it can be called with property syntax. 


The ``isEmpty()`` method returns ``true`` if the ``String`` has no characters (is the empty ``String``) and ``false`` otherwise.

.. code-block:: shadow 

    var distance = "mile";
    Console.printLine(distance.size()); // Prints 4
	Console.printLine(distance->size); // Also prints 4, using property syntax
	Console.printLine(distance.isEmpty()); // Prints false
	
Value at a location inside a ``String``
---------------------------------------

The ``index()`` method takes a ``long`` and returns the ``byte`` value at that location inside the ``String``.  This method is equivalent to using the ``[]`` operator.  Locations start at 0 and go up to one less than the size of the ``String``.

If the ``String`` only contains ASCII characters, this method returns the character at the given location.

.. code-block:: shadow 

	var word = "autological";
	Console.printLine(cast<code>(word.index(6))); // Prints "g"
	Console.printLine(cast<code>(word[6])); // Also prints "g"

Substrings
----------

``substring()`` is an overloaded method. One version takes in two ``int`` values that represent the starting and ending indices of the new ``String``. For example, in the ``String`` ``"hi"``, ``h`` has index 0 and ``i`` has index 1. The ``substring()`` method returns a new ``String`` with all byte values from (and including) the starting index to the ending index (excluding the byte value at this index). 

The other version takes in one ``int`` representing a starting index. A new ``String`` containing all characters starting from (and including) this index until the end of the ``String`` are returned.

If all the characters in a ``String`` are ASCII values, these methods find substrings based on the characters at the given indices.  Otherwise, the indices only refer to byte locations, which may or may not align with characters.

.. code-block:: shadow 

    var music = "Rock n Roll"; 
    var second = music.substring(0,4); // "Rock"
    var first = music.substring(7); // "Roll"
    Console.printLine(first # second); // Prints "RollRock"

``String`` comparison
---------------------

The ``equal()`` method for ``String`` values compares the current object to another ``String``, returning ``true`` if the two values have the same contents, including case.  Calling ``equal()`` is equivalent to using the ``==`` operator on two ``String`` values.   

.. code-block:: shadow

    var sweet1 = "chocolate"; 
    var sweet2 = "caramel"; 
    Console.printLine(sweet1.equal(sweet2)); // Prints false


The ``compare()`` method for ``String`` values compares the current object to another ``String``, returning -1, 0, or 1, if the current object comes earlier, at exactly the same point, or later in a lexicographic (dictionary) ordering than the other value, respectively.

.. code-block:: shadow

    var lyric1 = "sweet";
    var lyric2 = "caroline";
    // Prints 1 because "sweet" comes after "caroline" lexicographically
	Console.printLine(lyric1.compare(lyric2)); 


Numerical methods
=================

There is no separate class for mathematical operations like the ``Math`` class in Java.  Instead, numerical types contain methods to perform all appropriate operations on themselves.

We will describe a few useful methods for the ``int`` type, most of which also apply to the ``double`` type.  Although these two numeric types are the most important, there are also useful methods for all other primitive types such as ``code``, ``long``, ``boolean``, and so on. In order to explore the entire Shadow standard library, visit the `documentation page <http://shadow-language.org/documentation/shadow/standard/$package-summary.html>`__ for the ``standard`` package, and select the desired class or interface to see its methods and properties. 

Basic mathematical operations
-----------------------------

Within the ``int`` class, there are many methods for performing calculations. For example, the ``add()``, ``subtract()``, ``multiply()``, ``modulus()``, and ``divide()`` methods each take an ``int`` as a parameter and return an ``int``.  These methods perform the same operations as ``+``, ``-``, ``*``, ``%``, and ``/`` , respectively.   There are also overloaded versions of these methods that take a different type (such as ``double``) and might return a different type as a consequence. 

.. code-block:: shadow

    var sum = 10.add(9); 
    Console.printLine(sum); // 19 is printed to the console 

Advanced mathematical operations
--------------------------------

There are also a number of methods that perform complex operations that are **not** equivalent to simple operators.  These can perform logarithms, exponentiation, trigonometric operations, and others.  A few examples follow.

The method ``abs()`` returns the non-negative version the ``int`` it is called on, producing a ``uint``.  The ``logBase10()`` method does what its name implies: It takes the base 10 logarithm of whatever number it's called on. In addition, ``min()`` and ``max()`` each take another ``int`` as a parameter and compare it to the ``int`` the method was called on, returning the minimum or maximum of the two numbers, respectively.  The ``pow()`` method raises the current value to an exponent, which is the single parameter for the method, and returns a ``double``. Lastly, the ``sin()`` method finds the sine of the current value (returning a ``double``). The ``cos()`` method works in the same way, except that it finds the cosine of the current value.  For all trigonometric methods, angle values are assumed to be in *radians*. 

.. code-block:: shadow 
    
	// Prints 70
    Console.printLine((-70).abs()); 
    
	// Prints 2.0
    Console.printLine(100.logBase10()); 
    
	// Prints 7
    Console.printLine(8.min(7)); 

	// Prints 8.0
    Console.printLine(2.power(3)); 
    
	// Prints -0.9880316240928618
    Console.printLine(30.sin()); 

Other methods
-------------

Although only a few have been discussed here, the remainining ``int`` methods are described on its `documentation page <http://shadow-language.org/documentation/shadow/standard/int.html>`__.

* ``addWithOverflow(int other)``
* ``bitAnd(int other)``, can also take a ``long``
* ``bitComplement()``
* ``bitOr(int other)``, can also take a ``long``
* ``bitRotateLeft(int amount)``, can also take a ``uint``
* ``bitRotateRight(int amount)``, can also take a ``unit``
* ``bitShiftLeft(int amount)``, can also take a ``unit``
* ``bitShiftRight(int amount)``, can also take a ``unit``
* ``bitXor(int other)``, can also take a ``long``
* ``compare(double other)``, can also take a ``float``, ``int``, or ``long``
* ``equal(double other)``, can also take a ``float``, ``int``, or ``long``
* ``flipEndian()``
* ``leadingZeros()`` 
* ``logBase2()``
* ``logBaseE()``
* ``negate()``
* ``ones()``
* ``squareRoot()``
* ``subtractWithOverflow(int other)``
* ``toDouble()`` (same for ``byte``, ``code``, ``float``, ``int``, ``long``, ``short``, ``String``, ``ubyte``, ``uint``, ``ulong``, and ``ushort``)
* ``toUnsigned()``
* ``trailingZeroes()``

Except for the methods corresponding to bitwise operations, the ``double`` type has most of the same methods as the ``int`` type, with a few additional ones appropriate for floating-point values, which are listed below.  All ``double`` methods are described on its `documentation page <http://shadow-language.org/documentation/shadow/standard/double.html>`__.

* ``ceiling()``
* ``floor()``
* ``isFinite()``
* ``isInfinite()``
* ``isNaN()``
* ``multiplyAdd(double multiplicand, double addend)``
* ``round()``

	











     