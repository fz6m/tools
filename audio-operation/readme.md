## Python 音频操作

### 使用前

安装依赖：
```py
    pip install pydub
```

下载 ffmpeg ：
[官网下载](https://ffmpeg.zeranoe.com/builds/)

下载完 ffmpeg 压缩包后将其解压，并在系统路径中添加其 `/bin` 目录
例：`E:/ffmpeg/bin`

之后找到安装的 pydub 依赖根目录 `Python/Lib/site-packages/pydub/utils.py` 修改该文件：
```py
def which(program):
    """
    Mimics behavior of UNIX which command.
    """
    # Add .exe program extension for windows support
    if os.name == "nt" and not program.endswith(".exe"):
        program += ".exe"

    envdir_list = [os.curdir] + os.environ["PATH"].split(os.pathsep)
    # 添加下面这一行，append 内容为刚刚 ffmpeg 的 bin 目录
    envdir_list.append('E:/ffmpeg/bin')

    for envdir in envdir_list:
        program_path = os.path.join(envdir, program)
        if os.path.isfile(program_path) and os.access(program_path, os.X_OK):
            return program_path
```

### 使用说明

参考以下内容获取更多使用方法：

Pydub 库项目地址：[jiaaro / pydub](https://github.com/jiaaro/pydub)

API 说明文档：[API Documentation](https://github.com/jiaaro/pydub/blob/master/API.markdown)
