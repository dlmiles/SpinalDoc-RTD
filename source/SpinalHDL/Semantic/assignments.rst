.. role:: raw-html-m2r(raw)
   :format: html

Assignments
===========

Assignments
-----------

There are multiple assignment operators:

.. list-table::
   :header-rows: 1
   :widths: 1 5

   * - Symbol
     - Description
   * - ``:=``
     - Standard assignment, equivalent to ``<=`` in VHDL/Verilog.
   * - ``\=``
     - Equivalent to ``:=`` in VHDL and ``=`` in Verilog. The value is updated instantly in-place.
   * - ``<>``
     - Automatic connection between 2 signals or two bundles of the same type. Direction is inferred by using signal direction (in/out). (Similar behavior to ``:=``\ )

When muxing (for instance using ``when``, see :doc:`when_switch`.), the last
valid standard assignment ``:=`` wins. Else, assigning twice to the same assignee
results in an assignment overlap (see :doc:`../Design errors/assignment_overlap`).

.. code-block:: scala

   val a, b, c = UInt(4 bits)
   a := 0
   b := a
   //a := 1 // this assignment would overlap with a := 0 and take priority
   c := a

   var x = UInt(4 bits)
   val y, z = UInt(4 bits)
   x := 0
   y := x      // y read x with the value 0
   x \= x + 1
   z := x      // z read x with the value 1

   // Automatic connection between two UART interfaces.
   uartCtrl.io.uart <> io.uart

It also supports Bundle assignment (convert all bit signals into a single bit-bus of suitable width of type Bits, to then use that
wider form in an assignment expression).  Bundle multiple signals together using ``()`` (Scala Tuple syntax) on both the left hand
side and right hand side of an assignment expression.

.. code-block:: scala

   val a, b, c = UInt(4 bits)
   val d       = UInt(12 bits)
   val e       = Bits(10 bits)
   val f       = SInt(2  bits)
   val g       = Bits()

   (a, b, c) := B(0, 12 bits)
   (a, b, c) := d.asBits
   (a, b, c) := (e, f).asBits           // both sides
   g         := (a, b, c, e, f).asBits  // and on the right hand side

It is important to understand that in SpinalHDL, the nature of a signal (combinational/sequential) is defined in its declaration, not by the way it is assigned.
All datatype instances will define a combinational signal, while a datatype instance wrapped with ``Reg(...)`` will define a sequential (registered) signal.

.. code-block:: scala

   val a = UInt(4 bits)              // Define a combinational signal
   val b = Reg(UInt(4 bits))         // Define a registered signal
   val c = Reg(UInt(4 bits)) init(0) // Define a registered signal which is
                                     //  set to 0 when a reset occurs

Width checking
--------------

SpinalHDL checks that the bit count of the left side and the right side of an assignment matches. There are multiple ways to adapt the width of a given BitVector (``Bits``, ``UInt``, ``SInt``):

.. list-table::
   :header-rows: 1
   :widths: 3 5

   * - Resizing techniques
     - Description
   * - x := y.resized
     - Assign x with a resized copy of y.<br/>
       Resize value is automatically inferred to match x and may widen or truncate the width.<br/>
       The inferred conversion is based on the target width on the left hand side of the
       assignment expression being resolved and obeys the same semantics as x.resize(newWidth)
       detailed below.
       The expression `x := y.resize(x.getBitsWidth bits)` might be considered equivalent.
   * - x := y.resize(newWidth)
     - Assign x with a resized copy of y to the newWidth.<br/>
       The value of newWidth may widen or truncate the width, retaining the value at the
       LSB side and padding with zero at MSB side.
   * - x := y.resizeLeft(newWidth)
     - Assign x with a resized copy of y to the newWidth.<br/>
       The value of newWidth may widen or truncate the width, retaining the value at the
       MSB side and padding with zero at LSB side.


There is one case where Spinal automatically resizes a value:

.. list-table::
   :header-rows: 1
   :widths: 4 7 10

   * - Assignment
     - Problem
     - SpinalHDL action
   * - myUIntOf_8bit := U(3)
     - U(3) creates an UInt of 2 bits, which doesn't match the left side (8 bits)
     - | Because U(3) is a "weak" bit count inferred signal, SpinalHDL resizes it automatically.
       | This can be considered to be functionally equivalent to `U(3, 2 bits).resize`


Combinatorial loops
-------------------

SpinalHDL checks that there are no combinatorial loops (latches) in your design.
If one is detected, it raises an error and SpinalHDL will print the path of the loop.
