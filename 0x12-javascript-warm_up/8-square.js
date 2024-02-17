#!/usr/bin/node

let num = Number(process.argv[2]);

if (isNaN(num)) {
    console.log("Missing size");
} else {
    for (let i = 0; i < num; i++){
        for (let j = 0; j < num; j++){
            process.stdout.write("X");
        }
        process.stdout.write("\n")
    }
}