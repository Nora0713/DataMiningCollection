function productSearch() {
    var productName=$("#productName").val();
    var URL="/productSearch";
    $("#showResult").empty();
    var showPanel=document.getElementById("showResult");
    $.ajax(
        {
            type: "post",
            url: URL,
            timeout: 8000,
            dataType: "json",
            data: {
                "product": productName,
            },
            success: function (data) {
                $.each(data['hits']['hits'], function (infoIndex, info){
                    var outside=document.createElement("div");
                    outside.setAttribute("class","panel panel-default");
                    var inside=document.createElement("div");
                    inside.setAttribute("class","panel-collapse in");
                    inside.setAttribute("style","height: auto;");
                    var realTextDiv=document.createElement("div");
                    realTextDiv.setAttribute("class","panel-body");
                    realTextDiv.innerHTML="公司:"+info['_source']['company']+"</br>"+
                        "产品:"+info['_source']["product"]+"</br>"+
                        "类型:"+info['_source']['type1']+" "+info['_source']['type2']+
                        " "+info['_source']['type3']+" "+info['_source']['type4']+"</br>"+
                        'pdf:<a href="'+info['_source']['pdf_url']+'">'+info['_source']['pdf_url']+"</a></br>"+
                        'txt:<a href="'+info['_source']['txt_url']+'">'+info['_source']['txt_url']+"</a></br>"+
                        "filename:"+info['_source']['filename']
                    ;
                    inside.appendChild(realTextDiv);
                    outside.appendChild(inside);
                    showPanel.appendChild(outside);
                });
            },
            error: function(jqXHR, textStatus, errorThrown){
                alert('error ');
            }
        })
}

function companySearch() {
    var companyName=$("#companyName").val();
    var URL="/companySearch";
    $("#showResult").empty();
    var showPanel=document.getElementById("showResult");
    $.ajax(
        {
            type: "post",
            url: URL,
            timeout: 8000,
            dataType: "json",
            data: {
                "company": companyName,
            },
            success: function (data) {
                $.each(data['hits']['hits'], function (infoIndex, info){
                    var outside=document.createElement("div");
                    outside.setAttribute("class","panel panel-default");
                    var inside=document.createElement("div");
                    inside.setAttribute("class","panel-collapse in");
                    inside.setAttribute("style","height: auto;");
                    var realTextDiv=document.createElement("div");
                    realTextDiv.setAttribute("class","panel-body");
                    realTextDiv.innerHTML="公司:"+info['_source']['company']+"</br>"+
                        "产品:"+info['_source']["product"]+"</br>"+
                        "类型:"+info['_source']['type1']+" "+info['_source']['type2']+
                        " "+info['_source']['type3']+" "+info['_source']['type4']+"</br>"+
                        'pdf:<a href="'+info['_source']['pdf_url']+'">'+info['_source']['pdf_url']+"</a></br>"+
                        'txt:<a href="'+info['_source']['txt_url']+'">'+info['_source']['txt_url']+"</a></br>"+
                        "filename:"+info['_source']['filename']
                    ;
                    inside.appendChild(realTextDiv);
                    outside.appendChild(inside);
                    showPanel.appendChild(outside);
                });
            },
            error: function(jqXHR, textStatus, errorThrown){
                alert('error ');
            }
        })
}

function typeSearch() {
    var type3=$("#type3 option:selected").text();
    var URL="/typeSearch";
    $("#showResult").empty();
    var showPanel=document.getElementById("showResult");
    $.ajax(
        {
            type: "post",
            url: URL,
            timeout: 8000,
            dataType: "json",
            data: {
                "type3": type3,
            },
            success: function (data) {
                $.each(data['hits']['hits'], function (infoIndex, info){
                    var outside=document.createElement("div");
                    outside.setAttribute("class","panel panel-default");
                    var inside=document.createElement("div");
                    inside.setAttribute("class","panel-collapse in");
                    inside.setAttribute("style","height: auto;");
                    var realTextDiv=document.createElement("div");
                    realTextDiv.setAttribute("class","panel-body");
                    realTextDiv.innerHTML="公司:"+info['_source']['company']+"</br>"+
                        "产品:"+info['_source']["product"]+"</br>"+
                        "类型:"+info['_source']['type1']+" "+info['_source']['type2']+
                        " "+info['_source']['type3']+" "+info['_source']['type4']+"</br>"+
                        'pdf:<a href="'+info['_source']['pdf_url']+'">'+info['_source']['pdf_url']+"</a></br>"+
                        'txt:<a href="'+info['_source']['txt_url']+'">'+info['_source']['txt_url']+"</a></br>"+
                        "filename:"+info['_source']['filename']
                    ;
                    inside.appendChild(realTextDiv);
                    outside.appendChild(inside);
                    showPanel.appendChild(outside);
                });
            },
            error: function(jqXHR, textStatus, errorThrown){
                alert('error ');
            }
        })
}