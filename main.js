// $("#btn").on("click",getFolder);
function init(){
    var btn=document.getElementById("btn");
    btn.onclick=getFolder;  
}
function getFolder(){
    console.log("clicked");
    const fs = require('fs');
    const path = require('path');

    // 文件夹路径
    const folderPath = '/path/to/folder';

    // 遍历目录下的文件
    fs.readdir(folderPath, (err, files) => {
        if (err) throw err;

        // 循环遍历文件
        files.forEach((file) => {
            // 获取文件完整路径
            const filePath = path.join(folderPath, file);

            // 判断文件类型是否为pdf或doc/docx
            if (/\.(pdf|doc|docx)$/i.test(filePath)) {
            // 执行相应的操作，比如复制或移动文件
            console.log('找到匹配的文件：', filePath);
            }
        });
    });
}
init();
