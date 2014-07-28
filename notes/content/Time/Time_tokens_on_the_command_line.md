 on the command line
===============================

Basics
------
Use `date`:

        $(date '+%Y%m%d-%H%M%S')
to produce

        20110211-225505
(etc.) 

Formatted "interpreted sequences"
---------------------------------
1. Large summary sequences
 1. Date
  * `%c` : locale's date and time (e.g., Thu Mar  3 23:05:25 2005)
  * `%D` : date; same as `%m/%d/%y`
  * `%F` : full date; same as `%Y-%m-%d`
  * `%T` : time; same as `%H:%M:%S`
  * `%x` : locale's date representation (e.g., 12/31/99)
 1. Time
  * `%X` : locale's time representation (e.g., 23:13:48)
  * `%p` : locale's equivalent of either AM or PM; blank if not known
  * `%P` : like `%p`, but lower case
  * `%r` : locale's 12-hour clock time (e.g., 11:11:04 PM)
  * `%R` : 24-hour hour and minute; same as `%H:%M`
 1. Time zone
  * `%z` : `+hhmm` numeric timezone (e.g., -0400)
  * `%:z` : `+hh:mm` numeric timezone (e.g., -04:00)
  * `%::z` : `+hh:mm:ss` numeric time zone (e.g., -04:00:00)
  * `%:::z` : numeric time zone with : to necessary precision (e.g., -04, +05:30)
  * `%Z` : alphabetic time zone abbreviation (e.g., EDT)

1. Units
 1. Century
  * `%C` : century; like `%Y`, except omit last two digits (e.g., 20)
 1. Year
  * `%g` : last two digits of year of ISO week number (see %G)
  * `%G` : year of ISO week number (see `%V`); normally useful only with `%V`
  * `%y` : last two digits of year (00..99)
  * `%Y` : year
 1. Month
  * `%m` : month (01..12)
  * `%b` : locale's abbreviated month name (e.g., Jan)
  * `%B` : locale's full month name (e.g., January)
  * `%h` : same as `%b`
 1. Week
  * `%U` : week number of year, with Sunday as first day of week (00..53)
  * `%V` : ISO week number, with Monday as first day of week (01..53)
  * `%W` : week number of year, with Monday as first day of week (00..53)
 1. Day
  * `%a` : locale's abbreviated weekday name (e.g., Sun)
  * `%A` : locale's full weekday name (e.g., Sunday)
  * `%d` : day of month (e.g, 01)
  * `%e` : day of month, space padded; same as `%_d`
  * `%j` : day of year (001..366)
  * `%u` : day of week (1..7); 1 is Monday
  * `%w` : day of week (0..6); 0 is Sunday
 1. Hour
  * `%H` : hour (00..23)
  * `%I` : hour (01..12)
  * `%k` : hour ( 0..23)
  * `%l` : hour ( 1..12)
 1. Minute
  * `%M` : minute (00..59)
 1. Second
  * `%S` : second (00..60)
  * `%s` : seconds since 1970-01-01 00:00:00 UTC
  * `%N` : nanoseconds (000000000..999999999)

1. Formatting
 1. Line formatting
  * `%n` : a newline
  * `%%` : a literal `%`
  * `%t` : a tab
 1. Padding
By default, date pads numeric fields with zeroes.  The following optional flags may follow `%':
  * `-` :  (hyphen) do not pad the field
  * `_` :  (underscore) pad with spaces
  * `0` :  (zero) pad with zeros
  * `^` :  use upper case if possible
  * `#` :  use opposite case if possible

[end]
