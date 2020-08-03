Using the Shadow Compiler
-------------------------

*Note: This tutorial is for version 0.7.5 of the Shadow compiler and may not be accurate for other versions.*

The Shadow compiler is required in order to transform written Shadow programs into their executable counterparts. It provides a number of helpful features, including descriptive error-messages and a simple, automated build system. The compiler, along with detailed installation instructions, is available on the **Downloads** page.

Getting Started
^^^^^^^^^^^^^^^

Like many utilities, the Shadow compiler is operated via the command-line. Access to the command-line varies by platform, but is usually available through a terminal emulator. Running the install script included with the Shadow compiler adds its location to the system's ``PATH`` variable, allowing it to be run from any directory with the command ``shadowc``.

For simple programs, compilation can be invoked with the following command:

.. code-block:: shadow

    shadowc Main.shadow 
	
In this case, ``Main.shadow`` is a Shadow source file containing a ``main`` method. This ``main`` method will become the entry point of the program in the resulting executable. The compiler will automatically attempt to resolve any dependencies, both locally and within the standard library.

By default, the resulting executable will bear the same name as the source file (in this case ``Main.exe`` on Windows and ``Main`` on other systems). The executable name can be specified using the ``-o`` option:

.. code-block:: shadow

    shadowc Main.shadow -o UsefulProgrgam.exe 

Additional Options
^^^^^^^^^^^^^^^^^^

When run with the option ``-h`` (or ``--help``), the compiler will print a list of all available options and their descriptions. This will also occur if an invalid option or argument is specified, along with a corresponding error message. For reference, the help printout is reproduced below:

.. code-block:: console

     usage: shadowc <mainSource.shadow> [-o <output>] [-c <config.xml>]
     -c,--config <config.xml>   Specify optional configuration file
                                If shadow.xml exists, it will be checked
     -f,--force-recompile       Recompile all source files, even if
                                unnecessary
     -h,--help                  Display command line options and exit
     -i,--information           Display information about the compiler and
                                exit
     -n,--nolink                Compile Shadow files but do not link
     -o,--output <file>         Place output into <file>
     -r,--human-readable        Generate human-readable IR code
     -t,--typecheck             Parse and type-check the Shadow files
     -v,--verbose               Print detailed information about the
                                compilation process
     -w,--warning <flag>        Specify warning flags
	 

Configuration Files
^^^^^^^^^^^^^^^^^^^

**The Shadow compiler ships with tested configuration files. Outside of special cases, most users will not need to worry about creating their own configuration files. If the compiler works as desired on your platform, this section can safely be ignored.**

In some cases, it is necessary or convenient to specify additional options in a configuration file. Such cases include cross-compiling (compiling for another platform) and the addition of non-typical include paths (those which the compiler won't look through on its own). When no configuration file is present, the compiler makes assumptions (either through default values or automatic detection) about the appropriate settings for the given platform. If the file is present but does not make use of all possible options, the same process will be applied to the unspecified fields.

Configuration files are XML-based, and may be passed to the compiler following the option ``-c`` (or ``--config``). If the option is not used, the compiler will check for the file ``shadow.xml``, first in the directory of the given source file and then in the compiler executable's directory. If neither file exists, the compiler will fall back on default settings. The following is a complete description of all legal tags and attributes within a Shadow configuration file:
	
**Tags:**
	* ``<shadow>`` - The outermost tag of the file, used to specify platform information for the compilation process. (*required*)
	* ``<system>`` - Used to specify the location of the Shadow standard libraries. Only one standard path may be specified. (*optional*)
	* ``<include>`` - Used to define additional search paths for resolving dependencies (``import`` statements). If any include paths are specified, the path ``<include>.</include>`` must also be. (*optional*)

**Attributes of the <shadow> tag:** *Note: All of the following attributes are entirely optional, and will be determined by the compiler if absent. The default values are generally accurate, and should not be overridden unless necessary.*

	* ``os`` - The operating system on which the program is being compiled and on which it will run. This determines the choice of system calls to be used by the standard libraries, and may also determine the linker to be used by the compiler (``gcc`` or ``clang``). Any name may be specified, but only those containing the text "Windows", "Mac", and "Linux" currently receive special treatment. All others are interpreted as "Linux".
	* ``arch`` - The addressing mode (32 or 64) used by the target platform's processor. This information determines pointer size and is used by Shadow's exception handling system.
	* ``target`` - The target triple used by the LLVM component of the Shadow compiler. See the **LLVM Target Triples** section for more information
	* ``link`` - The parameters to be passed to the linker.

The following example demonstrates the general structure of a Shadow configuration file:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <shadow os="Linux" arch="64" target="x86_64-unknown-linux-gnu">
      <system>/home/dave/standardlibs</system>
      <import>.</import>
      <import>/usr/local/lib/extralibs</import>
    </shadow>

In the example above, the user has explicitly specified some platform and directory information. Within the ``<shadow>`` tag, the ``os="Linux"`` attribute ensures that the compiler will use Linux-compliant system calls for standard library functions. The attribute ``arch="64"`` ensures that 64-bit addressing is used. Although the **target** attribute seems to contain redundant information, it represents a special set of information used by the compiler's LLVM backend (specifically, the last stages of compilation which output platform-specific machine code). See the section on **LLVM Target Triples** for more information.

The ``<system>`` tag is used to explicitly specify that the Shadow standard library is located in ``/home/dave/standardlibs/.`` Within this directory, the compiler looks for the directory ``shadow/`` containing the libraries in question. The tag ``<import>.</import>`` tells the compiler to resolve import statements by searching directories relative to the file being compiled. This tag must always be specified **if** any other include paths are specified, or the standard libraries (and presumably most user programs) will fail to resolve dependencies. Additional paths, such as the one specified in ``<import>/usr/local/lib/extralibs</import>`` will also be searched when resolving dependencies.

**Configuration for Microsoft Windows**

The configuration file below describes the platform attributes for compiling on (and for) Microsoft Windows. Because MinGW does not support 64-bit compilation, it is important to prevent the compiler from attempting to do so.

.. code-block:: shadow
    <?xml version="1.0" encoding="UTF-8"?>
    <shadow os="Windows" arch="32" target="x86-unknown-mingw32">
    </shadow>

**LLVM Target Triples**

During compilation, the Shadow compiler uses a third party tool, the LLVM compiler, to generate the final, platform-specific machine code of an executable. Because the LLVM compiler is an external tool, it requires its own set of platform information to generate valid machine code. During compilation, the contents of the ``target`` attribute (either taken from a configuration file or automatically determined) are handed directly to the LLVM compiler. Thus, the attribute must follow the formatting of an LLVM target "triple". The following information provides some explanation of how to format these triples:

The canonical form of LLVM target triple is either ``Architecture-Vendor-OperatingSystem or Architecture-Vendor-OperatingSystem-Environment.``

	* Architecture: ``arm, mips, sparc, x86, x86_64``, etc.
	* Vendor: ``apple, pc, nvidia``, etc.
	* Operating System: ``freebsd, ios, linux, macosx, win32, windows``, etc.
	* Environment: ``gnu, android, msvc``, etc.

*Note: unknown is a valid entry in any of these fields. The most critical fields to fill in are those for architecture and operating system.*

Many additional, arguably more obscure options exist for each field. See the beginning of the **header file** from LLVM's triple-handling code for a more complete listing. Unfortunately, the document seems to provide incomplete information (for example, the ``mingw32`` operating system attribute is not listed).

**Examples:**

	* ``x86-unknown-Win32``
	* ``x86_64-unknown-Linux-GNU``
	* ``x86_64-Apple-MacOSX``

All LLVM tools are capable of automatically detecting the correct triple for a given platform. If LLVM is properly installed, the command ``llc --version`` will display information including the default triple. A compiled version of this tool comes with the Windows installation of Shadow, and can be run from the associated directory. However, the Windows platform currently has limitations. See the **Windows** section for details.


