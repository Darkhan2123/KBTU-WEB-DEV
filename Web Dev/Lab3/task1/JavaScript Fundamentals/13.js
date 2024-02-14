let i = 3;

while (i) {
    alert( i-- );
}
// 1

let i = 0;
while (++i < 5) alert( i );
//From 1 to 4

let i = 0;
while (i++ < 5) alert( i );
//From 1 to 5

for (let i = 0; i < 5; i++) alert( i );
// from 0 to 4

for (let i = 0; i < 5; ++i) alert( i );
//from 0 to 4