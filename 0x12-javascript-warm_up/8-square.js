#!/usr/bin/node
const x = Math.floor(process.argv[2]);
if (isNaN(x)) {
	console.log('Missing size');
} else {
	for (let r = 0; r < size; r++) {
	let row = '';
	for (let c = 0; c < size; c++) row += 'X';
	console.log(row);
  }
}
