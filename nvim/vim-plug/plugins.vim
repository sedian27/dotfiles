call plug#begin('~/.config/nvim/plugged')
" Multi cursor
Plug 'terryma/vim-multiple-cursors'
" Comment code
"Plug 'tpope/vim-commentary'
" Easy motion for VSCode
"Plug 'asvetliakov/vim-easymotion'
" Syntax support
"Plug 'sheerun/vim-polyglot'
" Autopairs
"Plug 'jiangmiao/auto-pairs'
" File explorer
"Plug 'scrooloose/NERDTree'    
" Icons
"Plug 'ryanoasis/vim-devicons'
" Intellisense
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
" Airline
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
" Indent guides
"Plug 'Yggdroot/indentLine' 
" Git integration
"Plug 'mhinz/vim-signify'
" Autoclose tags
"Plug 'alvan/vim-closetag'
" Ranger
"Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
" Fzf
"Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
"Plug 'junegunn/fzf.vim'
"Plug 'airblade/vim-rooter'
" Prettier
Plug 'prettier/vim-prettier', { 'do': 'yarn install' }
" Themes
Plug 'joshdick/onedark.vim'
"Plug 'crusoexia/vim-monokai'
"Plug 'ayu-theme/ayu-vim'
call plug#end()
