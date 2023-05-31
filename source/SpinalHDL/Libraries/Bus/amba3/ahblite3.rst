
AHB-Lite3
=========

Characteristics
---------------

 * Based on AMBA 3 AHB-lite specification.
 * Supports only a single master, compared to AMBA 2 AHB-lite that came
   before, so there is a related signal count reduction due to this.
 * Shared HWDATA and HADDR lines, address decoder asserts HSEL line
   that is non-shared per device endpoint.
 * Separate HWDATA (to downstream device) and HRDATA (from downstream device)
   data path signals, so no tri-state support and interconnect may need to
   multiplex HRDATA.
 * Burst transfer mode capable.
 * Wide data bus configurations are possible in bits^2, such as 64 through to 1024 bits.


Configuration and instantiation
-------------------------------

First each time you want to create a AHB-Lite3 bus, you will need a configuration object. This configuration object is an ``AhbLite3Config`` and has following arguments :

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
     - Width of HADDR (byte granularity)
   * - dataWidth
     - Int
     - 
     - Width of HWDATA and HRDATA


There is in short how the AHB-Lite3 bus is defined in the SpinalHDL library :

.. code-block:: scala

   case class AhbLite3(config: AhbLite3Config) extends Bundle with IMasterSlave {
     //  Address and control
     val HADDR = UInt(config.addressWidth bits)
     val HSEL = Bool()
     val HREADY = Bool()
     val HWRITE = Bool()
     val HSIZE = Bits(3 bits)
     val HBURST = Bits(3 bits)
     val HPROT = Bits(4 bits)
     val HTRANS = Bits(2 bits)
     val HMASTLOCK = Bool()

     //  Data
     val HWDATA = Bits(config.dataWidth bits)
     val HRDATA = Bits(config.dataWidth bits)

     //  Transfer response
     val HREADYOUT = Bool()
     val HRESP = Bool()

     override def asMaster(): Unit = {
       out(HADDR,HWRITE,HSIZE,HBURST,HPROT,HTRANS,HMASTLOCK,HWDATA,HREADY,HSEL)
       in(HREADYOUT,HRESP,HRDATA)
     }
   }

There is a short example of usage :

.. code-block:: scala

   val ahbConfig = AhbLite3Config(
     addressWidth = 12,
     dataWidth    = 32
   )
   val ahbX = AhbLite3(ahbConfig)
   val ahbY = AhbLite3(ahbConfig)

   when(ahbY.HSEL) {
     //...
   }

Variations
----------

There is an AhbLite3Master variation. The only difference is the absence of the ``HREADYOUT`` signal. This variation should only be used by masters while the interconnect and slaves use ``AhbLite3``.
