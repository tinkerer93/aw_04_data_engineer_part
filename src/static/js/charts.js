// set margins
let margin = ({top: 20, right: 20, bottom: 30, left: 40}),
    height = 400 - margin.top - margin.bottom,
    width = 400 - margin.left - margin.right;

// get data
let values = {{ data.value | safe }}
let entities = {{ data.entity | safe }}

// append svg
let svg = d3.select("#histogram")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

// add x axis
let x = d3.scaleLinear()
    .domain(d3.max(values, function(d) {}))
