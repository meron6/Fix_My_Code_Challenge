#!/usr/bin/node
/**
 * Prints a square of a given size using hash characters (#).
 * Usage: ./1-print_square.js <size>
 * Example: ./1-print_square.js 4
 */

const size = parseInt(process.argv[2]);

if (isNaN(size) || size <= 0) {
  console.log('Usage: ./1-print_square.js <size>');
  console.log('Example: ./1-print_square.js 4');
  process.exit(1);
}

for (let i = 0; i < size; i++) {
  console.log('#'.repeat(size));
}
