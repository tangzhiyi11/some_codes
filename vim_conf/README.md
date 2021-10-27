# 我自己使用的 vim 配置

## vim-plug
插件管理工具，仓库地址：https://github.com/junegunn/vim-plug/wiki/tutorial

安装
```
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```


## vimrc配置

```
colorscheme elflord
set nu
set expandtab
set ts=4

" Plugins will be downloaded under the specified directory.
call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')

" Declare the list of plugins.
Plug 'tpope/vim-sensible'
Plug 'junegunn/seoul256.vim'
Plug 'preservim/nerdtree'
Plug 'kien/ctrlp.vim'
"Plug 'dense-analysis/ale'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" List ends here. Plugins become visible to Vim after this call.
call plug#end()

" nerdtree
map <F3> :NERDTreeMirror<CR>
map <F3> :NERDTreeToggle<CR>
```

配置完之后，用 vim 打开任意文本，然后键入`:PlugInstall`进行安装（或者键入 `:PlugInstall 插件名(最后一个/后的名字，如ctrlp.vim)` 进行安装）

## 常用技巧

- ctrlp
  - 使用 <Ctrl-v> 垂直分割窗口打开文件
  - 使用 <Ctrl-x> 水平分割窗口打开文件
- 注释颜色看不清
  - colorscheme elflord # 换一个颜色主题，可以直接加在vimrc里
