 - 使用步骤：
 - 请确保安装python
   - 请确保安装所有依赖库
    - 请确保已经输入你的密钥到gpt.bat中

在此目录右键打开CMD窗口输入gpt，或者直接双击gpt.bat即可

依赖库安装：
```
pip install openai
pip install colorama
```

密钥配置：在gpt.bat中第二行填上你的密钥，例如
```
set OPENAI_KEY=sk-************************************************
```

示例：
![demo_img](screenshot/demo.png)

 ### 帮助：
以_开头的是指令哦，目前支持有stop，clear，export三个命令

| 命令     | 工作      |
|--------|---------|
| stop   | 退出gpt   |
| clear  | 清空上下文   |
| export | 导出对话到桌面 |

例如：_stop将退出程序