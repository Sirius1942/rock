#!/usr/bin/env sh

# 确保脚本抛出遇到的错误
set -e

# 生成静态文件
git init
git add -A
git commit -m 'deploy'
git push -u origin master
cd -