$(function(){ 
	setTotal();
	$(".add").click(function(){ 
		var t=$(this).parent().find('input[class*="num_show"]');
		t.val(parseInt(t.val())+1) 	
		setTotal(); 
	}); 

	$(".minus").click(function(){ 
		var t=$(this).parent().find('input[class*="num_show"]'); 
		t.val(parseInt(t.val())-1) 
		if(parseInt(t.val()-1)<1){ 
			t.val(1); 
		}
		setTotal();
	}); 

	function setTotal(){ 
		var s=0; 
		s=(parseInt($(".num_show").val())*parseFloat($(".show_pirze > em").html())).toFixed(2); 
		$(".total").children(":first").html(s);
	}

	$("#goods_intro").click(function(){ 
		$("#goods_eval").removeClass("active");
		$("#goods_intro").addClass("active");
		$('#intro_content').show();
		$('#eval_content').hide();
	});

	$("#goods_eval").click(function(){ 
		$("#goods_eval").addClass("active");
		$("#goods_intro").removeClass("active");
		$('#intro_content').hide();
		$('#eval_content').show();
	});

	$("#buy_now").click(function(){ 
		var num = $("#order_num").val();
		var id = $("#gd_id").html();
		window.location.href="/place_order/?gnum="+num+"&gid="+id;
	});

	$("#add_cart").click(function(){ 
		var num = $("#order_num").val();
		var id = $("#gd_id").html();
		window.location.href="/add_cart/?gid="+id+"&gnum="+num;
	});
}) 