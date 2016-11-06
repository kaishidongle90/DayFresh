$(function(){ 

	$('#all').click(function(){
		if($(this).prop('checked')){
			$(':checkbox:not(#all)').prop('checked',true).next().attr('name','count')
		}else{
			$(':checkbox:not(#all)').prop('checked',false).next().attr('name','')
		}
	});

	$(':checkbox:not(#all)').click(function(){
		if($(this).prop('checked')){
			$(this).next().attr('name','count')
		}else{
			$(this).next().attr('name','')
		}
	});


	$(".add").click(function(){ 
		var s=0;
		var sum=0;
		var p=$(this).parent().parent().parent();
		var t=$(this).parent().find('input[class*="num_show"]');
		var id=p.find('li[class*="col01"]').find('input');
		
		t.val(parseInt(t.val())+1);		
		s+=parseInt(t.val())*parseFloat(p.find('li[class*="col05"]').html()); 
		p.find('li[class*="col07"]').find('em').html(s.toFixed(2));		
		$.post("/set_num/",{id:(id.val()),num:(t.val())});

		
	});

	$(".minus").click(function(){ 
		var s=0;
		var p=$(this).parent().parent().parent();
		var t=$(this).parent().find('input[class*="num_show"]'); 
		var id=p.find('li[class*="col01"]').find('input');
		
		t.val(parseInt(t.val())-1); 
		if(parseInt(t.val())<1){ 
			t.val(1); 
		}
		s+=parseInt(t.val())*parseFloat(p.find('li[class*="col05"]').html()); 
		p.find('li[class*="col07"]').find('em').html(s.toFixed(2));
		$.post("/set_num/",{id:(id.val()),num:(t.val())});

		});

}) 


