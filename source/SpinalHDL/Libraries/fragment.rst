
Fragment
========

Specification
-------------

The ``Fragment`` bundle is the concept of transmitting a "big" thing by using multiple "small" fragments. For examples :


* A picture transmitted with width*height transaction on a ``Stream[Fragment[Pixel]]``
* An UART packet received from an controller without flow control could be transmitted on a ``Flow[Fragment[Bits]]``
* An AXI read burst could be carried by an ``Stream[Fragment[AxiReadResponse]]``

Signals defined by the ``Fragment`` bundle are :

.. list-table::
   :header-rows: 1
   :widths: 1 1 1 5

   * - Signal
     - Type
     - Driver
     - Description
   * - fragment
     - T
     - Master
     - The "payload" of the current transaction
   * - last
     - Bool
     - Master
     - High when the fragment is the last of the current packet


As you can see with this specification and precedent example, the ``Fragment`` concept doesn't specify how transaction are transmitted (You can use Stream,Flow or any other communication protocol). It only add enough information (\ ``last``\ ) to know if the current transaction is the first one, the last one or one in the middle of a given packet.

.. note::
   The protocol didn't carry a \'first\' bit because it can be generated at any place by doing \'RegNextWhen(bus.last, bus.fire) init(True)\'

Functions
---------

For ``Stream[Fragment[T]]`` and ``Flow[Fragment[T]]``\ , following function are presents :

.. list-table::
   :header-rows: 1
   :widths: 1 1 20

   * - Syntax
     - Return
     - Description
   * - x.first
     - Bool
     - Return True when the next or the current transaction is/would be the first of a packet
   * - x.tail
     - Bool
     - Return True when the next or the current transaction is/would be not the first of a packet
   * - x.isFirst
     - Bool
     - Return True when an transaction is present and is the first of a packet
   * - x.isTail
     - Bool
     - Return True when an transaction is present and is the not the first/last of a packet
   * - x.isLast
     - Bool
     - Return True when an transaction is present and is the last of a packet


For ``Stream[Fragment[T]]``\ , following function are also accessible :

.. list-table::
   :header-rows: 1
   :widths: 1 1 1

   * - Syntax
     - Return
     - Description
   * - x.insertHeader(header : T)
     - Stream[Fragment[T]]
     - Add the ``header`` to each packet on ``x`` and return the resulting bus


Example
-------

.. code-block:: scala

   // FIXME example: single stream fragment transaction, showing tx and rx sides
   // FIXME example: two flow fragment tranaction, showing tx and rx sides
   // FIXME example: three stream fragment transation, showing tx and rx sides
   val inputStreamFragment = master port Stream (Fragment(Bits(8 bits)))



This ``extender`` provides several status signals, such as ``working``, ``last``, ``done`` where ``working`` means there is one input transfer accepted and in-progress, ``last`` indicates the last output transfer is prepared and waiting to complete, ``done`` become valid represents the last output transfer is fireing and making the current input transaction process complete and ready to start another transaction.

.. wavedrom::

  { "signal": [
    { "name": "clk",         "wave": "p........." },
    { "name": "inputStream",        "wave": "x3x.....4x", "data": ["T1", "T2"] },
    { "name": "count",        "wave": "x3x.....4x", "data": ["2", "4"] },
    { "name": "outputStream",       "wave": "x..2x2x.2x", "data": ["D1", "D2", "D3"] },
    { "name": "working",      "wave": "0.1......."},
    { "name": "done",      "wave": "0.......10"},
    { "name": "first",      "wave": "0.1.0....."},
    { "name": "last",      "wave": "0.....1..0"},
  ]}

.. note::

   If only count for output stream is required then use ``StreamTransactionCounter`` instead.
