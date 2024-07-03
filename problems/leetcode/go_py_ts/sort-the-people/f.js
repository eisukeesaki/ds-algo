/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
function sortPeople(names, heights) {
  let pairs = new Map();
  let sorted = [];

  for (let i = 0; i < heights.length; i++) {
    pairs.set(heights[i], names[i])
  }

  heights.sort((a, b) => b - a);
  console.log(pairs.get(180));
  // for (height of heights) {
  //   map.get(height);
  // }
}


function main() {
  const names = ["Mary", "John", "Emma"];
  const heights = [180, 165, 170];
  // const sorted_names = sortPeople(names, heights);
  sortPeople(names, heights);
}

main();
