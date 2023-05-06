
Attributes, Tags and Annotations
================================

Introduction
------------

There are a number of mechanisms to annotate HDL artifacts with attributes,
this section tries to list all those available in the system and their
purpose and use cases.


.. code-block:: scala

   class MyClass extends Component {
     ...
     val io = new Bundle {
        val signal = Reg(Bool())
     }
   }


Generic attribute methods:

.. code-block:: scala

    val signal = Bool() addAttribute(AttributeFlag(name="my_flag = 123")) // could be just "my_flag"

.. code-block:: verilog

    (* my_flag = 123 *) wire signal;


Generic attribute methods:

.. code-block:: scala

    val signal = Bool() addAttribute(AttributeString(name="with_string", value="TRUE"))

.. code-block:: verilog

    (* with_string="TRUE" *) wire signal;


Generic attribute methods:

.. code-block:: scala

    val signal = Bool() addAttribute(AttributeInteger(name="with_integer", value=42))

.. code-block:: verilog

    (* with_integer=42 *) wire signal;


Multiple attribute methods:

.. code-block:: scala

    val signal = Bool() addAttribute(AttributeInteger(name="with_integer", value=42)) addAttribute(AttributeFlag("my_flag"))

.. code-block:: verilog

    (* with_integer=42 *) (* my_flag *) wire signal;


Multiple attribute methods (alternative methods):

.. code-block:: scala

    val signal = Bool() addAttribute(AttributeInteger(name="with_integer", value=42, kind=COMMENT_ATTRIBUTE)) addAttribute(AttributeFlag("my_flag", kind=COMMENT_ATTRIBUTE))

.. code-block:: verilog

    /* with_integer=42 */ /* my_flag */ wire signal;


Well-known attibutes
--------------------

KeepAttribute

.. code-block:: scala

    val signal = Bool() addAttribute(KeepAttribute)

.. code-block:: verilog

    (* keep *)(* synthesis syn_keep = 1 *)(* syn_keep *) wire signal;


Table of Tags
-------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 80 100

   * - Label
     - Type
     - Details
     - Notes
   * - reset
     - DataAssign??
     - 
     - 
   * - init
     - InitAssign
     - data.init(0)
     - 
   * - default
     - DefaultTag
     - 
     - 
   * - initial
     - InitialAssign
     - 
     - 
   * - randomBoot
     - 
     - data.randBoot()
     - This is only used for Simulation initialization purpose to assign a random value on startup, not HDL.   NOT-TRUE?: May cause $urandom to be emitted in verilog outputs.
   * - unusedTag
     - 
     - data.allowPruning()
     - Hint this signal is elegible for pruning by default at SpinalHDL elaboration phase.
   * - allowAssignmentOverride
     - 
     - data.allowOverride()
     - | Inhibits Design rule checking, where one assignment overlaps another assignment completely.
       | Allow a Data assignments to be overriden, See Design+errors/assignment_overlap.html
   * - allowDirectionLessIoTag
     - 
     - data.AllowDirectionLessIo()
     - Allow a Data of an io Bundle to be directionless.  See Design+errors/iobundle.html
   * - AllowPartialAssignedTag
     - 
     - data.AllowPartialyAssigned()
     - Mem.scala
   * - AllowMixedWidth
     - 
     - MemSymbolesTag
     - Allow a register to be partially assigned
   * - unsetRegIfNoAssignementTag
     - 
     - data.allowUnsetRegToAvoidLatch()
     - Allow a register to have only an init (no assignments). See Design+errors/unassigned_register.html#register-with-only-init
   * - noCombinatorialLoopCheck
     - 
     - data.noCombLoopCheck()
     - Disable combinational loop checking for thie Data.  See Design+errors/combinational_loop.html
   * - noBackendCombMerge
     - 
     - data.noBackendCombMerge()
     - Put the combinational logic driving this signal in a separate process
   * - allowOutOfRangeLiterals
     - 
     - 
     - 
   * - noInit
     - 
     - 
     - 
   * - IfDefTag(cond: String)
     - 
     - 
     - 
   * - CommentTag(comment: String)
     - 
     - 
     - 
   * - simPublic
     - 
     - data.SimPublic()
     - 
   * - ExternalDriverTag
     - 
     - 
     - 
   * - canSimplifyHost
     - 
     - data.canSimplifyIt
     - Can this data be simplified ?
   * - 
     - 
     - 
     - 


Table of internal tags
----------------------

Internal Implementation Details Tags subject to change between any release including patch level changes.

.. list-table::
   :header-rows: 1
   :widths: 20 20 80 100

   * - Label
     - Type
     - Details
     - Notes
   * - 
     - 
     - 
     - 
   * - tagAutoResize
     - 
     - data.resize()
     - 
   * - tagTruncated
     - 
     - 
     - 
   * - PropagatePullNameTag
     - 
     - propagatePullName()
     - Removed feature.
   * - ClockDomainTag
     - 
     - 
     - 
   * - ClockDomainReportTag
     - 
     - 
     - 
   * - ClockDomainBoolTag
     - 
     - 
     - internal super-class
   * - ClockTag
     - 
     - 
     - 
   * - ResetTag
     - 
     - 
     - 
   * - ClockEnableTag
     - 
     - 
     - 
   * - ClockSyncTag
     - 
     - clockDomain.setSynchronousWith(clockDomainB)
     - Inhibit Cross Clock Domain checking, with all items associated with clockDomainB.  See Design+errors/clock_crossing_violation.html
   * - ClockDrivedTag
     - 
     - 
     - 
   * - ClockDriverTag
     - 
     - 
     - 
   * - GenericValue
     - 
     - 
     - BlackBox generic values
   * - noNumericType
     - 
     - 
     - Transform all unsigned/signed into std_logic_vector.
   * - uLogic
     - 
     - 
     - Create a Ulogic tag used by Blackbox in order to transform std_logic into std_ulogic.
   * - addDefaultGenericValue
     - 
     - 
     - In VHDL add the generic value in the definition of the blackbox.
   * - PhaseNextifyTag
     - 
     - 
     - 
   * - TagAFixTruncated
     - 
     - 
     - 
   * - AFixRounding(saturation: Boolean, overflow: Boolean, rounding: RoundType)
     - 
     - 
     - 
   * - crossClockDomain
     - 
     - data.addTag(crossClockDomain)
     - Inhibit Cross Clock Domain checking, with the Data it is attached to.  See Design+errors/clock_crossing_violation.html
   * - crossClockBuffer
     - 
     - 
     - 
   * - tagAFixResized
     - 
     - 
     - 
