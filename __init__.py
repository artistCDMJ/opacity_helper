# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {"name": "Eevee Opacity Panel",
           "author": "CDMJ",
           "version": (2, 00, 0),
           "blender": (2, 80, 0),
           "location": "Toolbar > Misc Tab > Opacity",
           "description": "helper panel for multiple object opacity assignment",
           "warning": "",
           "category": "Object"}

import bpy



class OBJECT_OT_group_opaque(bpy.types.Operator):
    """Set Opaque"""
    bl_idname = "object.group_opaque"


    bl_label = "Set Selection to Opaque"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        for o in context.selected_objects:
            o.active_material.blend_method = 'OPAQUE'       
                
        return {'FINISHED'}

class OBJECT_OT_group_alpha_blend(bpy.types.Operator):
    """Set Alpha Blend"""
    bl_idname = "object.group_blend"


    bl_label = "Set Selected to Alpha Blend"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        for o in context.selected_objects:
            o.active_material.blend_method = 'BLEND'       
                
        return {'FINISHED'}

class OBJECT_OT_group_alpha_hashed(bpy.types.Operator):
    """Set Alpha Hashed"""
    bl_idname = "object.group_hashed"


    bl_label = "Set Selected to Alpha Hashed"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        for o in context.selected_objects:
            o.active_material.blend_method = 'HASHED'       
                
        return {'FINISHED'}

class OBJECT_OT_group_alpha_clip(bpy.types.Operator):
    """Set Alpha clip"""
    bl_idname = "object.group_clip"


    bl_label = "Set Selected to Alpha Clip"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        for o in context.selected_objects:
            o.active_material.blend_method = 'CLIP'       
                
        return {'FINISHED'}    

class OBJECT_OT_group_alpha_multiply(bpy.types.Operator):
    """Set Alpha multiply"""
    bl_idname = "object.group_multiply"


    bl_label = "Set Selected to Alpha Multiply"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        for o in context.selected_objects:
            o.active_material.blend_method = 'MULTIPLY'       
                
        return {'FINISHED'}    
    
class OBJECT_OT_group_alpha_add(bpy.types.Operator):
    """Set Alpha add"""
    bl_idname = "object.group_add"


    bl_label = "Set Selected to Alpha Additive"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        for o in context.selected_objects:
            o.active_material.blend_method = 'ADD'       
                
        return {'FINISHED'}   



class PANEL_PT_opacity_panel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_idname = "opacity.settings"
    bl_space_type = 'VIEW_3D'
    bl_label = "Settings"
    bl_region_type = "UI"
    bl_category = "Opacity Helper"

    #if bpy.context.scene.render.engine == 'BLENDER_EEVEE':

    def draw(self, context):
        layout = self.layout

        box = layout.box()                             
        col = box.column(align = True)
        col.label(text="Change Selected Opacity")

        row = col.row(align=True)
        #row.scale_y = 2.0
        #row1=row.split(align=True)
        #row1.scale_x=0.50
        #row1.scale_y=2.0
        row.operator("object.group_blend", text = "ALPHA BLEND")
        row = col.row(align=True)
        row.operator("object.group_hashed", text = "ALPHA HASHED")
        row = col.row(align=True)
        row.operator("object.group_clip", text = "ALPHA CLIP")
        row = col.row(align=True)
        row.operator("object.group_multiply", text = "MULTIPLY")
        row = col.row(align=True)
        row.operator("object.group_add", text = "ADD")
        row = col.row(align=True)
        row.operator("object.group_opaque", text = "OPAQUE")
                                

classes = (
    OBJECT_OT_group_alpha_add,
    OBJECT_OT_group_opaque,
    OBJECT_OT_group_alpha_clip,
    OBJECT_OT_group_alpha_multiply,
    OBJECT_OT_group_alpha_hashed,
    OBJECT_OT_group_alpha_blend,
    PANEL_PT_opacity_panel
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
