## Things to remember about Bash scripting

 * no spaces on either side of `=`
 * no final `/` in regex replace:
 
   ```python
   for i in a_*_c ; do mv "$i" "${i/b/d}" ; done
   ```

[end]