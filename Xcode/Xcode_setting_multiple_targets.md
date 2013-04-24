Xcode - setting multiple targets
==================================

Steps (for Xcode v. 3.2.5)

After creating a project:

 1.  Create a second "target" for the non-interactive test, so that no more than one program is identified as "_main" for any given target. This can be done (a) from the menu Project > New Target… or (b) by using either the right mouse button or option-click on the Targets item in the "Groups & Files" navigation palette at the left side of the Xcode window. There are many choices of template, but the best option is to duplicate the one that is created by default when the project is initialized and then change its name.

 1.  For each of the various `.cpp` files in the project, do Get Info > Targets; "Get Info" can also be done using command-i.

 1.  Check the appropriate check-boxes for the targets shown:

  1. for `main.cpp` (non-interactive test program) and the student's program file, check the box for the non-interactive test target name;

  1. for the interactive test program and the student's program file, check the box for the interactive text target name.

The student's program file has both check-boxes checked, while header files have nothing checked.

[end]
