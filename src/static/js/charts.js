var margin = {top: 10, right: 30, bottom: 30, left: 50},
    width = 460 - margin.left - margin.right,
    height = 1000 - margin.top - margin.bottom;

// append svg
var svg = d3.select("#histogram")
    .append("svg")
        .attr("class", "axis")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

// get the data
d3.json("api/get_data", function(error, data) {

    // X axis
    var x = d3.scaleLinear()
      .domain([0, d3.max(data.value)]) // get the range of data on x axis (from 0 to max value)
      .range([0, width]);

    var ticks = d3.range(0, Math.ceil(x.domain()[1]) + 1, 5);

    // set the parameters for the histogram
    var histogram = d3.histogram()
      .domain(x.domain())  // the domain of the graphics
      .thresholds(ticks); // bin numbers (0, 5, 10 etc)

    // get the bins
    var bins = histogram(data.value);
    console.log(bins)

    // Y axis
    var y = d3.scaleLinear()
      .range([height, 0])
      .domain(d3.extent(bins, d => d.length));

    svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x)
            .tickValues(ticks));
    svg.append("g")
        .call(d3.axisLeft(y))

    // append the bar rectangles to the svg element
    svg.selectAll("rect")
      .data(bins)
      .enter()
      .append("rect")
        .attr("x", 1)
        .attr("transform", d => `translate(${x(d.x0)}, ${y(d.length)})`)
        .attr("width", d => x(d.x1) - x(d.x0) -1)
        .attr("height", d => height - y(d.length))
        .style("fill", "steelblue")
});
