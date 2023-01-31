var ctx = document.getElementById("scrums_chart").getContext("2d");
var scrums_won = {{ match_statistics.scrums_won }};
var scrums_lost = {{ match_statistics.scrums_lost }};

var data = {
    labels: ["Scrums Won", "Scrums Lost"],
    datasets: [
        {
            data: [scrums_won, scrums_lost],
            backgroundColor: ["#006400", "#8B0000"],
            borderColor: ["#006400", "#8B0000"],
            borderWidth: 1
        }
    ]
};

var options = {
    title: {
        display: true,
        text: 'Scrums Won vs Scrums Lost'
    },
    tooltips: {
        callbacks: {
           label: function(tooltipItem, data) {
                  var label = data.labels[tooltipItem.index] || '';

                  if (label) {
                      label += ': ';
                  }
                  label += Math.round(tooltipItem.yLabel * 100) / 100;
                  return label;
           }
        }
    }
};

var chart = new Chart(ctx, {
    type: 'pie',
    data: data,
    options: options
});
