function checkAge(age) {
    if (age > 18) {
        return true;
    } else {
        // ...
        return confirm('Did parents allow you?');
    }
}
function checkAge(age) {
    if (age > 18) {
        return true;
    }
    // ...
    return confirm('Did parents allow you?');
}
//No difference!

function checkAge(age) {
    return (age > 18) ? true : confirm('Did parents allow you?');
}
function checkAge(age) {
    return (age > 18) || confirm('Did parents allow you?');
}

function min(a, b) {
    return a < b ? a : b;
}