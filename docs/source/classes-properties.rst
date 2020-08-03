Properties of Classes and Objects
---------------------------------

Now that we have covered the basics of classes in **Shadow**, we can move on to some features/properties of classes. 

.. _immutable-and-freeze-keywords: 

The ``immutable`` and ``freeze`` Keywords
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a :ref:`previous tutorial<Strings and Immutability>`, we discussed the concept of **immutability** in terms of a ``String``. When we say that a ``String`` is **immutable**, we mean that once it is created, **its value cannot be changed**. 

In **Shadow**, a ``String`` is not the only thing that is ``immutable`` -- classes and references can be as well. We will start with analyzing ``immutable`` classes. See the basic example below: 


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    /* Imagine you own a restaurant, 
     * and you are looking to hire a 
     * another server. You use this 
     * class to create application 
     * objects. Once an object is  
     * created, which represents one
     * application, its contents can 
     * never change. Thus, we declare 
     * the class to be immutable.
     */

    immutable class tutorials:properties@JobApplication
    {
        get String name; 
        get int age; 
        get boolean experience; 
        get String skill; 

        public create(String n, int a, boolean e, String s) 
        {
            name = n;
            age = a; 
	    experience = e; 
	    skill = s; 
        }
	
        public evaluateApp() => () 
        {
            if ( age <= 18 or experience == false ) 
	    {
	        Console.printLine(name # " is not qualifed for the job!"); 
	    }
			
	    else 
	    {
	        Console.printLine(name # " would be a great employee!"); 
	    }	
        }
    }

In order to declare a class to be ``immutable``, the syntax is: ``immutable class ClassName`` (see **Line 14**).  The constructor and other methods within the class **cannot** be marked as ``immutable``, just the class header. 

Aside from the keyword ``immutable``, the ``JobApplication`` class does not *appear* to be any different from the other non-``immutable`` class we have studied, the ``Otter`` class. However, notice how none of the member variables are marked with the keyword ``set``. If you tried to do so, you would get a compile error because instances of ``immutable`` classes cannot be changed once they are created. Further, any method (outside of the constructor) that would try to change the contents of an object of an ``immutable`` class will result in a compile error. Yet, the method ``evaluateApp()`` is valid because although it uses the values of some member variables in an ``if`` / ``else`` , it does not attempt to change them. 

Syntax aside, why is it beneficial to create ``immutable`` classes, and why would we want to create ``immutable`` objects/references? The answer lies in the idea of **thread safety**. If  you have a program that is multi-threaded, it is possible that more than one thread could be trying to change a single object at the same time. This could lead to unintended results or errors in the program. Thus, by creating as many ``immutable`` objects as possible, you help to eliminate the chances of running into this problem. You can then pass around the object with confidence that it will not be changed. 
In order to understand how to create an immutable reference/object, take a look at the following driver program for the ``JobApplication`` class. 


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:properties@ApplicationDriver
    {
        public main( String[] args ) => ()
	{
	    JobApplication chris = JobApplication:create("Chris", 20, true, "positive attitude"); 
	    chris.evaluateApp(); 	
	}
    }

The console output is: 

.. code-block:: console
    
    Chris would be a great employee! 

As you can see in the driver program, **when a class is declared to be** ``immutable``, you do not need to use the ``immutable`` keyword to make the object ``immutable``; it automatically is.  The ``evaluateApp()`` method is called and executes as expected.

However, let’s imagine that the ``JobApplication`` class is non- ``immutable``. How can we create an ``immutable`` instance of the class? **We use the** ``freeze`` **keyword**. Using ``freeze`` creates an ``immutable`` , deep copy of the object it is called on. 

The syntax for using ``freeze`` is below. 

``immutable JobApplication chris = freeze(JobApplication:create("Chris", 20, true, "positive attitude"));`` 

Using ``freeze`` on the right side of the equals sign creates an ``immutable`` reference to a non- ``immutable`` object and stores it in the ``immutable`` object ``Chris``. If the statement on the left side of the equals sign had just been ``JobApplication chris``, then you would have gotten a compile error **because an** ``immutable`` **reference cannot be assigned to a non-** ``immutable`` **object (and vice versa).** 


``readonly``
^^^^^^^^^^^^

Although ``immutable`` references/classes can help with **thread safety**, the trouble is that an immutable reference cannot be stored into a normal reference without losing the guarantee that its contents are protected (as explained above). To mediate between the two different kinds of references, ``readonly`` references are used.

If a reference is marked as ``readonly``, it means that no mutable method can be called on it. However, it is useful because you can store either a normal reference or a ``immutable`` reference in it. Although this may not seem much different from an ``immutable`` reference, with a ``readonly`` reference, someone might have a normal reference they can use to change the contents of the object. Conversely, with an ``immutable`` reference, it's as if all the references to the object are ``readonly``. No one can ever change the contents of such an object.

Although methods can be marked as ``readonly``, classes cannot be. In addition, all methods of an ``immutable`` class are ``readonly`` automatically. 


Deep Copying and ``copy``
^^^^^^^^^^^^^^^^^^^^^^^^^

Another notable feature of Shadow and Shadow classes is the ability to create **deep copies** of objects. You have probably already made deep copies without knowing it;  there was a section on ``copy`` in the :ref:`Arrays<Arrays>` tutorial, and we just discussed ``freeze`` (i.e. a form of deep copying). 

Nevertheless, to be precise, making a **deep copy** means not only copying the object, but all members of the object as well. This is different than storing an object in another reference, as this only creates an **alias** to the original object. Especially in other programming languages such as Java, attempting to make a deep copy can lead to a circular reference,  where a cycle of copying begins that never terminates. Shadow mitigates this potential problem through the keywords ``copy`` and ``freeze``.  

See below for an example of using ``copy`` (references the ``Otter`` class from the :ref:`previous tutorial<Classes: The Basics>`): 

.. code-block:: shadow 

    Otter oliver = Otter:create("Oliver", "Ocean"); 
    Otter oscar = copy(oliver); 

As you can see, the syntax for using ``copy`` is quite simple. You simply write ``copy(objectToCopy)`` and store it in an object of the appropriate type. The ``Otter`` ``oscar`` is now a deep copy of ``oliver`` -- including deep copies of all of its members. Any changes to ``oscar`` are not reflected in ``oliver``. Internally, the ``copy`` command keeps track of all the new objects allocated. If a circular reference would cause something to be copied a second time, the ``copy`` command instead uses the first copy. The exception to the rule is ``immutable`` objects, which cannot be changed anyway. References to such objects are assigned directly, without making copies of the underlying objects.

In order to review how ``freeze`` works, take a look at the :ref:`above section<immutable-and-freeze-keywords>`. The syntax is the same. The only difference is that ``freeze`` creates an immutable copy of the object. 


Arrays as Objects
^^^^^^^^^^^^^^^^^
At this point in the tutorials, you probably have noticed that arrays appear to behave much like objects. You can initialize them with ``create()``, use the ``copy`` command, and call certain methods on them (e.g. ``index()`` ). As it turns out, **arrays themselves are objects**, so concepts relating to Objects in general apply to arrays.

Now that we have introduced objects, it is also worth mentioning that instead of having an array of primitive type or a ``String`` array,  you can also create an array of objects as well. In addition, you can also declare an array to be ``nullable``. This will be covered in the next section. 


.. _nullable-arrays: 

``nullable`` Arrays
^^^^^^^^^^^^^^^^^^^^

Just as you can declare a ``String`` reference to be ``nullable``, you can do the same for arrays. However, it is important to note that the **array itself is not nullable, but the elements inside of it are.** Consider the example below. 

.. code-block:: shadow 
    :linenos: 

    nullable String[] test = String:null[4]; 
		
    Otter ophelia = Otter:create("Ophelia", "River", 7); 
		
    test[1] = "Joy"; 
    test[2] = #ophelia; 

    Console.printLine(test); 

The console output is: 

.. code-block:: shadow 

    [null, Joy, default@Otter, null]

The ``nullable`` ``String`` array ``test`` is created with 4 elements, all storing ``null``. Then, in **Line 5**, we have changed the value of the 2nd element in the array to "Joy". In **Line 6**  have changed the value of the 3rd element in the array to the ``String`` representation of the ``Otter`` object ``ophelia``. 

.. note:: Recall that putting the ``#`` in front of a value converts it to a ``String``.


Method Overriding
^^^^^^^^^^^^^^^^^

Often confused with method overloading, **method overriding** is when the programmer provides a new default implementation for a pre-provided method in a class. In order to properly override a method, the overridden method header must **exactly** match the header of the original method. The method body may -- and should -- be different. A commonly overridden method for Objects is the ``toString()`` method, which gives a ``String`` representation of the object. It is a good example on how to override a method, and it is shown in the next section. 

``toString()``
^^^^^^^^^^^^^^

You may have noticed in an :ref:`earlier section<nullable-arrays>` that the ``String`` representation of the ``Otter`` object ``ophelia`` was ``default@Otter`` . In other languages like Java, ``toString()`` returns a number representing the location of that object in memory, and most of that time the number is meaningless to the programmer. In **Shadow**, the default implementation of ``toString()`` **returns the package and class that the object belongs to.**  If you don’t create a package for a class, like in the ``Otter`` example, the package will be default automatically. 

Either way, the default implementation is often useless. This is where **method overriding** becomes valuable. For example, let’s pretend we have a very simple class representing Shadow State Park, located in the Methods Mountain Range. The member variables represent the guest’s name, length of stay, and preferred activity, respectively. See below for the full class. 

.. code-block:: shadow 
    :linenos:  
    
    import shadow:io@Console;

    class tutorials:properties@ShadowPark
    {
        get String guestName; 
	get set int days; 
	get set String activity; 
	
	public create(String gn, int d, String a) 
	{
	    guestName = gn; 
	    days = d; 
	    activity = a; 
	}
	
	public readonly toString() => (String)
	{
	    String one = # guestName # " is staying for " # days # " days"; 
	    String two = " and would like to go " # activity; 
		
	    return one # two; 			
	}
	
    }


Here is an exerpt from the driver program and console output: 

.. code-block:: shadow 
    :linenos: 

    ShadowPark guest1 = ShadowPark:create("Natasha", 3, "rock climbing"); 
    Console.printLine(guest1); 

.. code-block:: console

    Natasha is staying for 3 days and would like to go rock climbing

The key lines to pay attention to in the ``ShadowPark`` class are **Lines 16-22**. This is where we have overridden the default ``toString()`` method. If a programmer decides to override the ``toString()`` method in any class, the method header **MUST** match ``public readonly toString() => (String)``, exactly. Omitting ``readonly`` will cause a compile error, as ``toString()`` cannot make changes to the object it is called on. 

Now, when we say ``Console.printLine(objectName)``, or ``#objectName``,  the program will display on the console the ``String`` value returned by the ``toString()`` method that we overrode, as shown in the driver program above. Our new ``toString()`` method is now much more helpful/informational than what would have been returned from the ``toString()`` method by default, ``properties@ShadowPark``. 

More information on method overriding will be provided when we start discussing **inheritance** in a :ref:`later tutorial<Inheritance>`. 



