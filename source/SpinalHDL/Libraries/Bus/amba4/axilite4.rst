
AXI-Lite4
=========

Characteristics
---------------

 * Does not support AXI4 burst mode


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
     - Width in bits of DATA (maybe 32 or 64 bits)
   * - readIssuingCapability
     - Int
     - -1
     - 
   * - writeIssuingCapability
     - Int
     - -1
     - 
   * - combinedIssuingCapability
     - Int
     - -1
     - 
   * - readDataReorderDepth
     - Int
     - -1
     - 


Variations
----------
