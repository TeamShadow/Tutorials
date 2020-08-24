*******
Classes
*******

Congratulations! If you've reached this point in the tutorials, you should have good understanding of the basics of the Shadow language: variables, operators, making choices, loops, methods, and arrays. Now, it's time to move on to classes, objects, and interfaces -- three crucial topics. Similar to Java, Shadow is *object-oriented*. However, before we dive into creating and using objects, we must first understand Shadow classes. 

Whenever we write a program, we always start by creating and naming the class that serves as the container for our code. So far, we've been writing the majority of our code directly inside the ``main()`` method to test out the language basics.  In the :ref:`Methods` tutorial, we introduced the idea of methods as a way to break down long segments of code into useful, named chunks. However, methods are always part of an *object*, which can also contain data.

We want to keep data organized so that only the methods that need to access the data can do so.  To define a group of data and the methods that can access it, we write *classes* which are the blueprints for objects.  Just as we started with just the ``main()`` method and showed how we could add additional methods, we're going to show you how you can write different classes to create objects that can hold different data and interact with each other.

In order to explain the concepts behind classes and objects, we'll be analyzing an extended example of the ``Otter`` class. An object is a collection of data and methods to manipulate that data.  Sometimes Shadow objects model objects in the physical word, as in this case where ``Otter`` objects could model real otters.  In other cases, a Shadow object could represent something more abstract like a collection of messages or a particular shade of blue.

Before we go on, take a moment to read through the program below to get familiar with it. 


.. code-block:: shadow 
    :linenos:

    class Otter
    {
        /* These are the private member variables
		 * of the Otter class.
		 */
		get String name; 
		get set String habitat; 
		get set boolean mate; 
		get set int age; 
		
		/* This is the contructor for the Otter class,
		 * which initializes its private members.
		 */
		public create(String newName, String newHabitat, int age) 
		{
			name = newName; 
			habitat = newHabitat; 
			this:age = age; 
			mate = false; 
		} 
		
		/* Implementation of the set method
		 * for the member variable mate. 
		 */
		public set mate(boolean value) => ()
		{
			if (value and age > 2)
			{
				mate = true;
			}
			else
			{
				mate = false;
			}
		}

		/* This  method returns an int 
		 * representing the number of fish caught. 
		 */
		public goFishing() => (int)
		{
			int fish; 
			if (mate) 
			{
				fish = 10; 	
			}
			else 
			{
				fish = 5; 
			}				
			return fish; 
		}	
    }

Member variables
================

The first thing to note about the ``Otter`` class is its *member variables* (also called *fields*)  seen on **Lines 6-9**. Member variables represent a class's data. For example, imagine you're looking at a real, live otter. How would you describe or define the animal? Does it have a name? What's its habitat? Does it have a mate? What's its age? Each piece of information can be stored as specific member variable in the ``Otter`` class. The ``name`` member is a ``String`` variable, ``mate`` is a ``boolean``, ``age`` is an ``int``, and ``habitat`` is a ``String`` as well. There's no limit to how many member variables a class can have, and there's no minimum requirement. A class doesn't *need* to have member variables at all. 

Aside from the modifiers ``get`` and ``set``, declaring a member variable is the same as declaring any local variable. Unlike local variables, which only exist for the lifetime of a method, these variables exist inside of an object for its lifetime.

.. note:: Unlike local variables, member variables *must* be declared with an explicit type, instead of ``var``.

Member variables cannot be accessed by code written in a different class.  If you're familiar with other object-oriented languages, it's as if all member variables in Shadow are declared ``private``, although this keyword should not be used explicitly for Shadow member variables.

Since these variables can only be directly accessed by code in the same class,  we use the ``get`` and ``set`` modifiers to allow other classes to read or write the value of these private member variables through properties, explained :ref:`below <Properties>`.


Constructors and objects
========================

It is important to understand that the ``Otter`` class is *not* an ``Otter`` object. Rather, it's a template or blueprint that describes the attributes, features, and actions of an ``Otter``. Writing the class doesn't create any ``Otter`` objects, but we can create an object, or an *instance*, of the ``Otter`` class.  This object will have its own name, habitat, age, and will either be mated or not.  ``Otter`` objects will all have the same member variables, but the *values* of those member variables will vary from one object to another. Otters, like people, are unique, after all.

To create objects and specify the initial values for member variables, we use a *constructor*. A constructor is a special kind of method in a Shadow class.  There's an example of a constructor on lines **Lines 14-20** of our example ``Otter`` class.  We use constructors to create a new object by passing in the appropriate values. The general method header for a constructor is as follows: 

.. code-block:: shadow 

	public create(parameters)

The name of every constructor in Shadow is ``create``.  Most constructors are ``public``, allowing code in other classes to create a new object of the class. The number and type of parameters will vary, depending on the class. Before we get into the body of the constructor, let's go over the basic syntax for creating an object in Shadow, which is similar to how arrays are created.

A constructor is used to initialize an object, not to give back information. Unlike normal methods, a constructor has no return types, not even ``=> ()``.

.. note:: Many object-oriented languages use the name of the class for constructors, but Shadow uses ``create``.


Creating an object
------------------

Objects can be created in any method.  Some classes have a ``main()`` method where a program can start, and other's don't.  Although the ``Otter`` class doesn't have a ``main()`` method, we could, for example, create an ``Otter`` object in a method of another class.  Sometimes, we will call a class that tests objects of other classes a *driver class*.

We could imagine a driver class ``OtterDriver`` that has a ``main()`` method.  Inside this ``main()`` method, the following code could create an ``Otter`` object:

.. code-block:: shadow 

	Otter olive = Otter:create("Olive", "river", 6);

The first part of this line, ``Otter olive``, declares a variable of type ``Otter`` to point at the object we're about to create.  The type must match the kind of object we're creating. The name of our variable is ``olive``, which follows the same naming conventions  we discussed in the  :ref:`Variables` tutorial.

The expression on the right of the equals sign invokes the ``Otter`` constructor, creating an ``Otter`` object. Inside the parentheses we see three literal values, the name (``"Olive"``), habitat (``"river"``), and age (``6``) that the constructor requires as parameters. Looking back at the ``Otter`` class, you can see in the constructor parameter list that it requires two ``String`` variables and an ``int``, in that order.


The constructor body
--------------------

Now that you know how to create an object, let's examine **Lines 16-19** of the ``Otter`` class to see how the constructor works . The goal of a constructor is to initialize the object's member variables. On **Line 16**, the ``newName`` parameter giving the name of the ``Otter`` is stored into the ``name`` member variable.  Given the driver code above, ``"Olive"`` will be stored into ``name``.

What happens if the parameter name is the same as the member variable name? Although this is legal in Shadow, the parameter name will *hide* the name of the member variable. **Line 18** shows a way to resolve this problem. Both the member variable and the parameter have the same name, ``age``. Although the code would compile if you said ``age = age;``, it would have no effect, since it would set the value of the parameter to itself.  By putting ``this:`` before the name of a member variable, you can specify that you're referring to the member variable *inside* the current object.  The keyword ``this`` is a Shadow reserved word that refers to whatever object the code is currently inside of. 

**Line 19** demonstrates that not all member variables need to be initialized using parameter values.  The member variable ``mate`` is always initialized to ``false``, as we assume that an ``Otter`` object does not have a mate when it's first created. 

.. note:: We also could have set the field ``mate`` equal to ``false`` at **Line 8** where the variable is initially declared.

Overloaded constructors
=======================

Just like other methods in Shadow, constructors can be *overloaded*. This means that one class can have more than one constructor, as long as each one's parameter list varies in type or number from the others. Consider this additional constructor for the ``Otter`` class: 


.. code-block:: shadow 

    public create(String newName, String newHabitat) 
    {
        name = newName; 
		habitat = newHabitat; 
		age = 0; 
		mate = false; 
    }


The only difference is this overloaded constructor does not take in an ``int`` representing age. It sets the member variable ``age`` to ``0`` when the object is created.  This constructor is legal because it has a different number of parameters. 

If this constructor is part of the ``Otter`` class, someone could create an ``Otter`` object with the following code: 

.. code-block:: shadow 

	Otter oliver = Otter:create("Oliver", "ocean");

Now ``oliver`` is an ``Otter`` whose ``age`` member is ``0``. Both ``olive`` and ``oliver`` are still ``Otter`` objects containing the same kinds of data, even though they were created by invoking different constructors. 

Default constructors
====================

A default constructor is a constructor that takes in no parameters.  Objects created by default constructors are assigned default values for all of their member variables.

If you don't write any constructors for your class, the Shadow compiler creates a default one behind the scenes, initializing all variables with the following default values for commonly used primitive types:

* ``int``: ``0``
* ``double``: ``0.0``
* ``boolean``: ``false``
* ``code``: ``'\0'``

Note that this default constructor is created for you only if *no other* constructor is defined in the class. However, what happens to reference (non-primitive) member variables? If the member variable is ``nullable``, the compiler will initialize it to ``null``, but if it isn't, the compiler will give an error because you haven't said what this member variable will be initialized to and there's no suitable default.

If you get this compiler error, you *could* mark all reference variable types as ``nullable`` , but doing so would increase the number of ``nullable`` references, which is a bad programming practice. If there are reasonable defaults for these member variables, you can easily initialize the individual member variables outside of any constructor. 

For example, if one of your member variables is ``String something;``, to avoid using ``nullable`` and still use the default constructor, you could simply write ``String something = "";`` 


Constructor chaining
====================

*Constructor chaining* is another feature of constructors that helps eliminate repeated code. Using the keyword *this*, you can invoke an existing constructor from another constructor of that class. Doing so makes it easy to provide a range of different constructors to programmers who will use your class.  These constructors will often call other constructors that that take more parameters, supplying them with default parameter values.

The following code shows the original constructor for the ``Otter`` class with two more added: 

.. code-block:: shadow 
    :linenos: 

    public create(String newName, String newHabitat, int age)
    {
        name = newName;
        habitat = newHabitat;
        this:age = age;
        mate = false;
    }
    
    public create(String newName, String newHabitat)
    {
    	this(newName, newHabitat, 0); 
    }
    
    public create(String newName)
    {
    	this(newName, "unknown"); 
    }

Now, consider the following code from a test program: 

.. code-block:: shadow 

    Otter jasmine = Otter:create("Jasmine"); 
    Console.printLine(jasmine->name); 

    Otter harrison = Otter:create("Harrison", "pond"); 

Notice that we create ``jasmine`` using that constructor that takes only one parameter, the name. How do the other member variables get instantiated? Look at **Line 16** above. Using the ``this`` keyword, it invokes the previous constructor using the name that was passed in (``"Jasmine"``) along with a value for ``habitat`` (``"unknown"``) as parameters. Control then flows to the constructor that takes two ``String`` values as parameters. If there hadn't been such a  constructor, we would have gotten a compiler error. In this constructor, there is yet *another* example of constructor chaining. The two ``String`` values passed in, along with the value ``0``, are sent as parameters to the original constructor where the member variables are initialized.

Finally, look at the second ``Otter`` object, ``harrison``. Here, we have invoked the constructor that takes two ``String`` values, which also includes a call using ``this``. The member variable ``age`` is set to ``0``. 

.. note:: It's permitted to write other code inside a constructor after invoking another constructor using ``this``, but the constructor invocation *must* be the first statement.


Properties
==========

Let's return to the original ``Otter`` class and consider the ``get`` and ``set`` keywords. 

Because all member variables in Shadow are private, how can other classes access or change these values? It would be tedious to write *accessors* (methods that return the value of a member variable)  and *mutators* (methods that change the value of a member variable) for every single member variable. Instead, Shadow provides a tool called *properties*. Properties are similar to method calls, but they use the arrow operator (``->``) instead of parentheses with arguments. 

In order to see how properties work, take a look at **Line 6** of the original ``Otter`` class: 

.. code-block:: shadow 

		get String name;

Here the ``get`` keyword modifies the member variable ``name``, creating an accessor property that we can use in our ``OtterDriver`` program, part of which is shown below:


.. code-block:: shadow 
    :linenos: 

    Otter olive = Otter:create("Olive", "river", 6); 
    Console.printLine(olive->name # " lives in a " # olive->habitat); 
		
    olive->mate = true; 
    Console.printLine(olive->name # " has a mate: " # olive->mate); 
    Console.printLine(olive->name # " just caught " # olive.goFishing() # " fish!"); 
		
The program output is below: 

.. code-block:: console 

    Olive lives in a river
    Olive has a mate: true
    Olive just caught 10 fish!


In **Line 2** of the driver program we see ``olive->name``, which returns the value of the member variable ``name`` (``"Olive"``). The same applies for ``olive->habitat``. If either ``name`` or ``habitat`` hadn't had ``get`` in their declaration, we would've needed to write accessor methods for both in order to retrieve their values in ``OtterDriver``. 

Additionally, the ``set`` keyword can be used to create a mutator property. **Line 4** states ``olive->mate = true;``. If no ``set`` mutator method was defined in the program, the member variable ``mate`` would simply have been changed to ``true``.

Most of the time, simply applying the ``get`` or ``set`` modifier to a member variable is fine, but it's possible to customize what happens if you want something more complicated than retrieving or storing a value.  For example, in the ``Otter`` class, a condition must be met before ``mate`` can be set to ``true``: 

.. code-block:: shadow 
    :linenos: 

    public set mate(boolean value) => ()
    {
        if(value and age > 2)
		{
			mate = true;
		}
		else
		{
			mate = false;
		}
    }

In order for the property to work correctly, the method header is critical. The syntax is as follows:  

.. code-block:: shadow 
	
	public set memberName(parameter of member type) => ()

In the ``Otter`` class, the member variable name is ``mate`` and the type is ``boolean``, as reflected in the method header. Now, ``mate`` will only be set to ``true`` if the ``Otter`` object has an age greater than 2. As you can see in the console output from ``OtterDriver``, ``olive`` is 6, so she did find a mate. 

.. note:: This method and indeed all properties can also be called directly as methods (since that's what they are, under the covers), but property syntax is easier to read.


Normal methods
==============

Beyond constructors and properties, a class can have any 
number of other methods, as discussed in the previous :ref:`Methods` tutorial.

Recall that the ``Otter`` class has a method called ``goFishing()``, repeated below:

.. code-block:: shadow 
    
    public goFishing() => (int)
    {
        int fish;
        if (mate)
        {
            fish = 10;
        }
        else
        {
            fish = 5;
        }
        return fish;
    }	


The method takes in no parameters and returns an ``int`` representing the number of fish caught. If the ``Otter`` object the method is called on has a mate, it catches twice the number of fish. As seen in **Line 6** of the ``OtterDriver`` class, we call this method using normal method syntax: 

.. code-block:: shadow

	objectName.methodName(parameters);


.. note:: The object's name must always be used when calling a method on a *different* object. However, if we want to call a method on the same object as the method we're currently in, the ``objectName.`` can be left off (or can be replaced with ``this.``).  

Packages
========

*Packages* in Shadow are a means of organizing groups of classes that are commonly used together. A normal Shadow class should be written in its own file, whose name ends with ``.shadow``.  These files should be put in the same folder if they're in the same package.

A few packages are worth mentioning because they're used all the time. For example, the ``shadow:standard`` package contains essential classes, interfaces, singletons, and exceptions (to be explained in later tutorials) needed for any Shadow program. These types do not need to be explicitly imported because the compiler will do so automatically. Other built-in Shadow packages are listed below (as described in the `Shadow API <http://shadow-language.org/documentation/$overview.html>`__). 

* Package ``shadow:io`` contains fundamental types used for input and output, both for the console and for file and path manipulation.

* Package ``shadow:natives`` contains classes and exceptions used to interact with C code.

* Package ``shadow:utility`` contains basic data structures and utility classes that are useful in many different kinds of programs.

While these are packages fundamental to the Shadow language, what if you wanted to create your own package? For example, you might be wondering what package the sample programs for these tutorials are in. If not specified in the class header, classes are stored in the ``default`` package. Now that we've introduced packages,  we'll put all future programs in a ``tutorials`` package.

First, we'll create a folder called ``tutorials``. Inside this folder we can have multiple other folders to hold different classes. For example, inside the ``tutorials`` folder, we could make a folder called ``variables``. Inside this folder, we could put all the programs we have relating to variable examples, making it a subpackage of the ``tutorials`` package. But how do we designate the package in class headings? 

Let's pretend we made a class called ``VariableClass``. Instead of the class header saying ``class VariableClass``, we should now write ``class tutorials:variables@VariableClass``. 

The package name is ``tutorials:variables`` (exactly matching the folder names), and the class name is ``VariableClass``. The class name must appear after the ``@`` symbol. 

It's always a good idea to put your code into packages to stay organized. From now on, packages will be incorporated into our example programs.

If classes are in the same package, they can refer to each other's names without using an ``import`` statement.  However, if you want to use outside classes (with the exception of those in ``shadow:standard``), one approach is to use an ``import`` statement at the top of your program.  We have seen this many times, since most of our code has needed to use the ``Console`` singleton from the ``shadow:io`` package:

.. code-block:: shadow

	import shadow:io@Console;
	
Using an ``import`` statement is the most common and convenient way of referring to a class from another package, but it's also possible to use its *fully qualifed name*.  If you don't use an ``import`` statement, you can refer to a class using its whole name, including packages.  Thus, you could type out ``shadow:io@Console`` everytime you wanted to refer to ``Console``.  This approach is sometimes required when you need to import two different classes that have the same name.
