// const form = document.querySelector('form');

// form.addEventListener('submit', async (event) => {
// 	event.preventDefault();
// 	const data = {
// 		folder_path : document.getElementById('folder_path').files[0].path
// 	};
// 	const response = await fetch('/folder', {
// 		method: 'POST',
// 		headers: {
// 			'Content-Type': 'application/json'
// 		},
// 		body: JSON.stringify(data)
// 	});
// 	const result = await response.json();
// 	if (response.ok) {
// 		alert('成功选择文件夹：' + result.folder_path);
// 	} else {
// 		alert('错误：' + result.message);
// 	}
// });
$("#openFileDialog").on("click",openFileDialog);
function openFileDialog() {
    $.ajax({
		type:'POST',
		url: '/get_folder_path/',  // 后端接口的URL
		// method: 'GET',
		success: function(data) {
			// var path=JSON.parse(data)
            console.log(data.folder_path);  // 处理从服务器返回的数据
			$("#path").val(data.folder_path);
		}
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
		$.ajax({
			// type:'POST',
			url: '/seek_keyword/', 
			method:'POST',
			//将路径和关键词传给后端
			dataType: 'json',
			data:{
				'keyword':keyword,
				'folder_path':path
			},
			success: function(data) {
				console.log(data.code); 
			}
		  });
	}
}
