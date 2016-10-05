## Make basic syntax

Notes from Chapter 7 of Andy Oram and Mike Loukides, _Programming with GNU software_ (O'Reilly, 1997).

 * comments: lines beginning with `#`
 * targets: 
   
   * begin at left margin, followed by `:`
   * name of a file to create or task to be executed; file is always sought first
   * any dependencies of target follow the `:` (space-delimited)
   * targets may be defined recursively 
   * `make task`: executes task
   * `make program.o`: compiles `program.c` and generates object-file
   * `make`: alone, creates the first target described in the makefile

 * shell command lines: 

   * line begins with \t (not space)
   * must be a single line, continued with `\` or concatenated with `;`

 * not "up-to-date":
 
   * older than its dependencies and so must be recompiled
   * or else non-existent

 * abbreviations:
 
   * `$@`: full name of target, including suffix
   * `$*`: name of target, stripped of suffix
   * `$(MACRO)`: variable, bearing flags, source- and object-files, etc.
   * `$<`: the source file used to build the target

 * common variables
 
   * `VPATH`: series of comma-delimited directories to be searched
   * `CFLAGS`: series of space-delimited options to a command

 * suffix rules
 
   * `<suffixes>;: <command line>`: when particular suffixes are supplied, execute `<command line>`

 * pattern rules: use `%` as wildcards in filenames, which as target-files may be space-delimited

### Common targets

 * deleting object modules
 
   * `make clean`: deletes all object modules
   * `clean` as target: specifies command line to be executed

 * `.SUFFIXES`:
 
   * alone, clear the suffix list
   * followed by space-delimited suffixes, declares that those suffixes are used in default rules in this file

### Common flags

 * `-f`: specifies a particular makefile
 * `-n`: dry-run
 * `-i`: terminate on any error (non-zero error-code)
 * `-k`: continue other compilations on error in any one compilation
 * `-q`: determine whether target is up-to-date
 * `-s`: silent mode
 * `-j`: run multiple commands in parallel
 * `-t`: make up-to-date any files that are not so (using `touch`)
 * `-d`: verbose mode (debug)

[end]