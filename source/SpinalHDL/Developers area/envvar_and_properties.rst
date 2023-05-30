Java Environment Variables and Properties
=========================================

Thie page attempts to document details about environment variables and
properties that affect the SpinalHDL project a different times.


Environment Variables
---------------------

These can be setup often using `export VARNAME=value` from a Linux/MacOS system shell,
or with in windows with `set VARNAME=value`.


.. list-table::
   :header-rows: 1
   :widths: 2 2 2

   * - Name
     - Default
     - Description
   * - SPINAL_TARGET_DIR
     - "."
     - Initializes SpinalConfig.defaultTargetDirectory
   * - SPINAL_SIM_WORKSPACE
     - "./simWorkspace"
     - Location of workspace for SpinalSim simulation working area.
   * - VERILATOR_BIN
     - By default `verilator_bin` is expected in the $PATH
     - Location override for the `verilator_bin` when using the Verilator Simulation backend of SpinalSim.
   * - MAKE
     - By default `make` is expected in the $PATH
     - Location overide



System Properties
-----------------

These can be setup often using the `-P` options to build tools like `sbt` or
`java`, for example `sbt -Pspinal.property.example=value clean build`.


   :header-rows: 1
   :widths: 2 2 2

   * - Name
     - Default
     - Description
   * - spinal.core.SpinalConfig.headerWithRepoHash
     - true
     - Set 'true' or 'false.  Provides default to SpinalConfig.
   * - spinal.sim.VerilatorBackendConfig.maxCacheEntries
     - 100
     - Set a 0 or positive interger number.  0 means unlimited.
   * - spinal.sim.Config.maxCacheEntries
     - 100
     - Set a 0 or positive interger number.  0 means unlimited.
   * - user.home
     - Defined by JVM from $HOME
     - 
   * - os.arch
     - Defined by JVM from runtime platform
     - Used to configure internals for Linux/MacOS/Windows runtime platform
   * - os.name
     - Defined by JVM from runtime platform
     - Used to configure internals for Linux/MacOS/Windows runtime platform
   * - java.home
     - Defined by JVM from runtime platform
     - Used to configure internals for Linux/MacOS/Windows runtime platform


