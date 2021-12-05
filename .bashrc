#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# Custom Statements

# Paths
export PATH=~/thewhistlerScripts/:$PATH
export PATH=~/.config/rofi/bin:$PATH
export PATH=~/.local/bin:$PATH

# Aliases
alias check='heroku logs -n 1500 -a grih-karya | grep -v Restart | grep -v "Nav Srijan"' 
alias checkdb='heroku pg:psql postgresql-crystalline-15463 --app grih-karya'
alias vi=nvim
alias vim=nvim
alias minecraft='java -jar ~/TLauncher/TLauncher-2.8.jar'

export HISTCONTROL=ignorespace

[ -f ~/.fzf.bash ] && source ~/.fzf.bash
