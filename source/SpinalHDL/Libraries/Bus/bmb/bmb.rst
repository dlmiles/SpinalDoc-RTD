
BMB (Banana Memory Bus)
=======================

Characteristics
---------------

 * ???? REVIEWME
 * Less complicated than other bus types for the same feature spec
   ???? can we provide numbers ??? which metrics are less complex ???
 * It is not necessary for every slave endpoint to implement burst support / unaligned
   access support when one or more slaves do implement it.
 * State-less adapter made possible via the context feature
   ??? can we describe this is less BMB specific jargon ???
 * The interconnect can support out of order bus transactions


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
     - None `(must be specified)`
     - Width in bits of ADDR (byte granularity)
   * - dataWidth
     - Int
     - None `(must be specified)`
     - Width in bits of DATA (multiple of 8 bits)


Variations
----------


Example Project Usage
---------------------

Saxon SOC project uses this Bus at https://github.com/SpinalHDL/SaxonSoc#bmb-spec-wip

The specification for bus largely sits within the SpinalHDL code base.
