$("#files").hide();
$("#results").hide();
$("#download").hide();
var userAns=[];
var key;

$("#openFileDialog").on("click",openFileDialog);
function openFileDialog() {
    // $.ajax({
	// 	type:'POST',
	// 	url: '/get_folder_path/',  // 后端接口的URL
	// 	// method: 'GET',
	// 	success: function(data) {
	// 		// var path=JSON.parse(data)
    //         console.log(data.folder_path);  // 处理从服务器返回的数据
	// 		$("#path").val(data.folder_path);
	// 	}s
	//   });
	if($("#keyfile").length>0){
		$("#keyfile").remove();
	}
	if($("#views").length>0){
		$("#views").remove();
	}
	$("#files").hide();
	$("#results").hide();
	$("#download").hide();

	fetch('/get_folder_path/', {
		method: 'POST',
		headers: {
			'X-CSRFToken': '{{ csrf_token }}',
			'Content-Type': 'application/json'
		  }
	  })
		.then(response => response.json())
		.then(data => {
			console.log(data.folder_path);  // 处理从服务器返回的数据
			console.log(data.files);

			// if($("#views").length>0){
			// 	$("#views").remove();
			// }
		  	$("#path").val(data.folder_path);
			if ($("#path").val()==""){
				$("#files").hide();
			}
			var str="<ul id='views'>";
			var files=data.files.split("*");
			// console.log(files);
			for(var i=0;i<files.length;i++){
				if(files[i]!=""){
					str+="<li><p>"+files[i]+"</p></li>";
					// console.log(str);
				}
			}
			str+="</ul>";
			$("#files").append(str);
			$("#files").show();
		})
		.catch(error => {
		  console.error('Error:', error);
		});
  }

$("#seek").on("click",seekKeyword);
function seekKeyword(){

	var keyword=$("#keyword").val();
	var path=$("#path").val();

	if(path==""){
		alert("请先选择文件夹！");
	}
	else if(keyword==""){
		alert("请先输入关键词！");
	}
	else{
		key=keyword;
		// fetch('/seek_keyword/', {
		// 	method: 'POST',
		// 	headers: {
		// 	  'X-CSRFToken': '{{ csrf_token }}',
		// 	  'Content-Type': 'application/json'
		// 	},
		// 	body: JSON.stringify({ 'keyword': keyword,'folder_path':path })
		//   })
		// 	.then(response => response.json())
		// 	.then(data => {
		// 		console.log(data.code); 
		// 		// 		result();
		// 	})
		// 	.catch(error => console.error(error));
		$.ajax({
			type:'POST',
			url: '/seek_keyword/', 
			//将路径和关键词传给后端
			dataType: 'json',
			data:{
				'keyword':keyword,
				'folder_path':path
			},
			success: function(data) {
				
				// console.log(data.res);
				if($("#keyfile").length>0){
					$("#keyfile").remove();
				}
				if(data.res != ""){
					var file
				var rows
				var str="<ul id='keyfile'>"
				file=data.res.split("*");
				//注意，这里下标是从1开始的
				for(var i=1;i<file.length;i++){
					rows=file[i].split("@");
					for(var j=0;j<rows.length;j++){
						console.log(rows[j]);
						if(j==0){
							str+="<li><input type='checkbox'  value='"+i+"' "+"id='"+i+"' name='option'>"+rows[j]+"<hr>"
						}else{
							var temp=rows[j].split(keyword);
							str+=temp[0];
							for(var k=1;k<temp.length;k++){
								str+="<span id='keyword1'>"+keyword+"</span>"+temp[k];
							}
							str+="<br><br>"
						}
					}
					str+="</li>"
				}
				str+="</ul>"
				$("#results").append(str);
				$("#results").show();
				$("#download").show();
				userAns=[];
				// $("#download").bind("click",submit);
				$("#keyfile input").bind("click",onBoxClick);
				}else{
					alert("没有数据！");
					$("#results").hide();
					$("#download").hide();
				}
			}
		});
	}
}
function onBoxClick(){     //保存用户的选择
    var i=$.inArray($(this).val(),userAns);
        if(i==-1){   //若不在数组里，就添加
            userAns.push($(this).val());
        }
        else{
            userAns.splice(i,1);    //若在数组里，则是取消选择后删除
        }
    console.log(userAns);
}

//下载选中文件
$("#download").bind("click",downLoad);
function downLoad(){
	//获取选择的文本内容
	var text=""
	for(var i=1;i<$("#keyfile li").length+1;i++){
		if($.inArray($("input[id='" + i + "']").val(),userAns)>=0){
			text+=$("input[id='" + i + "']").parent().text()+"\n";
		}
	}

	console.log(text);
	if(text!=""){
		$.ajax({
			type:'POST',
			url: '/download/', 
			//将保存的文本传给后端
			dataType: 'json',
			data:{
				'text':text,
				'key':key
			},
			success: function(data) {
				if(data.code=='1'){
					alert("保存成功！");
				}
			}
		});
	}else{
		alert("请选择需要下载的部分");
	}
}