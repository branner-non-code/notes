### Supply default text in form but clear it when user begins typing

Works, 20130610:

    function clearField(){
      if (this.defaultValue === this.value) {
        this.value = '';
      }
    }
    var searchBox = document.createElement('textArea');
    searchBox.defaultValue='Enter text here.';
    searchBox.onkeydown=clearField; // better than onfocus(), since we want focus here by default
    searchBox.focus();

[end]
