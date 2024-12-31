# simple-o1-agent

## How to use

1. Install the dependencies

```shell
pip install -r requirements.txt
```

2. Run the program

```shell
streamlit run chatbot.py
```

## todo

1. [ ] codebase_search：
    在代码库中搜索相关的代码片段
    可以根据语义查找代码
    适合查找特定功能或实现的代码
2. [ ] grep_search：
    在文件或目录中快速搜索特定文本模式
    支持精确匹配和正则表达式
    可以限定搜索范围和文件类型
3. [ ] list_dir：
    列出目录的内容
    显示文件和子目录的详细信息
    可以查看文件大小和目录结构
4. [ ] view_file：
    查看文件内容
    可以指定查看的行数范围
    适合预览和检查文件内容
5. [ ] view_code_item：
    查看特定代码项（如类、函数）的详细内容
    需要提供完整的代码项路径
    适合深入查看代码实现
6. [ ] write_to_file：
    创建新文件
    可以写入文件内容
    支持创建空文件或带内容的文件
7. [ ] edit_file：
    编辑现有文件
    可以修改文件的特定行
    支持部分内容替换
8. [ ] related_files：
    查找与指定文件相关的其他文件
    帮助理解代码上下文
9. [ ] run_command：
    在用户系统上运行终端命令
    需要评估命令的安全性
    可以执行各种系统操作
1. [ ] command_status：
     查看之前执行的命令状态
     可以获取命令输出和执行结果
