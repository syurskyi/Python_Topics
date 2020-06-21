______ ___
__ 'PyQt5' __ ___.modules:
    ____ ? ______ ?C.., ?W..
    ____ ?.?C.. ______ __, pS.. __ Signal

____
    ____ PySide2 ______ ?C.., ?W..
    ____ PySide2.?C.. ______ Signal


PALETTES _ {
    # bokeh paired 12
    'paired12':['#000000', '#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928', '#ffffff'],
    # d3 category 10
    'category10':['#000000', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ffffff'],
    # 17 undertones https://lospec.com/palette-list/17undertones
    '17undertones': ['#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49', '#458352','#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b', '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff']
}


c_ _PaletteButton(?W...?PB..):
    ___  -   color):
        s_. - ()
        sFS..(?C...?S..(24, 24))
        color _ color
        sSS..("background-color: %s;" % color)

c_ _PaletteBase(?W...?W..):

    selected _ Signal(object)

    ___ _e.._color  color):
        selected.e..(color)


c_ _PaletteLinearBase(_PaletteBase):
    ___  -   colors, $ $$
        s_. - ($ $$)

        __ isinstance(colors, st.):
            __ colors __ PALETTES:
                colors _ PALETTES[colors]

        palette _ layoutvh()

        ___ c __ colors:
            b _ _PaletteButton(c)
            b.pressed.c..(
                l___ c_c: _e.._color(c)
            )
            palette.aW..(b)

        sL..(palette)


c_ PaletteHorizontal(_PaletteLinearBase):
    layoutvh _ ?W...?HBL..


c_ PaletteVertical(_PaletteLinearBase):
    layoutvh _ ?W...?VBL..


c_ PaletteGrid(_PaletteBase):

    ___  -   colors, n_columns_5, $ $$
        s_. - ($ $$)

        __ isinstance(colors, st.):
            __ colors __ PALETTES:
                colors _ PALETTES[colors]

        palette _ ?W...QGridLayout()
        row, col _ 0, 0

        ___ c __ colors:
            b _ _PaletteButton(c)
            b.pressed.c..(
                l___ c_c: _e.._color(c)
            )
            palette.aW..(b, row, col)
            col +_ 1
            __ col __ n_columns:
                col _ 0
                row +_ 1

        sL..(palette)
