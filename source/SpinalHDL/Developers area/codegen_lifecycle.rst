Lifecycle
=========

This page attempts to document details about the internal workings of
the codegen lifecycle that exist inside SpinalHDL.


SpinalHDL Codegen (internal) Lifecycle
--------------------------------------

This section seeks to document the internal lifecycle concerning how
SpinalHDL takes Scala code and emits HDL language artifacts.

Internally there is a sequence of phases that occur.
Some of these phases can be hooked into by your project Scala code and
utilized for various purposes to assist in the task of HDL code generation.


List of Phases:

 * Phase One
 * Phase Two
 * Phase Three
 * phase: spinal.core.internals.PhaseCreateComponent
 * phase: spinal.core.internals.PhaseDummy
 * phase: spinal.core.sim.SpinalSimConfig$$anon$1
 * phase: spinal.core.sim.SimVerilatorPhase
 * phase: spinal.core.internals.PhaseMemBlackBoxingDefault
 * phase: spinal.core.internals.PhaseDeviceSpecifics
 * phase: spinal.core.internals.PhaseApplyIoDefault
 * phase: spinal.core.internals.PhaseNameNodesByReflection
 * phase: spinal.core.internals.PhaseCollectAndNameEnum
 * phase: spinal.core.internals.PhaseCheckIoBundle
 * phase: spinal.core.internals.PhaseCheckHiearchy
 * phase: spinal.core.internals.PhaseAnalog
 * phase: spinal.core.internals.PhaseNextifyReg
 * phase: spinal.core.internals.PhaseRemoveUselessStuff
 * phase: spinal.core.internals.PhaseRemoveIntermediateUnnameds
 * phase: spinal.core.internals.PhasePullClockDomains
 * phase: spinal.core.internals.PhaseInferEnumEncodings
 * phase: spinal.core.internals.PhaseInferWidth
 * phase: spinal.core.internals.PhaseNormalizeNodeInputs
 * phase: spinal.core.internals.PhaseRemoveIntermediateUnnameds
 * phase: spinal.core.internals.PhaseSimplifyNodes
 * phase: spinal.core.internals.PhaseCompletSwitchCases
 * phase: spinal.core.internals.PhaseRemoveUselessStuff
 * phase: spinal.core.internals.PhaseRemoveIntermediateUnnameds
 * phase: spinal.core.internals.PhaseCheck_noLatchNoOverride
 * phase: spinal.core.internals.PhaseCheck_noRegisterAsLatch
 * phase: spinal.core.internals.PhaseCheckCombinationalLoops
 * phase: spinal.core.internals.PhaseCheckCrossClock
 * phase: spinal.core.internals.PhasePropagateNames
 * phase: spinal.core.internals.PhaseAllocateNames
 * phase: spinal.core.internals.PhaseDevice
 * phase: spinal.core.internals.PhaseGetInfoRTL
 * phase: spinal.core.internals.PhaseDummy
 * phase: spinal.core.internals.PhaseVerilog



Things to explain and link examples, of feature that can be implemented:

 * rework
 * rename
 * plugin patterns
 * enumerate registers in a design to apply
 * initialize registers without any reset value to a random initialization value

