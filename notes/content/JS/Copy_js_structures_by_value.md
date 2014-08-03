## Copy JS structures by value

### Array

    new_array = old_array.slice(0);

### Object

    new_object = JSON.parse(JSON.stringify(old_object));

[end]