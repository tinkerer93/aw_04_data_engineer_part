// set margins
let margin = ({top: 20, right: 20, bottom: 30, left: 40}),
    height = 400 - margin.top - margin.bottom,
    width = 400 - margin.left - margin.right;


// append svg
let svg = d3.select("#histogram")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

// get data
d3.json("/api/get_data", function(error, json) {
    if (error) throw error;
    data = json;

    // add x axis
    let x = d3.scaleLinear()
        .domain([0, d3.max(function(d) {return d;})])
        .range([0, width]);
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    let histogram = d3.histogram()
        .value(function(d) {return d;})
        .domain(x.domain())
        .thresholds(x.ticks(5));

    let bins = histogram(data.value);

    // add y axis
    let y = d3.scaleLinear()
        .range([height, 0]);
    y.domain([0, d3.max(bins, function(d) { return d.length; })]);
    svg.append("g")
        .call(d3.axisLeft(y));

    // append bars to svg element
    svg.selectAll("rect")
        .data(bins)
        .enter()
        .append("rect")
            .attr("x", 1)
            .attr("transform", function(d) { return `translate(${x(d.x0)},${y(d.length)})`;})
            .attr("width", function(d) { return x(d.x1) - x(d.x0) - 1;})
            .attr("height", function(d) {return height - y(d.length);})
            .style("fill", "#20639b")

});


