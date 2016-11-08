$(function(){ 
	$("#listByPrice").click(function(){ 
		var typeid = $("#typeid").val();
		var match = $("#match").val();
		if(match == "asc"){
			window.location.href = "/listByPrice"+typeid+"_1/?sec=desc";
		}else if (match == "desc"){
			window.location.href = "/listByPrice"+typeid+"_1/?sec=asc";
		}
	});
}) 