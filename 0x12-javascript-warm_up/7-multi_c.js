#!/usr/bin/node
const x = Math.floor(process.argv[2]);
if (isNaN(x)) {
	console.log('Missing size');
} else {
	for (let i = 0; i < x; i++) {
		console.log('C is fun');
	}
}
