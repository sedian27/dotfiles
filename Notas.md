#Después de instalar Arch:
#Recuerda primero instalar xorg.
sudo pacman -S lightdm lightdm-gtk-greeter qtile alacritty xorg-xinit pulseaudio pavucontrol pamixer brightnessctl
sudo systemctl enable lightdm
reboot

#Instalación de programas en mí orden:
sudo pacman -S firefox rofi picom ranger thunar neovim udiskie ntfs-3g network-manager-applet volumeicon cbatticon libnotify notification-daemon arandrxcb-util-cursor lxappearance vlc
yay -S visual-studio-code-bin spotify
sudo pacman -S exa
yay -S ccat

#Fondo de pantalla
sudo pacman feh
#cambiar tema rofi
sudo pacman -S which
rofi-theme-selector

#copiar de dotfiles:
.config/qtile > ~/.config
.xprofile > ~/
.bashrc > ~/ #recuerda instalar exa y ccat o borrar los alias.
# Si usas GIT borra la ultima línea y descomenta las anteriores.
# y guarda esto cómo .git-prompt.sh -> https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh

#Apoyo para instalar Drivers de nvidia y utilidades:
https://github.com/helmuthdu/aui
#Dotfiles base
https://github.com/antoniosarosi/dotfiles

#Personalizar terminal
sudo pacman -S fish
curl -L https://get.oh-my.fish | fish

cp -r dotfiles/.config/fish ~/.config
cp -r dotfiles/.config/omf ~/.config

omf install

temas:
omf theme agnoster
omf theme spacefish


#Fuentes
#Principalmente para no tener problemas:
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
yay -S nerd-fonts-ubuntu-mono nerd-fonts-mononoki


#Editores de Texto
visual-studio-code-bin -> AUR
¿Por que utilizarlo? -> Sincronización de extensiones, temas, etc.. y porque se puede conectar con SQL-Server
neovim
#Enlazar vim:
cd /bin
sudo ln -s nvim vim

#Sonido y Musica
pulseaudio pavucontrol pamixer #audio
spotify  -> AUR, si no tienes premium: después de instalarlo instala spotify-adblock-git :).



#PROGRAMAS QUE USO
Dbeaver
#SQL SERVER:
yay -S mssql-server msodbcsql mssql-tools
sudo /opt/mssql/bin/mssql-conf setup
sudo systemctl start/stop mssql-server
azuredatastudio
jdownloader2
openvpn
yay -S protonvpn-cli-ng
bluez-utils
intellij-idea-ultimate-edition -> aur
mysql -> aur
mysql-workbench
geeqie
xorg-server-xephyr
kite
tomcat9
nodejs
