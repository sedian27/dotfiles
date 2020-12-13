
from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

icon = lambda fg='text', bg='dark', fontsize=16, text="?": widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=3
)

powerline = lambda fg="light", bg="dark": widget.TextBox(
   **base(fg, bg),
    text="", # Icon: nf-oct-triangle_left
    fontsize=37,
    padding=-2
)

workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    separator(),
    widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
    separator(),
]

primary_widgets = [
    *workspaces(),

    separator(),

    #powerline('color3', 'dark'),

    icon(fg="light", text=' '), # Icon: nf-fa-download
    
    widget.Pacman(**base(fg='light'), update_interval=1800),

    separator(),
    icon(fg="light", text=' '), # Icon: nf-fa-download
    widget.Volume(**base(fg='light'), get_volume_command='amixer'),

    #powerline('color3', 'color4'),

    #icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    
    #widget.Net(**base(bg='color3'), interface='wlp2s0'),

    #powerline('color2', 'color3'),

    #powerline('color1', 'color2'),

    separator(),
    icon(fg="light", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(fg='light'), format='%d/%m/%Y - %H:%M '),

    #powerline('dark', 'color2'),
    widget.Battery(**base(fg='light'), format='{percent:2.0%}', charge_char='ﮣ', low_foreground='#FF0000'),

    widget.Systray(background=colors['dark'], padding=5),

    widget.CurrentLayoutIcon(**base(bg='dark'), scale=0.65),
    #widget.CurrentLayout(**base(bg='dark'), padding=5),
]

secondary_widgets = [
    *workspaces(),

    
    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),
    
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()