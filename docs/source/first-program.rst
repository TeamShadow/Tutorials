Getting Started - Your First Shadow Program 
-------------------------------------------

In accordance with programming tradition, the first program demonstrated will print the message ``"Hello, World!"``

.. code-block:: shadow 
    :linenos: 
	
    // This program prints out "Hello, World!"
    import shadow:io@Console;

    class HelloWorld
    {
        public main( String[] args ) => ()
        {
            Console.printLine("Hello, World!");
        }
    }

Although the function of this code is relatively simple, it contains several important structural elements. Let's examine each section of code independently.

Comments
^^^^^^^^

The very first line in the program serves as a *comment*. Comments allow an author to annotate code with relevant information. 
In practice, comments are used to describe the function of a segment of code or to provide important information about the program. There are two (really three) different rules which define comments:

* Anything between // and the end of the line will be ignored
* Anything between /* and */ will be ignored - even across multiple lines

.. code-block:: shadow
    :linenos: 

    /*
     * None of this text will be compiled.
     * Not this line.
     * Not this line either.
     */

Comments are only present within the source code of a program. Neither the compiler nor the end-product executable will be impacted by comments. The third kind of comment is a documentation comment which contains specially marked-up information about code that can be used to automatically generate documentation. A documentation comment looks like the second kind of comment except that it begins with /** instead of /*.

Importing Packages with ``import``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: shadow

    import shadow:io@Console;

The ``import`` keyword allows the use of code stored in other locations. For organizational purposes, external code can be stored within groupings called packages. In this case, we are using the class ``Console`` from the package ``shadow:io``. Additionally, ``io`` is a subpackage (a package within another package) of ``shadow``. Subpackages are accessed from within their superpackages via the ``:`` operator. Once inside the correct package, individual classes are accessed with the ``@`` operator.


To import all classes within a particular package, you can leave off a particular class at the end. If access to the entire contents of ``io`` was desired, the following statement could be used:

.. code-block:: shadow

    import shadow:io;

Defining a Class
^^^^^^^^^^^^^^^^
.. code-block:: shadow
    :linenos: 

    class HelloWorld 
    {
         ...
    }

The first line in this segment declares a class named ``HelloWorld``. The definition of ``HelloWorld`` begins on the following line with a left brace (``{``) and ends several lines later with a corresponding right brace (``}``). All methods and variables declared in this space become members of ``HelloWorld``. All code in Shadow must be encapsulated within a class.

The ``main`` Method
^^^^^^^^^^^^^^^^^^^^
.. code-block:: shadow
    :linenos: 

    public main( String[] args ) => ()
    {
        ...
    }


While this segment demonstrates a typical *method* definition, it is also the definition of a special-case method known as the *main method*. In Shadow, most code is written inside of methods; thus, most operations (such as printing text, changing variable values, or calling other methods) can only take place within methods. In addition, a method may be given data as *parameters* and may *return* data to its caller.


The statement ``public main( String[] args ) => ()`` specifies a number of attributes for a method named ``main()``, all of which form the method's particular *signature* when taken as a whole. To distinguish a method from a variable of the same name, we always put parentheses after the method name. The specific structure and meaning of a method declaration will be explained in later tutorials.

Aside from being a member method of ``HelloWorld, main()`` serves a unique purpose. In order to compile an executable program, a ``main()`` method must be present somewhere within the program. The execution of a program always begins within its ``main()`` method, from which other methods may be called. Put simply, it's the starting point of the program.

Printing Text
^^^^^^^^^^^^^
.. code-block:: shadow

    Console.printLine("Hello, World!");

Finally, nested within both the ``HelloWorld`` class and the ``main()`` method, is the code which actually performs the intended function of the program.
      
The ``printLine("Hello, world!")`` portion of this line calls a method named ``printLine()`` with the parameter ``"Hello, World"``. In turn, this causes the text ``"Hello, World"`` to be printed to the screen. But what is the purpose of the ``Console`` portion?

Once again, the syntax in this statement represents a special case. It's worth remembering that methods are members of their surrounding class. In addition, methods can only be called from an existing *instance* of their class, known as an object. An object must be created prior to calling any member methods.

``Console``, however, is a special kind of class called a singleton. This means that only one ``Console`` object can exist within the entire program (in reality, within an individual thread of the program). Normally, an object is created using the ``create`` keyword. However, a singleton is created in the first method that uses it. Any later uses of the singleton will retrieve the existing object. In this case, the ``Console`` command gives us access to the ``Console`` object which has the ability to print out information using its ``printLine()`` method described above. Shadow syntax requires that the name of an object and the name of the method that is being called are separated by a dot.
