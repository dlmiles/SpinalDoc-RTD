Project Lifecycle
=================

This page attempts to document and outline the form of a project lifecycle 
to include the features SpinalHDL can provide and assist with and what is
happening suching each stage of the process.


* checkout project

  An example of project structure to scafold your project is maintained
  at https://github.com/SpinalHDL/SpinalTemplateSbt


* sbt startup (background daemon, automatically fetches dependencies and
  libraries needed for:

   * sbt itself,
   * SpinalHDL,
   * the target project, 
   * the testing

  The items it does not fetch dependencies for are the EDA tooling
  environment for tools such as Simulation and Formal Verification (see the
  appropiate section for setup information).


* Writing the HDL implementation of your project.
  You describe the behaviour of your hardware in SpinalHDL.

  An example of a project class file can be seen at: https://github.com/SpinalHDL/SpinalTemplateSbt/blob/master/hw/spinal/projectname/MyTopLevel.scala

  You might use sbt command to confirm it is syntactically correct Scala (this does not confirm what is being describe can be elaborated).
  ``compile``


* Elaboration of HDL into a Verilog file (if you target this language in your
  EDA flow):

  ``runMain projectname.MyTopLevelVerilog``

  This step maybe perform before you begin to Simulate or Formally Verify to
  validate the design passes being able to be elaborated.

  Error can be found here (in the design) that must be addressed.  Here is a
  link to some assistance in resolving the kinds of errors that occur during
  elaboration.


* Elaboration of HDL into a VHDL file (if you target this language in your
  EDA flow):

  ``runMain projectname.MyTopLevelVHDL``

  This step maybe perform before you begin to Simulate or Formally Verify to
  validate the design passes being able to be elaborated.

  Error can be found here (in the design) that must be addressed.  Here is a
  link to some assistance in resolving the kinds of errors that occur during
  elaboration.


* SpinalHDL simulation
   
   This makes uses of a Scala/Java testing framework such as:
     * scalatest

   The framework manages Simnulation much like Unit Testing.
   Due to this the sbt command:
   ``testOnly mypackage.MyTestSim``
   can be used to run that single test class.

   An example of a test class can be seen at: https://github.com/SpinalHDL/SpinalTemplateSbt/blob/master/hw/spinal/projectname/MyTopLevelSim.scala

* SpinalHDL formal verification
   
   This makes use of a Scala/Java testing framework such as:
     * scalatest

   The framework manages Simnulation much like Unit Testing.

   An example of a formal verification test class can be seen at: https://github.com/SpinalHDL/SpinalTemplateSbt/blob/master/hw/spinal/projectname/MyTopLevelFormal.scala


* HDL code-generation.  This can be a repeat of the Verilog / VHDL
  code-generation steps above (or reuse of testcode HDL artifacts).  It is
  included again here as you may have performed multiple code-test-debug
  iterations to improve your design so you now perform your final code generation.

  Verilog codegen example:
    Can be found at the `object MyTopLevelVerilog extends App` seen at:
    https://github.com/SpinalHDL/SpinalTemplateSbt/blob/master/hw/spinal/projectname/MyTopLevel.scala
    This can be executed from sbt with ``sbt runMain projectname.MyTopLevel.MyTopLevelVerilog``

  VHDL codegen example:
    Can be found at the `object MyTopLevelVhdl extends App` seen at:
    https://github.com/SpinalHDL/SpinalTemplateSbt/blob/master/hw/spinal/projectname/MyTopLevel.scala
    This can be executed from sbt with ``sbt runMain projectname.MyTopLevel.MyTopLevelVhdl``


* Using the generated HDL (Verilog/VHDL) you can provide that to your EDA
  flow in a state that is already well simulted, well tested.  Your EDA flow
  is then expected to perform synthesis and implementation processes towards
  achieving the final hardware design.


