
Wishbone
========

Characteristics
---------------

 * Supports classic Wishbone mode
 * Supports optional transaction TAG (separate and optional independant data, address,
   cycle-control tagging at different widths)
 * Supports optional SEL (selection bus-line)
 * Supports optional STALL (stall)
 * Supports optional LOCK (lock)
 * Supports optional ERR (error)
 * Supports optional RTY (retry)
 * Supports optional CTI (cycle type identifier)
 * Supports optional BTE (burst type extension), needed to support BURST modes.
 * ???? REVIEWME


Configuration and instantiation
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 1 1 1 2

   * - Parameter name
     - Type
     - Default
     - Description
   * - addressWidth
     - Int
     - 
     - Width in bits of ADDR (byte granularity)
   * - dataWidth
     - Int
     - 
     - Width in bits of DATA (multiple of 8 bits)
   * - selWidth
     - Int
     - 0
     -
   * - useSTALL
     - Boolean
     - false
     -
   * - useLOCK
     - Boolean
     - false
     -
   * - useERR
     - Boolean
     - false
     -
   * - useRTY
     - Boolean
     - false
     -
   * - useCTI
     - Boolean
     - false
     -
   * - tgaWidth
     - Int
     - 0
     - Tag Address width (0 to disable)
   * - tgcWidth
     - Int
     - 0
     - Tag Cycle width (0 to disable)
   * - tgdWidth
     - Int
     - 0
     - Tag Address width (0 to disable)
   * - useBTE
     - Boolean
     - false
     - Byte Type Extension support


Variations
----------

