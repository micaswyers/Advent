const fs = require('node:fs');

fs.readFile('test_input.txt', 'utf-8', (err, data) => {
  if (err) throw err;
  for ( const line of data ) {
    console.log(line.type);
  }
}
);