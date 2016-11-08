$(function(){ 

	$('#all').click(function(){
		if($(this).prop('checked')){
			$(':checkbox:not(#all)').prop('checked',true).next().attr('name','count')
		}else{
			$(':checkbox:not(#all)').prop('checked',false).next().attr('name','')
		}
		total();
	});

	$(':checkbox:not(#all)').click(function(){
		if($(this).prop('checked')){
			$(this).next().attr('name','count')
		}else{
			$(this).next().attr('name','')
		}
		total();
	});

	// 加法
	$(".add").click(function(){
		var t=$(this).parent().find(".num_show");
		t.val(parseInt(t.val())+1);

		setTotal(t);
		setNum(t);
		total();
	});

	// 减法
	$(".minus").click(function(){
		var t=$(this).parent().find(".num_show");
		t.val(parseInt(t.val())-1);

		if(parseInt(t.val())<1){ 
			t.val(1); 
		}

		setTotal(t);
		setNum(t);
		total();
	});

	// 计算小计
	function setTotal(t){
		var sum=0;
		var p=t.parent(".num_add").parent(".col06").siblings(".col05");
		var s=t.parent(".num_add").parent(".col06").siblings(".col07").find("em");
		sum+=parseInt(t.val())*parseFloat(p.html());
		s.html(sum.toFixed(2));
		return(sum.toFixed(2));

	}

	// 将数量存到数据库
	function setNum(t){
		var p=t.parent().parent().parent();
		var id=p.find(".col01").find('input');
		$.post("/set_num/",{id:(id.val()),num:(t.val())});
	}

	// 刷新页面计算小计
	$(".cart_list_td").each(function(){
		var t=$(this).find(".col06").find(".num_add").find(".num_show");
		setTotal(t);
	});

	// 计算总计
	function total(){
		var tal=0;
		var num=0;
		$('.cart_list_td input[type="checkbox"]:checked').each(function(){
			if($(this).prop("checked")){
				var t=$(this).parent('.col01').siblings(".col07").find("em").html()
				var n=$(this).parent('.col01').siblings(".col06").find(".num_add").find(".num_show").val();
			}
			tal+=parseFloat(t);
			num+=parseInt(n);
			
		});
		$(".settlements>.col03>em").html(tal.toFixed(2));
		$(".settlements>.col03>b").html(num);
		$(".total_count>em").html(num);
	}

	total();
	

}) 


