
// $("#btn").on("click",selectFolder);

// function selectFolder(){

//     const input = document.createElement('input');
//     input.type = 'file';
//     input.webkitdirectory = true; // 添加webkitdirectory属性，弹出文件夹选择器
//     input.onchange = function(event) {

//         const folderPath = event.target.files[0].path; // 获取选中的文件夹路径
//         console.log(folderPath); // 在控制台中输出文件夹路径，您可以将其发送到服务器进行处理
//         $("#path").text(folderPath);
//     };
//     input.click(); // 模拟点击input元素，弹出文件夹选择器
// }
const form = document.querySelector('form');
form.addEventListener('submit', async (event) => {
	event.preventDefault();
	const data = {
		folder_path : document.getElementById('folder_path').files[0].path
	};
	const response = await fetch('/folder', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	const result = await response.json();
	if (response.ok) {
		alert('成功选择文件夹：' + result.folder_path);
	} else {
		alert('错误：' + result.message);
	}
});
