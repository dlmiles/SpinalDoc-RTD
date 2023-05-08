Lifecycle
=========

This page attempts to document details about the internals workings of
the codegen lifecycle that exist inside SpinalHDL.


SpinalHDL Codegen (internal) Lifecycle
--------------------------------------

This section seeks to document the internal lifecycle concerning how
SpinalHDL takes Scala code and emits HDL language artifacts.

Internally there is a sequence of phases that occur.
Some of these phases maybe hooked into and utilized for various purposes by
applicaition code to assist the task of code generation.


List of Phases:

 * Phase One
 * Phase Two
 * Phase Three


Things to explain and link examples, of feature that can be implemented:

 * rework
 * rename
 * plugin patterns

