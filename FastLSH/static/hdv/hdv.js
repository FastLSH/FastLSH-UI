//   Copyright 2017 Peter XU Yaohai
//
//    Licensed under the Apache License, Version 2.0 (the "License");
//    you may not use this file except in compliance with the License.
//    You may obtain a copy of the License at
//
//        http://www.apache.org/licenses/LICENSE-2.0
//
//    Unless required by applicable law or agreed to in writing, software
//    distributed under the License is distributed on an "AS IS" BASIS,
//    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//    See the License for the specific language governing permissions and
//    limitations under the License.



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

$("#feature_list").hide()

function gen_feature_list(f_num, f_names){
    $("#f1").html(f_names[0]);
    $("#f2").html(f_names[1]);
    $("#f3").html(f_names[2]);

    sortable_html = "";
    for ( i = 3; i<f_num; i++){
        sortable_html += "<li id=\"f"+(i+1)+"\" class=\"list-group-item\">" + f_names[i]+"</li>";
    }

    $("#sortable1").html(sortable_html);
    $("#feature_list").show();

}

var dataPoints=[[0,0,0,0,0,0,0,0,0]]

var chart;

//colors for each type of data point
color_sets = ["#000","#dc4","#bc7","#932","#904","#347","#509","#eac"]

$(".data-select").click(function () {
     $.ajax({
         url: '/FastLSH/get_data_series',
         data: {data_type: $(this).attr('id')},
         cache: false,
         success: function(response){
         dataPoints = response["data"];
         gen_feature_list(response["f_num"],response["f_names"])
         draw();
         },
       error: function(){
       }
      });
});


$("#feature_list").bind("DOMSubtreeModified",function(){
  draw();
});


$("#v_dis").knob({
  release: function(value) {
    chart.options.chart.options3d.viewDistance = value;
    chart.redraw(false);
  }
});

$("#depth").knob({
  release: function(value) {
    chart.options.chart.options3d.depth = value;
    chart.redraw(false);
  }
});

function draw() {
    var view = $("#viewSelect").val();
    var is3D = true;
    var twoDfeature = 0;

    var xActive = $('#x-axis li').length;
    var yActive = $('#y-axis li').length;
    var zActive = $('#z-axis li').length;

    if (xActive) {
        var xFeature = $('#x-axis li:first-child').attr('id').replace('f','')-1+2;
    }
    if (yActive) {
        var yFeature = $('#y-axis li:first-child').attr('id').replace('f','')-1+2;
    }
    if (zActive) {
        var zFeature = $('#z-axis li:first-child').attr('id').replace('f','')-1+2;
    }
    
    if ((xActive+yActive+zActive)==3)
        is3D = true;
    else{
        is3D = false;
        twoDfeature = xActive*100+yActive*10+zActive;
    }

    var cout = $('#x-axis li').length;

    var dPoint = [];


    if ((!is3D)&&twoDfeature=="0") {
        alert("no feature selected");
    }


    for (var i=0; i<dataPoints.length; i++) {
        var ncolor = color_sets[dataPoints[i][1]];

        if (is3D)
            dPoint[dPoint.length] = {x: dataPoints[i][xFeature], y: Number(dataPoints[i][yFeature]), z: dataPoints[i][zFeature], color: ncolor, name:dataPoints[i][0]};
        else{
            if (twoDfeature=="110") {
                dPoint[dPoint.length] = {x: dataPoints[i][xFeature], y: Number(dataPoints[i][yFeature]), z: dataPoints[i][0], color: ncolor, name:dataPoints[i][0]};
            }
            if (twoDfeature=="101") {
                dPoint[dPoint.length] = {x: dataPoints[i][xFeature], y: Number(dataPoints[i][zFeature]), z: dataPoints[i][0], color: ncolor, name:dataPoints[i][0]};
            }
            if (twoDfeature=="11") {
                dPoint[dPoint.length] = {x: dataPoints[i][yFeature], y: Number(dataPoints[i][zFeature]), z: dataPoints[i][0], color: ncolor, name:dataPoints[i][0]};
            }
            if (twoDfeature=="1") {
                dPoint[dPoint.length] = {x: dataPoints[i][zFeature], y: 0, z: dataPoints[i][0], color: ncolor, name:dataPoints[i][0]};
            }
            if (twoDfeature=="10") {
                dPoint[dPoint.length] = {x: dataPoints[i][yFeature], y: 0, z: dataPoints[i][0], color: ncolor, name:dataPoints[i][0]};
            }
            if (twoDfeature=="100") {
                dPoint[dPoint.length] = {x: dataPoints[i][xFeature], y: 0, z: dataPoints[i][0], color: ncolor, name:dataPoints[i][0]};
            }
        }
    }


    var x_max = -999999;
    var y_max = -999999;
    var z_max = -999999;
    var x_min = 999999;
    var y_min = 999999;
    var z_min = 999999;

    for (var i=0; i<dPoint.length; i++){
        if (dPoint[i]['x']>=x_max){
            x_max = dPoint[i]['x'];
        }

        if (dPoint[i]['x']<=x_min){
            x_min = dPoint[i]['x'];
        }

        if (dPoint[i]['y']>=y_max){
            y_max = dPoint[i]['y'];
        }

        if (dPoint[i]['y']<=y_min){
            y_min = dPoint[i]['y'];
        }

        if (dPoint[i]['z']>=z_max){
            z_max = dPoint[i]['z'];
        }

        if (dPoint[i]['z']<=z_min){
            z_min = dPoint[i]['z'];
        }
    }

    x_axis_max = parseFloat(x_max) + (x_max-x_min)*0.1;
    x_axis_min = x_min - (x_max-x_min)*0.1;
    y_axis_max = parseFloat(y_max) + (y_max-y_min)*0.1;
    y_axis_min = y_min - (y_max-y_min)*0.1;
    z_axis_max = parseFloat(z_max) + (z_max-z_min)*0.1;
    z_axis_min = z_min - (z_max-z_min)*0.1;

    chart_options =
        {
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

        tooltip: {

        borderRadius: 10,
        formatter: function() {
        var p = this.point;
        return '<strong>'+p.name + '</strong><br>' +
               'x: <strong>'+p.x + '</strong><br> ' +'y: <strong>' +p.y + '</strong><br> '
               + 'z: <strong>'+p.z +'</strong>';
         }

        },

        title: {
            text: 'HDDV'
        },
        subtitle: {
            text: 'High Dimensional Data Visualizer'
        },
        plotOptions: {
            scatter: {
                width: 10,
                height: 10,
                depth: 10,
                turboThreshold: 3000
            },

        },


        yAxis: {
            min: y_axis_min,
            max: y_axis_max,
            title: null
        },
        xAxis: {
            min: x_axis_min,
            max: x_axis_max,
            gridLineWidth: 1
        },
        zAxis: {
            min: z_axis_min,
            max: z_axis_max,
            showFirstLabel: false
        },
        legend: {
            enabled: false
        },
        series: [{
            cropThreshold: 20000,
            turboThreshold: 20000,
            data: dPoint
        }]
    }

    chart = new Highcharts.Chart(chart_options);


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

};




