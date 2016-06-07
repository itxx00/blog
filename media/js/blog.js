$(function(){
    $("#pagination a").live("click", function(){
    	$(this).addClass("loading").text("loading...");
        var that = $(this);
        $.ajax({
			type: "GET",
			url: $(this).attr("href") + "#timeline",
			success: function(data){
            	that.parent().remove();
               	result = $(data).find("#timeline .post");
                nextHref = $(data).find("#pagination a").attr("href");
				$(function() {
					$("#timeline").append(result.fadeIn(300));
					$("img").lazyload({
						effect : "fadeIn"
					});
				});
				$("#pagination a").removeClass("loading").text("下一篇");
				$("#pagination a").attr("href", nextHref);
            }
        });
        return false;
    });
  
    $(".addComment").live("click",function(){
    	var that = $(this).addClass("loading").text("loading...");
    	var id = $(this).attr("id");
      	$("#commentDiv_"+id).load("/blog/content/"+id,null,function(){
        	that.remove();
        	$("#submitBtn_"+id).click(function(){
				var dataForm = $("#dataForm_"+id);
                                var loadBtn = $(this).addClass("loading").val("submiting...").attr("disabled","disabled");
				$.post(dataForm.attr("action"),dataForm.serializeArray(),function(re){
                                	var error = $("#error_"+id);
					if(re["state"] == "success"){
                                          if(!$("#ol_"+id +">li")[0]){
					  	$("#ol_"+id).empty();	
                                          }
                                          $("#ol_"+id).append("<li><p>"+re["time"]+",&nbsp;&nbsp;"+$("#nikename_"+id).val()+"&nbsp;:</p><p>"+$("#comment_"+id).val()+"</p></li>");
					  dataForm[0].reset();
                                          error.empty();
					}else{
						error.html(re["time"]);
					}
                                  loadBtn.removeClass("loading").val("Add").removeAttr("disabled");
				},"json");
         	 });
      	});
    });
 });