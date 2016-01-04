## Vim NERDtree commands


 1. Move between tabs:

    `gt` = next tab

    `gT` = previous tab

 1. Move to directory root: `P`.
 
 1. Toggle open all subdirectories recursively: `O`.
 
 1. Get help: `?`

 1. 

### Keyboard mappings from `?` page within NERD Tree

```text
NERD tree (5.0.0) quickhelp~
============================
File node mappings~
double-click, <CR>, o: open in prev window
go: preview
t: open in new tab
T: open in new tab silently
middle-click, i: open split
gi: preview split
s: open vsplit
gs: preview vsplit

----------------------------
Directory node mappings~
double-click, o: open & close node
O: recursively open node
x: close parent of node
X: close all child nodes of
   current node recursively
middle-click, e: explore selected dir

----------------------------
Bookmark table mappings~
double-click, o: open bookmark
t: open in new tab
T: open in new tab silently
D: delete bookmark

----------------------------
Tree navigation mappings~
P: go to root
p: go to parent
K: go to first child
J: go to last child
<C-j>: go to next sibling
<C-k>: go to prev sibling

----------------------------
Filesystem mappings~
C: change tree root to the
   selected dir
u: move tree root up a dir
U: move tree root up a dir
   but leave old root open
r: refresh cursor dir
R: refresh current root
m: Show menu
cd:change the CWD to the
   selected dir
CD:change tree root to CWD

----------------------------
Tree filtering mappings~
I: hidden files (off)
f: file filters (on)
F: files (on)
B: bookmarks (off)

----------------------------
Custom mappings~

----------------------------
Other mappings~
q: Close the NERDTree window
A: Zoom (maximize-minimize)
   the NERDTree window
?: toggle help   

----------------------------
Bookmark commands~
:Bookmark [<name>]
:BookmarkToRoot <name>
:RevealBookmark <name>
:OpenBookmark <name>
:ClearBookmarks [<names>]
:ClearAllBookmarks
```

### Keyboard mappings from NERD Tree help page

But there is better information from `?` within NERD Tree (above).

```text
2.3. NERD tree Mappings
NERDTreeMappings
 
Default  Description~
help-tag
Key
 
o.......Open files, directories and bookmarks....................NERDTree-o
go......Open selected file, but leave cursor in the NERDTree.....NERDTree-go
t.......Open selected node/bookmark in a new tab.................NERDTree-t
T.......Same as 't' but keep the focus on the current tab........NERDTree-T
i.......Open selected file in a split window.....................NERDTree-i
gi......Same as i, but leave the cursor on the NERDTree..........NERDTree-gi
s.......Open selected file in a new vsplit.......................NERDTree-s
gs......Same as s, but leave the cursor on the NERDTree..........NERDTree-gs
O.......Recursively open the selected directory..................NERDTree-O
x.......Close the current nodes parent...........................NERDTree-x
X.......Recursively close all children of the current node.......NERDTree-X
e.......Edit the current dir.....................................NERDTree-e


<CR>...............same as NERDTree-o.
double-click.......same as the NERDTree-o map.
middle-click.......same as NERDTree-i for files, same as

NERDTree-e for dirs.


D.......Delete the current bookmark .............................NERDTree-D


P.......Jump to the root node....................................NERDTree-P
p.......Jump to current nodes parent.............................NERDTree-p
K.......Jump up inside directories at the current tree depth.....NERDTree-K
J.......Jump down inside directories at the current tree depth...NERDTree-J
<C-J>...Jump down to the next sibling of the current directory...NERDTree-C-J
<C-K>...Jump up to the previous sibling of the current directory.NERDTree-C-K


C.......Change the tree root to the selected dir.................NERDTree-C
u.......Move the tree root up one directory......................NERDTree-u
U.......Same as 'u' except the old root node is left open........NERDTree-U
r.......Recursively refresh the current directory................NERDTree-r
R.......Recursively refresh the current root.....................NERDTree-R
m.......Display the NERD tree menu...............................NERDTree-m
cd......Change the CWD to the dir of the selected node...........NERDTree-cd
CD......Change tree root to the CWD..............................NERDTree-CD


I.......Toggle whether hidden files displayed....................NERDTree-I
f.......Toggle whether the file filters are used.................NERDTree-f
F.......Toggle whether files are displayed.......................NERDTree-F
B.......Toggle whether the bookmark table is displayed...........NERDTree-B


q.......Close the NERDTree window................................NERDTree-q
A.......Zoom (maximize/minimize) the NERDTree window.............NERDTree-A
?.......Toggle the display of the quick help.....................NERDTree-?


------------------------------------------------------------------------------
```

[end]