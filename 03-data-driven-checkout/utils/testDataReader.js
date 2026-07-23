const fs = require('fs');
const path = require('path');

/**
 * Loads a JSON data file from /data as an array of test case objects.
 * @param {string} fileName e.g. 'checkoutData.json'
 * @returns {Array<object>}
 */
function loadData(fileName) {
  const filePath = path.join(__dirname, '..', 'data', fileName);
  const raw = fs.readFileSync(filePath, 'utf-8');
  return JSON.parse(raw);
}

module.exports = { loadData };
