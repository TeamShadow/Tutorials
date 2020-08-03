``String`` and ``Int`` Methods
-------------------------------

This brief tutorial will cover some commonly used methods of the ``String`` and ``Int`` class. Each explanation is followed by a coded example. However, this is not an all-inclusive list. To see a complete list of all ``String`` and ``Int`` methods, visit the `Shadow API <http://shadow-language.org/reference/>`_.
 

Numeric Conversions
^^^^^^^^^^^^^^^^^^^

In order to convert a ``String`` value into a numeric type, there are two main methods. The ``toInt()`` method takes a ``String`` as a parameter and returns an ``int`` representation of a ``String``. The ``toDouble()`` method works in the same way, except it returns a ``double``. 

.. code-block:: shadow 
    :linenos: 

    var word = "6"; 
    var number = word.toInt(); 
    //number now holds the int 6


Changing Case
^^^^^^^^^^^^^^

There are two ``String`` methods that are used when trying to convert to either  uppercase or lowercase characters. However, while the uppercase version of letters may be common knowledge, not every character has a distinct uppercase/lowercase version. For example, the uppercase character for ``%`` is still ``%``. 

The  ``toLowerCase()`` method takes a ``String`` as a parameter and returns another ``String``, with *all* characters converted to lowercase. There is also a ``toUpperCase()`` method that converts all letters to uppercase and returns this new ``String``. 


.. code-block:: shadow 
    :linenos: 
    
    var yell = "YELLING"; 
    Console.printLine(yell.toLowerCase()); 
    //"yelling" is printed to the console

``substring()``
^^^^^^^^^^^^^^^^

``substring()`` is an overloaded method. One version takes in two ``int`` values that represent the starting and ending indices of a ``String``. For example, in the word "hi", "h" has index 0 and "i" has index one. The method then returns a ``String`` with all characters from (and including) the starting index to the ending index (excluding the character at this index). 

The other version takes in one ``int`` representing a starting index. All characters starting from (and including) this index until the end of the ``String`` are returned. 

.. code-block:: shadow 
    :linenos: 

    var music = "Rock n Roll"; 
    var second = music.substring(0,4); 
    var first= music.substring(7);  
    Console.printLine(first.concatenate(second)); 
    //"RollRock" is printed to the console

``equal()``
^^^^^^^^^^^^^

The ``equal()`` method for ``String`` values compares the current object to another ``String``, returning ``true`` if they are identical.   

.. code-block:: shadow 
    :linenos:

    var sweet1 = "chocolate"; 
    var sweet2 = "caramel"; 
    Console.printLine(sweet1.equal(sweet2)); 
    //false is printed to the console
		
``compare()``
^^^^^^^^^^^^^

The ``compare()`` method for ``String`` values compares the current object to another String, returning -1, 0, or 1, if the current object comes earlier, at exactly the same point, or later in a lexicographic ordering than the other value, respectively.

.. code-block:: shadow 
    :linenos:

    var lyric1 = "sweet";
    var lyric2 = "caroline";
    Console.printLine(lyric1.compare(lyric2)); 
    //1 is printed to the console because "sweet" comes after "caroline" lexicographically

``isEmpty()``
^^^^^^^^^^^^^

The ``isEmpty()`` method for returns ``true`` if the ``String`` the method being called on is empty (i.e. has length 0). 

.. code-block:: shadow 
    :linenos:

    var full = "";
    Console.printLine(full.isEmpty()); 
    //true is printed to the console

Other ``String`` Methods
^^^^^^^^^^^^^^^^^^^^^^^^

The following is a list of the remaining "built-in" ``String`` methods. For more information, here is the link to `Shadow API <http://shadow-language.org/documentation/shadow/standard/String.html>`_. 

* ``concatenate(nullable Object other)``

* ``concatenate(String other)``

* ``copy(AddressMap addresses)``

* ``index(long location)``

* ``iterator()``

* ``toByte()``

* ``toFloat()``

* ``toLong()``

* ``toShort()``

* ``toUByte()``

* ``toUInt()``

* ``toULong()``

* ``toUShort()``


Basic Mathematical Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Within the ``int`` class in Shadow, there are many methods that can be useful for performing calculations. For example, the ``add()``, ``subtract()``, ``multiply()``, ``modulus()``, and ``divide()`` methods each take an ``int`` as a parameter and return an ``int`` (other versions are mentioned in the next section). They perform the same operations as ``+``, ``-``, ``*``, ``%``, and ``/`` , respectively. 

.. code-block:: shadow 
    :linenos:

    var sum = 10.add(9); 
    Console.printLine(sum);
    //19 is printed to the console 

More Advanced Mathematical Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Also within the ``int`` class, there are many useful methods to perform more advanced mathematical calculations. Although only a few are discussed here, once again, the rest can be found on the `Shadow API <http://shadow-language.org/reference/>`_. 

The method ``abs()`` takes in an ``int`` as a parameter, and returns the non-negative version of that ``int`` (i.e. a ``uint``). ``logBase10()`` does exactly what its name implies: it takes the logarithm to the base 10 of whatever number it is called on. In addition, ``min()`` and ``max()`` take one ``int`` as a parameter each and compare it to the ``int`` the method was called on, returning the minimum and maximum of the two numbers, respectively.  ``pow()`` raises the current value to an exponent, which is the single parameter for the method, and returns a ``double``. Lastly, the ``sin()`` method takes the sine of the current value (returning a ``double``). The ``cos()`` method works in the same way, except that it takes the cosine of the current value.  The current value is assumed to be in *radians*. 

.. code-block:: shadow 
    :linenos:
    
    Console.printLine((-70).abs()); 
    //70 is printed to the console
		
    Console.printLine(100.logBase10()); 
    //2.0 is printed to the console
		
    Console.printLine(8.min(7)); 
    //7 is printed to the console
		
    Console.printLine(2.power(3)); 
    //8.0 is printed to the console
	
    Console.printLine(30.sin()); 
    //-0.9880316240928618 is printed to the console

Other ``int`` Methods
^^^^^^^^^^^^^^^^^^^^^

Although we have touched on a few ``int`` methods, they only represent a handful of them. A complete list can be found on the `Shadow API <http://shadow-language.org/documentation/shadow/standard/int.html>`_. It is also important to note that there are different versions of some of the methods we discussed above, like ``add()`` (e.g. it can also return a ``double``). 

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
* ``copy(AddressMap addresses)``
* ``equal(double other)``, can also take a ``float``, ``int``, or ``long``
* ``flipEndian()``
* ``leadingZeros()`` 
* ``logBase2()``
* ``logBaseE()``
* ``negate()``
* ``ones()``
* ``squareRoot()``
* ``subtractWithOverflow(int other)``
* ``toByte()``
* ``toCode()``
* ``toDouble()`` (same for ``float``, ``int``, ``long``, ``short``, ``String``, ``ubyte``, ``uint``, ``ulong``, ``ushort``, and ``unsigned``)
* ``trailingZeroes()``

Lastly, the ``double`` class has methods that can be called on ``double`` values. They can be found `here <http://shadow-language.org/documentation/shadow/standard/double.html>`_. The same can be said for the ``code``, ``long``, ``boolean``, etc. classes. In order to explore all of these methods and their capabilities, visit the Shadow API, `standard package <http://shadow-language.org/documentation/shadow/standard/$package-summary.html>`_, and select the desired class to see its methods. 

		











     