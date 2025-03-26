import os
import requests
import zipfile
import io

def download_layui():
    # 创建目录
    os.makedirs('app/static/lib/layui', exist_ok=True)
    
    # 下载 layui
    url = 'https://github.com/layui/layui/releases/download/v2.9.6/layui-v2.9.6.zip'
    print('正在下载 Layui...')
    response = requests.get(url)
    
    # 解压文件
    print('正在解压文件...')
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        # 只解压需要的文件
        for file in zip_ref.namelist():
            if file.startswith('layui-v2.9.6/layui/'):
                # 获取目标路径
                target_path = os.path.join('app/static/lib/layui', file.replace('layui-v2.9.6/layui/', ''))
                # 创建目录
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                # 解压文件
                if not file.endswith('/'):
                    with zip_ref.open(file) as source, open(target_path, 'wb') as target:
                        target.write(source.read())
    
    print('Layui 安装完成！')

if __name__ == '__main__':
    download_layui() 