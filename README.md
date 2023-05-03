
### 初始化本地倉庫

-  git init

### 檢查目前倉庫狀態

- git status

### 加入需要管理的程式檔案
- git add test.py
- git add .

### 新增忽略檔案
- .gitignore

### 進行commit儲存動作

- git commit -am "commit log"

### 檢視目前commit歷程

- git log

### 綁定員端倉庫url
###先做git remote add origin https://github.com/ChangyuChen123/XXXXXXX.git

- git add remot https://www.github.com/changyu123/xxxxxx
- git remote -v

### 推送程式碼
- git push -u origin master
- git push
- git push -f #強制上傳至雲端github

###合併上一次的commit
- git commit --amend
- 接下來按:wq


# 建立虛擬環境

### 建立新CONDA環境
- conda create -n linebot_env

#也可用這個
- pip install pipenv 
- conda create --name myenv python=3.8

###選擇新環境

- conda activate myenv
- pip list #查看環境套件

###新環境增加套件
- 在程式裡使用的套件
- pip install XXXX

### 與雲端伺服器介接套件(重要)
- pip install gunicorn

###套件整理成文字檔
- pip freeze > requirements.txt


###終端機退出環境

- conda deactivate
