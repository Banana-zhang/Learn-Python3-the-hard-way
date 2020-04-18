### Windows
* pwd：打印工作目录。

* hostname：计算机在网络中的名称。

* mkdir：创建目录。

* cd：更改目录。
  切换盘符只需要 d: 
  回到根目录 cd\

  返回上一级 cd ..
  善用 Tab键 自补全

* ls：列出目录中的内容。

* rmdir：删除目录。
  删除有文件的目录 rmdir -r

* pushd：推送目录。
  将目录推送到一个列表，方便直接访问
  pushd 后加要去的新目录，会把  **当前目录**  保存

* popd：弹出目录。
  回到pushd保存的目录

* cp：复制文件或目录。
  为防止覆盖掉同名文件可以在路径末尾加上\或/
  复制目录 cp -r

* robocopy：更可靠的复制命令。
  例：robocopy d:\work e:\back *.txt *.doc *.bmp *.tif /s

  将d:\work文件下的TXT、DOC、BMP、TIF复制到e:\back文件夹，其他文件则不复制。/s是表示包括
  除空文件下的所有子目录，如果没有则仅复制d:\work下的文件而不包括子目录。

* mv：移动文件或目录。
  相当于重命名

* more：逐页查看文件。

* type：打印整个文件。

* forfiles：在一大堆文件上面运行一条命令。

* dir -r：寻找文件。

* select-string：在文件中查找内容。

* help：阅读手册。
  get -help 命令     可以查看命令的解释说明

* helpctr：寻找恰当的手册页面。

* echo：打印一些参数。

* set：导出/设定一个新的环境变量。

* exit：退出shell。

* runas：成为超级用户root，危险命令！