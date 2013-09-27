##Unicode in Python regex.md

### Ordinary codepoints

Ordinary codepoints, 16 bits and up to four hex digits, are handled with the `\u` prefix:

~~~
import re
delete_me = '[^\u3300-\u9fff]'
re.sub(delete_me, '', the_string)
~~~

### High codepoints

But codepoints above four hex digits require 32 bits and the `\U` prefix, which in turn requires an explicit eight hex digits:

~~~
import re
delete_me = '[^\u3300-\u9fff\uf900-\ufaff\U00020000-\U0002fa1f]'
re.sub(delete_me, '', the_string)
~~~

[end]
