***********
Inheritance
***********


After mastering the basics of the Shadow language and learning how classes and interfaces work, we're ready to move on to some advanced object-oriented concepts. The first we'll dive into is *inheritance*. 

As you've probably noticed, objects on their own are powerful programming tools with innumerable applications. But sometimes we want to take an existing class and add features to it without disrupting code that uses the original class.  Inheritance allows us to do exactly this: make specialized or refined versions of existing classes in order to reuse code safely.

To illustrate the value of inheritance, consider the following scenario. You are the owner of Shadow and Light, a restaurant with three Michelin stars, and you want to write a program that represents your employees. First, you start by brainstorming the attributes that *all* employees at your restaurant share:

* Name
* Wage
* Hours worked

You also want to give your employees the ability to clock in and clock out of work.

You could write a class called ``Employee`` and give it member variables and methods that correspond to the attibutes and abilities outlined above. However, your employees have many things in common, but a chef will not have the same responsibilities as a waiter or manager. So, how will you differentiate the different jobs your employees have? 

You could forgo the ``Employee`` class completely and write separate classes: ``Waiter`` , ``Manager`` , and ``Chef`` . Each class would still contain all the abilities of a general employee but with some additions. While this approach is logical, it's not ideal because a lot of code will be repeated between the classes. What if there was a way for  the ``Waiter``, ``Manager``, and ``Chef`` classes to *inherit* from an ``Employee`` class? Any code and data that all classes need could be written in this parent class, and only the details that make the ``Waiter``, ``Manager``, and ``Chef`` classes special would be written in those child classes. Using this approach, we would not have to write some of the same methods or member variable declarations repeatedly. Shadow allows us to do exactly that. 

Before we go over how to implement this example, let's define some terms used with inheritance:

* **Parent class**: A parent class, or superclass, is a class that others inherit from. In this example, the parent class is ``Employee``. 

* **Child class**: A child class, or subclass, is one that inherits methods and member variables from another class. In this example, the subclasses are ``Waiter``, ``Manager``, and ``Chef``. 

* **Is-a relationship**: We say that a child class has an *is-a* relationship with its parent class. For example, a ``Waiter`` is an ``Employee``, but not every ``Employee`` is a ``Waiter``. 

The relationships between parent classes and their children can be viewed as a tree where each child branches off from its parent.

Shadow only allows *single inheritance*.  In other words, a class can only inherit from one other class, meaning that a child class may only have one parent. The ``Waiter`` class could not inherit from both the ``Employee`` and ``Student`` classes.  However, this restriction doesn't prevent the parent class  itself from inheriting from another class. In our example, the ``Employee`` class could inherit from another class called ``Person``. Ultimately, all classes are children of the the root class ``Object``, the only class that has no parent.

Inheriting from a class
=======================

In order to understand the syntax needed to inherit from a class, the two example classes ``Employee`` and ``Waiter`` are shown below:


.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:inheritance@Employee
    {
        get String name; 
		get set int hoursWorked; 
		get double wage; 
		
		public create(String name, double wage) 
		{
			this:name = name; 
			hoursWorked = 0; 
			this:wage = wage; 	
		}
		
		public clockIn(int hours) => ()
		{
			Console.printLine(name # " is clocking in for a " # hours # " hour shift"); 
			hoursWorked += hours; 	
		}
		
		public clockOut() => () 
		{
			Console.printLine(name # " is clocking out."); 
		}
    }



And here is the ``Waiter`` class: 

.. code-block:: shadow 
    :linenos: 

    import shadow:io@Console;

    class tutorials:inheritance@Waiter is Employee
    {
        int totalTables; 
		double tips; 
		
		public create(String name, double wage) 
		{
			super(name, wage); 
			tips = 0.0; 
			totalTables = 0; 
		}
		
		public waitTables(int tables) => () 
		{
			Console.printLine(this->name # " just picked up " # tables # " tables"); 
			numTables += totalTables; 	
		}
		
		public receiveTip(double tip)
		{
			tips += tip;
		}
    }


Using ``is`` for inheritance
----------------------------

By itself, there's nothing new about the ``Employee`` class. It has three member variables, one constructor, and two methods.

Now, look at the ``Waiter`` class. Notice how the class header says, ``class Waiter is Employee``. The keyword ``is`` signifies to the compiler that ``Waiter`` inherits from ``Employee``. Syntactically, this is the only thing you have to do to establish the inheritance relationship.  If no class is specified with an ``is``, the class ``Object`` is assumed to be the parent.

What's inherited?
-----------------

Now that we've established *how* to inherit from a parent class, it's important to discuss *what* exactly is inherited: the members of the parent class. All of its member variables and methods are passed on to the child. 

How does this apply to our example? Notice how ``Waiter`` *appears* to have only two member variables. In reality, it has five -- ``Waiter`` inherits the private member variables of its parent class, ``name``, ``hoursWorked``, and ``wage``. Although these private member variables are inherited, they cannot be directly used in the child class. For example, look at **Line 17** of the ``Waiter`` class. Instead of writing ``Console.printLine(name # ... )``, we must use the ``get`` property of the variable ``name`` in the child class. 


Calling parent constructors
---------------------------

In the constructor for the ``Waiter`` class, you may have noticed this unusual statement on **Line 10**: ``super(name, wage);``

When ``super()``  is called, it invokes the constructor of the parent class. However, the number and type of parameters must *exactly* match that of an existing parent constructor or you will get a compiler error. You should pay especially close attention if a parent class has multiple constructors. In our example, ``name`` is a ``String``, and ``wage`` is a ``double``, which matches the constructor in the ``Employee`` class. The member variables ``name``, ``hoursWorked``, and ``wage`` are subsequently initialized. However, ``tips`` and ``totalTables`` still need to be initialized, and this is done in the last two lines of the ``Waiter`` constructor.
 
.. warning:: If a parent class doesn't have a default constructor, which takes no parameters, you *must* make a call to ``super()`` to initialize the parent member variables explicitly.

Since the member variables of the parent class are ``private`` automatically, you could not simply say ``this:name = name;`` in the child class constructor. 

.. note:: If you make a call to ``super()`` in a child class constructor, that call *must* be the first statement in the constructor. 

Driver code using inheritance
-----------------------------

Examine the excerpt from the driver class and console output below in order to see inheritance in action:

.. code-block:: shadow 
    :linenos: 

    Employee sarah = Employee:create("Sarah" , 10.50);		
    Waiter trevor = Waiter:create("Trevor", 20.1, 50.5);		 
		 
    Console.printLine("Testing the Employee object"); 
    sarah.clockIn(7); 
    Console.printLine(); 
		 
    Console.printLine("Testing the Waiter object"); 
    Console.printLine("Hi, " # trevor->name); 
    trevor.clockIn(5);  
    trevor.waitTables(4);  

The console output: 

.. code-block:: console

    Testing the Employee object
    Sarah is clocking in for a 7 hour shift

    Testing the Waiter object
    Hi, Trevor
    Trevor is clocking in for a 5 hour shift
    Trevor just picked up 4 tables

As seen in the first few lines of the driver class, there is nothing syntactically different about creating either an ``Employee`` object or a ``Waiter`` object. In **Line 9**, notice the way that we access the ``name`` property inherited from the parent class: ``trevor->name``. Although these member variables cannot be directly accessed in the child class itself, ``get`` and ``set`` properties from the parent class can still be used on child class objects.  Similarly, on **Line 10** we can call the parent method ``clockIn()`` even though it was not defined in the ``Waiter`` class. Because it's inherited, we can call it on any ``Waiter`` object. 

Although we only showed implementations for ``Employee`` and ``Waiter``, you can practice inheritance by implementing the ``Chef`` and ``Manager`` classes.


Inheriting from a class and implementing interfaces
---------------------------------------------------

It's possible for a class to inherit from a parent class and also implement one or more interfaces. Although a class can implement multiple interfaces, it can only directly inherit from one other class. This can be confusing, since both relationships use the keyword ``is``. 

If a class inherits from another class, the parent class must come first after the ``is``, followed by the interfaces it implements in any order, separated by ``and``. For example:

.. code-block:: shadow 
    
    class Beyonce
		is Awesome
		and CanDance
		and CanSing

Here, the class name is ``Beyonce``, and the class it inherits from is ``Awesome``, and the two interfaces it implements are ``CanDance`` and ``CanSing``.  When a class implements several interfaces, it's Shadow convention to put the parent class and each interface on a separate, indented line.


The ``protected`` keyword
=========================

In the :ref:`Classes` tutorial, we explained the ``private`` and ``public`` modifiers, but there's also a ``protected`` modifier. If a constant or method is marked ``protected``, it means that it can only be accessed within the class itself and in any child classes. For example, if a method in the ``Employee`` class had been marked ``protected``, only code inside its children (such as ``Waiter``) and itself would be able to call it. 

In addition, you can also create ``protected`` ``get`` and ``set`` properties. Applying ``get`` and ``set`` modifiers to member variables creates ``public`` properties by default, so ``protected`` versions must be written by hand. See the three short classes below: 

.. code-block:: shadow 

    class tutorials:inheritance@Hello
    {
        get String word = "hello"; 
	
		protected set word(String word) => ()
		{
			this:word = word; 
		}
    }

.. code-block:: shadow 
    
    class tutorials:inheritance@Bonjour is Hello 
    {
        public speakFrench() => ()
		{
			this->word = "bonjour"; 
		}
    }

.. code-block:: shadow 
    :linenos:

    import shadow:io@Console;

    class tutorials:inheritance@Language
    {
        public main(String[] args) => ()
		{ 
			Hello hello = Hello:create(); 
			Console.printLine(hello->word);
			
			Bonjour bonjour = Bonjour:create(); 
			bonjour.speakFrench();
			Console.printLine(bonjour->word); 	
		}
    }

Note that class ``Bonjour`` inherits from ``Hello``. This means that, unless ``speakFrench()`` is called, the member variable ``word`` will contain the value ``"hello"`` in ``Bonjour`` objects. But we do call the ``speakFrench()`` method on **Line 11**, which causes the ``bonjour`` object to use the ``protected`` ``set`` property, changing its member variable ``word`` to ``"bonjour"``. We could *not* have used this ``set`` property in the driver class ``Language`` because it's marked ``protected`` in the parent class ``Hello``.

Method overriding
=================

In many cases, the methods that a parent class provides work perfectly for a child class.  However, there are situations when the child class needs to change the method, adding different functionality. This process, in which the programmer provides a new implementation for a method inherited from a parent class, is called *method overriding*. In order to properly override a method, the overridden method header must match the header of the original method. The method body may -- and should -- be different.

If a parent method is marked ``readonly``, overridden versions in child classes must also be marked ``readonly``.  It's possible to make the visibility of an overridden method broader, marking the child method ``public`` when the parent method was ``private``, but it's illegal to do the reverse, making the visibility of a method narrower.

A commonly overridden method is the ``toString()`` method, which gives a ``String`` representation of the object. Overriding the ``toString()`` method was discussed in an :ref:`earlier tutorial <The \`\`toString()\`\` method>`.

Children inherit the methods of their parents, and most inherited methods can be overridden. In our ``Employee`` and ``Waiter`` class examples above, ``Waiter`` inherits the methods ``clockIn()`` and ``clockOut()`` from ``Employee``. In order to use these methods (as defined in ``Employee``) on a ``Waiter`` object named ``waiter``, all you would need to do is write ``waiter.clockOut()``. However, the ``Waiter`` class has a ``tips`` member variable.  What if we need to reset the ``tips`` variable to ``0.0`` whenever a waiter clocks in?  We could override the ``clockIn()`` method in ``Waiter`` as shown below: 

.. code-block:: shadow 

    public clockIn(int hours) => ()
	{
		Console.printLine(this->name " is clocking in for a " # hours # " hour shift"); 
		this->hoursWorked += hours; 	
		tips = 0.0;
	}

Note that this method's header exactly matches the header of the ``clockIn()`` method in the ``Employee`` class. If the method had merely had the wrong return types or had been ``private`` instead of ``public``, there would have been a compiler error.  On the other hand, if we had written a method that took different parameters, we would have created a new overloaded method instead of overriding an existing method.

.. note:: Despite the similar names, the method overriding described above has nothing to do with method overloading, in which multiple methods have the same name but different parameter types.  It is possible for a class to do both method overriding and method overloading.  If an overloaded method is overridden, only the the method with matching parameters is overridden.


It's useful to note that in addition to constructors, the ``super`` keyword can also be used to call the parent class method of a method you have overridden. In the overridden ``clockIn()`` method above, we are mostly just repeating code from the parent class method.  We could shorten the code (and reduce the chances that we made an error copying it over) by calling the parent ``clockIn()`` method defined in ``Employee`` before resetting ``tips``: 

.. code-block:: shadow 

    public clockIn(int hours) => ()
	{
		super.clockIn(hours);
		tips = 0.0;
	}
	
.. note:: Although we can refer to parent methods using the ``super`` keyword, it isn't possible to refer to methods from earlier ancestors.

The ``locked`` keyword
----------------------

Some methods should *not* be overridden because their behavior needs to be fixed and predictable.  By marking a method ``locked``, children of the class cannot override that method. In other words, the implementation of that method cannot change. Under some circumstances, the compiler can call  ``locked`` methods using static dispatch instead of dynamic dispatch, resulting in slightly faster code.

As an example, if we wanted to make it so that the ``clockOut()`` method described above in the ``Employee`` class works exactly the same for all employees, we could define it in this way:

.. code-block:: shadow 

	public locked clockOut() => () 
	{
		Console.printLine(name # " is clocking out."); 
	}
	
It's also possible to mark a class header with the ``locked`` keyword.  It's impossible to inherit from classes that have been marked ``locked``.  ``String`` is an example of such a class.  The behavior of ``String`` is too important for it to be replaced by child classes that might do unexpected things.