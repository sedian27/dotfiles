# Dotfiles & configs

# Después de instalar Arch:
Qtile "*tiling window manager*"
```bash
sudo pacman -S lightdm lightdm-gtk-greeter qtile alacritty
sudo systemctl enable lightdm
```
reboot

## Xprofile

Como he mencionado antes, estos cambios no son permanentes. Para que lo sean
necesitamos un par de cosas. Primero instala
**[xinit](https://wiki.archlinux.org/index.php/Xinit)**:

```bash
sudo pacman -S xorg-xinit
```

Ahora puedes usar *~/.xprofile* para lanzar programas antes de que se ejecute
el gestor de ventanas:

```bash
touch ~/.xprofile
```

Por ejemplo, si escribes esto en tu *~/.xprofile*:

```bash
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0 &
setxkbmap latam &
nm-applet &
udiskie -t &
volumeicon &
cbatticon &
```

Cada vez que inicias sesión tendrás los iconos de la bandeja del sistema, tu
distribución de teclado y monitores configurados.

# Sonido:
```bash
sudo pacman -S pulseaudio pavucontrol pamixer
```

Ahora puedes establecer atajos de teclado para *pulseaudio*, abre el archivo de configuración de Qtile y añade esto:

```python
# Volumen
Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
```


# Control de Brillo:
```bash
sudo pacman -S brightnessctl
```

Puedes añadir estos atajos y volver a reiniciar Qtile:

```python
# Brillo
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
```



# Programas que utilizo:
## Navegador
```bash
sudo pacman -S firefox 
```

## Compositor

```bash
sudo pacman -S picom
# Pon esto en ~/.xprofile
picom &
```

## Menú

```bash
sudo pacman -S rofi
```

Atajos de teclado:

```python
Key([mod], "m", lazy.spawn("rofi -show run")),
Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
```

## Explorador de archivos

Terminal:
```bash
sudo pacman -S ranger
```

Grafico:
```bash
sudo pacman -S thunar
```

## Editor de Texto

En terminal:

```bash
sudo pacman -S neovim

enlazar vim:
cd /bin
sudo ln -s nvim vim
```

Grafico:

```bash
yay -S visual-studio-code-bin 
```

## Almacenamiento

Otra utilidad básica que podrías necesitar es montar de forma automática
unidades de almacenamiento externas. Para ello uso
**[udisks](https://wiki.archlinux.org/index.php/Udisks)**
y **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**.
*udisks* es una dependencia de *udiskie*, así que solo instalaremos este
último. Instala también el paquete
**[ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G)**
para leer y escribir en discos NTFS:
```bash
sudo pacman -S udiskie ntfs-3g
```

## Redes

Hemos configurado la red a través de *nmcli*, pero un programa gráfico es más
cómodo. Yo uso
**[nm-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**:

```bash
sudo pacman -S network-manager-applet
```
## Systray

Por defecto, tenemos una "bandeja del sistema" en Qtile, pero no hay nada
ejecutándose en ella. Puedes lanzar los programas que acabamos de instalar así:

```bash
udiskie -t &
nm-applet &
```

Ahora deberías ver unos iconos en la barra, puedes clicar en ellos para
configurar la red y discos. Puedes instalar también iconos para la batería y
el volumen:

```bash
sudo pacman -S volumeicon cbatticon
volumeicon &
cbatticon &
```

## Notificaciones

Me gusta tener notificaciones en el escritorio también, para ello tienes que
instalar
[**libnotify**](https://wiki.archlinux.org/index.php/Desktop_notifications#Libnotify)
y [**notification-daemon**](https://www.archlinux.org/packages/community/x86_64/notification-daemon/):

```bash
sudo pacman -S libnotify notification-daemon
```

En nuestro caso,
[esto es lo que tenemos que hacer para tener notificaciones](https://wiki.archlinux.org/index.php/Desktop_notifications#Standalone):

```bash
# Crea este fichero con nano o vim
sudo nano /usr/share/dbus-1/services/org.freedesktop.Notifications.service
# Pega estas líneas
[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon
```

Pruébalo:

```bash
notification-send "Hola Mundo"
```

## Monitores

Si tienes múltiples monitores, seguramente quieras usarlos todos. Así es como
funciona **[xrandr](https://wiki.archlinux.org/index.php/Xrandr)**:

```bash
# Lista todas las salidas y resoluciones disponibles
xrandr
# Formato común para un portátil con monitor extra
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0
```

Es necesario especificar la posición de cada salida, si no se utilizará 0x0, y
todas las salidas estarán solapadas. Ahora bien, si no quieres calcular píxeles
y demás necesitas una interfaz gráfica como
**[arandr](https://www.archlinux.org/packages/community/any/arandr/)**:

```bash
sudo pacman -S arandr
```

Ábrela con *rofi*, ordena las pantallas como quieras, y después puedes guardar
la disposición de las mismas, lo cual simplemente te dará un script con el
comando exacto de *xrandr* que necesitas. Guarda ese script, pero todavía no
le des al botón de aplicar.

Para un sistema con múltiples monitores deberías crear una instancia de *Screen*
por cada uno de ellos en la configuración de Qtile.

Encontrarás una lista llamada *screens* en la configuración de Qtile que
contiene solo un objeto inicializado con una barra en la parte de abajo.
Dentro de esa barra puedes ver los widgets con los que viene por defecto.

Añade tantas pantallas como necesites y copia-pega los widgets, más adelante
podrás personalizarlos. Ahora puedes volver a *arandr*, darle click en "apply"
y reiniciar el gestor de ventanats.

Con esto tus monitores deberían funcionar.

## Tema de GTK

Puedes instalar
también un tema de cursor distinto, para ello necesitas
**[xcb-util-cursor](https://www.archlinux.org/packages/extra/x86_64/xcb-util-cursor/)**.

```bash
sudo pacman -S xcb-util-cursor
```

Recuerda que solo verás los cambios si inicias sesión de nuevo. También hay
herramientas gráficas para cambiar temas puedes usar
**[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**,
que es un programa independiente del entorno de escritorio para realizar esta
tarea, y te permie previsualizar los temas.

```bash
sudo pacman -S lxappearance
```

### Vídeo y audio

Aquí sin duda el clásico
[vlc](https://wiki.archlinux.org/index.php/VLC_media_player_(Espa%C3%B1ol))
es lo que necesitamos:

```bash
sudo pacman -S vlc
```
spotify
sudo pacman -S exa
yay -S ccat

#Fondo de pantalla
sudo pacman feh
#cambiar tema rofi
sudo pacman -S which
rofi-theme-selector

# copiar de dotfiles:
```bash
cp -r .config/qtile ~/.config
cp -r .xprofile ~/
cp -r .bashrc ~/ #recuerda instalar exa y ccat o borrar los alias.
```

### Si usas GIT borra la ultima línea y descomenta las anteriores.
### y guarda esto cómo .git-prompt.sh -> https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh

## Apoyo para instalar Drivers de nvidia y utilidades:
https://github.com/helmuthdu/aui
## Dotfiles base
https://github.com/antoniosarosi/dotfiles

# Personalizar terminal
```bash
sudo pacman -S fish
curl -L https://get.oh-my.fish | fish

cp -r dotfiles/.config/fish ~/.config
cp -r dotfiles/.config/omf ~/.config

omf install

temas:
omf theme agnoster
omf theme spacefish
```

## Fuentes
```bash
Principalmente para no tener problemas:
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
yay -S nerd-fonts-ubuntu-mono nerd-fonts-mononoki
```

# PROGRAMAS QUE USO
Dbeaver
## SQL SERVER:
```bash
yay -S mssql-server msodbcsql mssql-tools
sudo /opt/mssql/bin/mssql-conf setup
sudo systemctl start/stop mssql-server
```
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
