#!/usr/bin/env python

from gimpfu import *

def python_drawrows(timg, tdrawable, rowSize=10, columnSize=10, fontname="Arial", fontsize=8, unit=3, textPos=20):
    gimp.context_push()
    timg.undo_group_start()
    
    # start plugin
    width = tdrawable.width
    height = tdrawable.height    
    
    # draw rows - black - red -green - blue - yellow - white - purple - gray
    colors = [(0,0,0), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,255,255), (255,0,255), (128,128,128)]
    horCounter = 0
    colorIndex = 0
        
    # draw rows
    while (horCounter < height):
        # CHANNEL-OP-ADD (0), CHANNEL-OP-SUBTRACT (1), CHANNEL-OP-REPLACE (2), CHANNEL-OP-INTERSECT (3)        
        pdb.gimp_image_select_rectangle(timg, CHANNEL_OP_REPLACE, 0, horCounter, width, rowSize)
        color = colors[colorIndex]
        gimp.set_foreground(color)
        pdb.gimp_edit_fill(tdrawable, FOREGROUND_FILL)
             
        
        # text
        textColor = (255,255,255)
        if (color == (0,0,0)):
            textColor = (255,255,255)
        if (color == (255,255,255)):
            textColor = (0,0,0)
        gimp.set_foreground(textColor)
        layer = pdb.gimp_text_layer_new(timg, horCounter, fontname, fontsize, unit)
        layer.translate(textPos, horCounter) 
        # gimp-image-insert-layer image, layer, parent, position
        pdb.gimp_image_insert_layer(timg, layer, None, 0)
        textColor = (255,255,255)
        
        horCounter = horCounter + rowSize
        # change the colorIndex
        colorIndex = colorIndex + 1
        if colorIndex == len( colors ):
            colorIndex = 0
    
    # clean up
    timg.undo_group_end()        
    gimp.displays_flush()
    gimp.context_pop()

register(
        "python_fu_drawrows",
        "draw lines",
        "draw lines",
        "Christian Thillemann",
        "Christian Thillemann",
        "1997-1999",
        "<Image>/Filters/Artistic/_DrawRows...",
        "RGB*, GRAY*",
        [
                (PF_INT, "row_size", "Size of row in color", 10),
                (PF_INT, "column_size", "Size of column in color", 10),                
                (PF_FONT, "font", "font", "Arial"),  
                (PF_INT, "font_size", "Font size", 8),
                (PF_INT, "unit_size", "Unit", 3),
                (PF_INT, "textPosition", "Text Position (x)", 20)
                
        ],
        [],
        python_drawrows)

main()