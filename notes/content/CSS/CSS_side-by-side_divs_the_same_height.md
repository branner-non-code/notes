## CSS Side-by-side divs the same height

### Mimic older table-row behavior

```
.container {
  display: table;
}
 
.rowlike {
  display: table-row;
}
 
.celllike {
  display: table-cell;
}
```

### For vertical centering of all elements

```
.rowlike:before {   
  content: '';      
  display: inline-block;
  height: 100%;     
  vertical-align: middle;
}                                                                               
```

[end]