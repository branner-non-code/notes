## Wenlin options

### General options

Configuration of Wenlin v. 4 is done using the `Options` menu. I normally use:

 * OFF `Simple Form Characters`
 * ON  `Quiet`
 * OFF `Reveal Codes in This Window`

### Viewing all available characters

Go to `Option => Hanzi Filter... => All 75,000+ Hanzi`

This makes the full Unicode CJK character set visible. Actually, there are still some characters that will require extra work to make appear in the "Look Up Word" pop-up window, because traditional and simplified forms are not normally visible simultaneously in that window. For instance, there is an ancient graph 幵 (_qiān_, _yán_) that has long been written as 开 (GY: "說文曰、平也、兩干對舉、又羌名、今作开同"). But because 开 is considered to be the simplified form of 開, it is not shown when you search for words pronounced _qiān_.

However, Wenlin's support for look-up of rare characters is generally very good.

### Text markup

Although Wenlin does not support most of the fancy text formatting characteristic of mainstream word processors, it reads a subset of XML tags and these can be used for certain basic formatting features, such as underlining and 

Go to `Option => Reveal Codes` in This Window

This enables you to see, edit, and add XML tags to effect some basic formatting:

 * `<u>X</u>` will underline X
 * `<center>XYZ</center>` will center XYZ
 * `<font color="red">X</font>` will color X red. The recognized color names are:
  * `aqua`
  * `black`
  * `blue`
  * `fuchsia`
  * `green`
  * `lime`
  * `maroon`
  * `navy`
  * `olive`
  * `purple`
  * `red`
  * `silver`
  * `teal`
  * `white`
  * `yellow`

 For finer gradations you can also use the standard six-digit hexadecimal RGB numbers (`<font color="ff0000">` for red, etc.).
 
 The formatting won't be visible until you set `Option => Reveal Code` to OFF again; at that point, you must be careful not to inadvertently delete part of the tag, otherwise it will "break" and the remainder of it will become visible, whlie the formatting will no longer work.

Images, links, and other common things can be produced using `<img>`, `<a>`, and so forth. See http://guide.wenlininstitute.org/wenlin4.1/Editing_Documents; the same content is installed within your Wenlin 4 installation — look for a subpath `/WenlinTushuguan/Help/html/editing_documents.html` on your hard drive.

[end]
