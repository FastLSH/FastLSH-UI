//Drag&Drop feature
$(function() {
    $( "#x-axis, #y-axis, #z-axis, #sortable1" ).sortable({
      connectWith: ".connectedSortable",
      revert: true,
      scroll: true,
      receive: function(event, ui) {
        var $this = $(this);
        if ($this.children('li').length > 1 && $this.attr('id')!="sortable1") {
            $(ui.sender).sortable('cancel');
        }
    }
}).disableSelection();

    $( "#sortable1" ).sortable({
      connectWith: ".connectedSortable",
      revert: true,
  }).disableSelection();

});



var dataPoints=[[0,0,0,0,0,0,0,0,0]]


$("#draw").click(function () {
    var view = $("#viewSelect").val();
    var is3D = true;
    var twoDfeature = 0;

    var xActive = $('#x-axis li').length;
    var yActive = $('#y-axis li').length;
    var zActive = $('#z-axis li').length;
    if (xActive) {
        var xFeature = $('#x-axis li:first-child').attr('id').charAt(1)-1;
    }
    if (yActive) {
        var yFeature = $('#y-axis li:first-child').attr('id').charAt(1)-1;
    }
    if (zActive) {
        var zFeature = $('#z-axis li:first-child').attr('id').charAt(1)-1;
    }
    
    if ((xActive+yActive+zActive)==3)
        is3D = true;
    else{
        is3D = false;
        twoDfeature = xActive*100+yActive*10+zActive;
    }

    var cout = $('#x-axis li').length;


    Highcharts.getOptions().colors = $.map(Highcharts.getOptions().colors, function (color) {
        return {
            radialGradient: {
                cx: 0.4,
                cy: 0.3,
                r: 0.5

            },
            stops: [
            [0, color],
            [1, Highcharts.Color(color).brighten(-0.2).get('rgb')]
            ]
        };
    });


    var dPoint = [];


    if ((!is3D)&&twoDfeature=="0") {
        alert("no feature selected");
    }

    for (var i=0; i<dataPoints.length; i++) {
        var ncolor = '#000';
        if (dataPoints[i][8] == 1)
            ncolor = '#000';
        else if (dataPoints[i][8] == 2)
            ncolor = '#595';
        else
            ncolor = '#CB3';

        
        if (is3D)
            dPoint[dPoint.length] = {x: dataPoints[i][xFeature], y: Number(dataPoints[i][yFeature]), z: dataPoints[i][zFeature], color: ncolor};
        else{
            if (twoDfeature=="110") {
                dPoint[dPoint.length] = {x: dataPoints[i][xFeature], y: Number(dataPoints[i][yFeature]), z: dataPoints[i][0], color: ncolor};
            }
            if (twoDfeature=="101") {
                dPoint[dPoint.length] = {x: dataPoints[i][xFeature], y: Number(dataPoints[i][zFeature]), z: dataPoints[i][0], color: ncolor};
            }
            if (twoDfeature=="11") {
                dPoint[dPoint.length] = {x: dataPoints[i][yFeature], y: Number(dataPoints[i][zFeature]), z: dataPoints[i][0], color: ncolor};
            }
            if (twoDfeature=="1") {
                dPoint[dPoint.length] = {x: dataPoints[i][zFeature], y: 0, z: dataPoints[i][0], color: ncolor};
            }
            if (twoDfeature=="10") {
                dPoint[dPoint.length] = {x: dataPoints[i][yFeature], y: 0, z: dataPoints[i][0], color: ncolor};
            }
            if (twoDfeature=="100") {
                dPoint[dPoint.length] = {x: dataPoints[i][xFeature], y: 0, z: dataPoints[i][0], color: ncolor};
            }


        }


    }


    var chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            margin: 100,
            type: 'scatter',
            options3d: {
                enabled: is3D,
                alpha: 10,
                beta: 30,
                depth: 250,
                viewDistance: 5,

                frame: {
                    bottom: { size: 1, color: 'rgba(0,0,0,0.02)' },
                    back: { size: 1, color: 'rgba(0,0,0,0.04)' },
                    side: { size: 1, color: 'rgba(0,0,0,0.06)' }
                }
            }
        },
        title: {
            text: 'Draggable box'
        },
        subtitle: {
            text: 'Click and drag the plot area to rotate in space'
        },
        plotOptions: {
            scatter: {
                width: 10,
                height: 10,
                depth: 10
            }
        },
        yAxis: {
            min: -10,
            max: 10,
            title: null
        },
        xAxis: {
            min: -10,
            max: 10,
            gridLineWidth: 1
        },
        zAxis: {
            min: -10,
            max: 10,
            showFirstLabel: false
        },
        legend: {
            enabled: false
        },
        series: [{
            name: 'Reading',
            data: dPoint
        }]
    });


$(chart.container).bind('mousedown.hc touchstart.hc', function (eStart) {
    eStart = chart.pointer.normalize(eStart);

    var posX = eStart.pageX,
    posY = eStart.pageY,
    alpha = chart.options.chart.options3d.alpha,
    beta = chart.options.chart.options3d.beta,
    newAlpha,
    newBeta,
            sensitivity = 5; // lower is more sensitive

            $(document).bind({
                'mousemove.hc touchdrag.hc': function (e) {
                // Run beta
                newBeta = beta + (posX - e.pageX) / sensitivity;
                chart.options.chart.options3d.beta = newBeta;

                // Run alpha
                newAlpha = alpha + (e.pageY - posY) / sensitivity;
                chart.options.chart.options3d.alpha = newAlpha;

                chart.redraw(false);
            },
            'mouseup touchend': function () {
                $(document).unbind('.hc');
            }
        });
        });

});

$("#filename").change(function(e) {
    var ext = $("input#filename").val().split(".").pop().toLowerCase();

    if($.inArray(ext, ["csv"]) == -1) {
        alert('Upload CSV');
        return false;
    }
    
    if (e.target.files != undefined) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var csvval=e.target.result.split("\n");
            var csvvalue=csvval[0].split(",");
            var inputrad="";
            for (var j =0 ;j<csvval.length;j++){
                inputrad=inputrad+"<tr>";
                csvvalue = csvval[j].split(",");
                var innerArray = [];
                for(var i=0;i<csvvalue.length;i++)
                {
                    var temp=parseInt(csvvalue[i]);
                    // $("#tx").text(typeof temp);
                    innerArray.push(csvvalue[i]);
                    // inputrad=inputrad+"<td>"+temp + "\n";
                    inputrad=inputrad+"<td>"+temp + "\n"+"</td>";
                }
                dataPoints.push(innerArray);
                inputrad=inputrad+"</tr>";
                $("#csvimporthint").html(inputrad);
                $("#csvimporthinttitle").show();
            };
        }
        reader.readAsText(e.target.files.item(0));

    }

    return false;

});

