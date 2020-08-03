Inheritance
-----------

The Concept
^^^^^^^^^^^

After mastering the basics of the **Shadow** language and learning how classes and interfaces work, we are now ready to move on to some more advanced **Object-Oriented** concepts. The first we will dive into is **inheritance**. 

As you have probably already noticed, objects on their own are very powerful programming tools, with innumerable applications. Inheritance introduces a whole new level of complexity. In order to **conceptually** understand what we mean by inheritance, consider the following scenario: 

You are the owner of a five-star restaurant, "Shadow and Light", and you want to write a program that represents your employees. First, you start by brainstorming the things or abilities that *all* employees at your restaurant share.

**Employee**

* Name
* Wage
* Hours worked
* Clock-in 
* Clock-out

You could then easily write a class called ``Employee`` and give it member variables and methods that correspond to the abilities outlined above. However, although your employees do have things in common, a chef will not have **all** the same responsibilities as a waiter or manager. So, how will you differentiate the different jobs your employees have? 

You *could* forgo the ``Employee`` class completely and write separate classes: ``Waiter`` , ``Manager`` , and ``Chef`` . Each class would still contain all the abilities of a general employee, but with some additions. While this sounds like a logical solution, it is not very efficient because a lot of code will be repeated between the classes. What if there was a way for  the ``Waiter``, ``Manager``, and ``Chef`` classes to **extend** an ``Employee`` class, just as interfaces are implemented? That way, we would not have to rewrite methods multiple times. In **Shadow**, **this is possible** via *inheritance*. 

Before we go over how to implement this example, let’s define some basic terms in regards to inheritance. 

* **Superclass** : A superclass, or parent class, is the class that others extend from. In this example, the superclass is ``Employee``. 

* **Subclass** : A subclass, or child class, is one that extends another class, inheriting its methods and member variables. In this example, the subclasses are ``Waiter``, ``Manager``, and ``Chef``. 

* **is-a Relationship:** We say that superclasses and subclasses have an **is-a** relationship. For example, a ``Waiter`` is an ``Employee`` , but an ``Employee`` is not always a ``Waiter``. 

.. note:: In order to visualize the relationship between superclasses and subclasses, think of it as branches coming off of a tree. The superclass is the tree itself, and its subclasses are the different branches coming off of it.

**That being said, it is extremely important to note that a given class can only extend one other class**. In basic terms, this means that a child class **may only have one parent** (e.g. A ``Waiter`` cannot extend ``Employee`` **and** a ``Student`` class).  However, this does not mean that a parent class cannot extend another class (e.g. ``Employee`` *could* extend a class called ``Person``). In fact, the root class of all objects is ``Object``. 


Implementation
^^^^^^^^^^^^^^

In order to understand the syntax and implementation of extending classes, there are two example classes provided below: ``Employee`` and ``Waiter``. Glance over them first, and then we will break them down. 


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:inheritance@Employee
    {
        get String name; 
	get set int hoursWorked; 
	get double wage; 
	
	public create(String n, double w) 
	{
	    name = n; 
	    hoursWorked = 0; 
	    wage = w; 	
	}
	
	public clockIn() => ()
	{
	    Console.printLine("You are clocking in for a 5 hour shift"); 
	    hoursWorked = 5; 	
	}
	
	public clockOut() => () 
	{
	    Console.printLine("You are clocking out. Your hours go back to 0"); 
	    hoursWorked = 0; 
	}
    }



And here is the ``Waiter`` class: 

.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:inheritance@Waiter is Employee
    {
        int numTables; 
	double tips; 
	
	public create(String n, double w, double t) 
	{
	    super(n, w); 
	    tips = t; 
	    numTables = 0; 
	}
	
	public waitTables(int n) => () 
	{
	    Console.printLine(this->name # " just picked up " # n # " tables"); 
	    numTables += n; 	
	}
    }


**The Class Header** 

By itself, there is nothing new included in the ``Employee`` class. There are 3 member variables, one constructor, and two methods. If an element of the class looks unfamiliar,  you should revisit the :ref:`Classes: The Basics<Classes: The Basics>` tutorial. 

Now, look at the ``Waiter`` class. Notice how the class header says, ``class Waiter is Employee``. The keyword ``is`` signifies to the compiler that ``Waiter`` *extends* employee. Syntactically, this is the only thing you have to do in order to "establish" this line of inheritance. 

**What, Exactly, is Inherited?**

Now that we have established, *how*, to extend a class, it is important to discuss *what* exactly is inherited: the members of the parent class. In other words, all of its member variables and methods are "passed on" to the child. 

How does this apply to our example? Notice how ``Waiter`` *appears* to only have 2 member variables. In reality, it has 5 -- ``Waiter`` inherits the private member variables of its parent class, ``Employee``. Although these private member variables are inherited, they cannot be directly used in the child class. For example, look at **Line 17** of the ``Waiter`` class. Instead of writing ``Console.printLine(name # … )``, we must use the ``get`` property of the variable ``name`` in the child class. 


**The Constructor**

In the ``Waiter`` class, you may have noticed that within its constructor, **Line 10** has the following statement: ``super(n, w);`` What does the ``super()`` method call do? When ``super()``  is called, it invokes the constructor of the parent class. However, the number and type of parameters must **exactly** match that of an existing parent constructor, or you will get a compile error. You should especially pay attention to this if a class has multiple constructors. So, in our example, ``n`` is a ``String``, and ``w`` is a ``double`` , which matches the constructor in the ``Employee`` class. The member variables ``name``, ``hoursWorked``, and ``wage`` are subsequently initialized. However, ``tips`` and ``numTables`` still need to be initialized, and this is done in the last two lines of the ``Waiter`` constructor. 

It is very important to note that if you are using ``super()`` in a child class constructor, **it must be the first statement in the constructor**, or you will get a compile error. Since the member variables of the parent class are ``private`` automatically, you could not simply say ``name = n;`` in the child class constructor. 

**The Driver Class** 

Examine the excerpt from the driver class and console output below in order to see **inheritance** in action. 

.. code-block:: shadow 
    :linenos: 

    Employee sarah = Employee:create("Sarah" , 10.50); 
		
    Waiter trevor = Waiter:create("Trevor", 20.1, 50.5); 
		 
		 
    Console.printLine("Testing the Employee object"); 
    sarah.clockIn(); 
    Console.printLine(); 
		 
    Console.printLine("Testing the Waiter object"); 
    Console.printLine("Hi, " # trevor->name); 
    trevor.clockIn();  
    trevor.waitTables(4);  

The console output: 

.. code-block:: console

    Testing the Employee object
    You are clocking in for a 5 hour shift

    Testing the Waiter object
    Hi, Trevor
    You are clocking in for a 5 hour shift
    Trevor just picked up 4 tables

As seen in the first few lines of the driver class, there is nothing syntactically different about creating either an ``Employee`` object or ``Waiter`` object. In **Line 11**, notice the way that we access the ``private`` member variable ``name`` inherited from the parent class: ``trevor->name``. Although these member variables cannot be directly accessed in the child class itself, the properties ``get`` and ``set`` can still be used to access/change their values.  Lastly, look at **Line 12**. Although the method ``clockIn()`` is not explicitly defined/overridden in the ``Waiter`` class, it is still inherited and can be called on any ``Waiter`` object. 

Although we only showed the implementation for ``Employee`` and ``Waiter``, it would be good practice to try and implement the ``Chef`` and ``Manager`` classes as an exercise. 


``constant`` and ``protected``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Two important keywords in **Shadow** are ``constant`` and ``protected``. 

By definition, if a member variable is marked with the keyword ``constant``, this means that once it is initialized, its **value can never change**. Technically, if a member variable is ``constant``, it is no longer a member variable because it does not belong to a specific object/instance of the class. It has the same unchanging value for every object. The types that can be marked as ``constant`` are primitives, arrays, and ``String`` values. In addition, constants can be declared as ``public``, ``private``, or ``protected``, as outside classes/code may need to access/know their values. 

Now you may be asking, what does the keyword  ``protected`` mean? If a ``constant`` or method is marked as ``protected``, it means that it can only be accessed within the class itself and in any classes that extend it. Using our example from the previous section, if a method in ``Employee`` had been marked as ``protected``, only its children (e.g. ``Waiter``) and an employee object would be able to call it. 

In addition, you can also create ``protected`` ``get`` and ``set`` properties. Although ``get`` and ``set`` automatically create ``public`` accessors/mutator methods, a ``protected`` version must be created by hand. See the three short, toy classes below: 

**Class One** 

.. code-block:: shadow 
    :linenos:

    class tutorials:inheritance@Hello
    {
        get String word = "hello"; 
	
	protected set word(String w) => ()
	{
	    word = w; 
	}
    }

**Class Two**

.. code-block:: shadow 
    :linenos:

    class tutorials:inheritance@Bonjour is Hello 
    {
        public speakFrench() => ()
	{
	    this->word = "bonjour"; 
	}
    }

**Driver Class** 

.. code-block:: shadow 
    :linenos:

    import shadow:io@Console;

    class tutorials:inheritance@Language
    {
        public main( String[] args ) => ()
	{ 
            Hello hello = Hello:create(); 
            Console.printLine(hello->word);
		
	    Bonjour bonjour = Bonjour:create(); 
	    bonjour.speakFrench();
	    Console.printLine(bonjour->word); 	
	}
    }

The first thing to pay attention to is that the class ``Bonjour`` extends ``Hello``. This means that unless ``speakFrench()`` is called, the member variable ``word`` will equal the literal value "hello" for each class. However, notice in **Lines 11 and 12** that we call ``speakFrench()`` on ``bonjour`` and use the ``get`` property to display the updated value "bonjour" on the console. The important point to make here is that we were not able to use the ``set`` property in the driver class ``Language`` because it is defined as ``protected`` in the parent class ``Hello``. This means that only ``Hello`` and its children may call the ``set`` property, and it is done so in the ``speakFrench()`` method of the subclass ``Bonjour``. Using ``protected`` methods helps to promote **data encapsulation**. 

Method Overriding, Revisited 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last topic we will briefly discuss in this introduction to **inheritance** is **method overriding**. If this concept is completely new to you, it would be a good idea to review the tutorial :ref:`Method Overriding<Method Overriding>`. 

As a refresher, method overriding is when the programmer provides a new default implementation for a pre-provided method in a class. In order to properly override a method, the overridden method header must exactly match the header of the original method. The method body may -- and should -- be different.

Since subclasses inherit the methods of its superclass, it is possible to override an inherited method. In our ``Employee`` and ``Waiter`` class examples above, ``Waiter`` inherits the methods ``clockIn()`` and ``clockOut()`` from ``Employee``. In order to use these methods (as defined in ``Employee``) on a ``Waiter`` object (named ``waiter``), all you would need to do is write ``waiter.clockOut()``. However, what if the waiter works different hours than a regular employee? You could then override the ``clockIn()`` and/or ``clockOut()`` methods in ``Waiter`` as shown below: 

.. code-block:: shadow 
    :linenos:


    public clockIn() => ()
    {
        Console.printLine("You are clocking in for a 4 hour shift."); 
	this->hoursWorked = 4; 
    }

**The key part of this method is that the header exactly matches the header of the** ``clockIn()`` **method in the** ``Employee`` **class**. If it had not, you would not have successfully overridden the method and gotten a compile error. There are no requirements on what has to be different in the method body. In this case, we simply changed the length of the shift for all ``Waiter`` objects. 


It is useful to note that in addition to constructors, ``super()`` can also be used to call the parent class method of a method you have overridden. For example, in the overridden ``clockIn()`` method above, if we wanted to call the ``clockIn()`` method defined in ``Employee`` , it would look like this: 

.. code-block:: shadow 
    :linenos:

    public clockIn() => ()
    {
        super.clockIn(); 
        // some more statements
    }


The ``locked`` Keyword
^^^^^^^^^^^^^^^^^^^^^^

Another feature of Shadow is the ``locked`` keyword. When you declare a method to be ``locked``, it means that the **children of the class cannot override the method**. In other words, you don’t want the implementation of a certain method to change. Declaring a method as ``locked`` can help increase the efficiency of a program, even if just slightly. 

The method header of a ``locked`` method is as follows: 

``public locked methodName() => ()`` 


Final Note
^^^^^^^^^^


As a final note, it is important to address the syntax of the header for a class that **extends** one class, but implements one or more interfaces. Although a class can implement multiple interfaces, it can only directly extend one other class. This can be confusing, as implementing and extending both use the keyword ``is``. 

As a rule, if a class extends another class, it should be the first statement, followed by the interfaces it implements in any order (and separated by ``and``). For example, 


.. code-block:: shadow 
    
    class Testy
    is Awesome
    and CanDance
    and CanSing

Here, the class name is ``Testy``, and the class it extends is ``Awesome``, and the two interfaces it implements are ``CanDance`` and ``CanSing``. 



