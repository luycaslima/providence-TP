import bpy

bl_info = {
    "name": "Providence - View Texture Mapper",
    "description": "Creates Textures using images and the Projection Texture mapping method.",
    "author": "Lucas Lima da Silva Santos (luycaslima@gmail.com)",
    "doc_url": "",
    "version": (0, 0, 0, 1),
    "blender": (4, 1, 0),
    "location": "View3D",
    "category": "Texturing"
}

#define the properties of the addon in the panel
class Providence_Props(bpy.types.PropertyGroup):
    pass


#Execute the main function of the addon
class Providence_Operator(bpy.types.Operator):
    """Project a image to the UV of an selected Object"""
    bl_label="Execute"
    bl_idname="providence.execute"
    bl_options = {"INTERNAL","UNDO"} #Enable undo operations

    def execute(self,context):
        #mesh = bpy.types.Mesh(0)
        #camera = bpy.types.Camera(0)


        return{'FINISHED'}
    pass

#define the UI panels
class VIEW3D_PT_Providence_Panel(bpy.types.Panel):
    # where to add the panel on the UI
    bl_space_type = "VIEW_3D" #3D VIEWPORT AREA - https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items
    bl_region_type= "UI" #SIDEBAR REGION - see blender documentation - https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items
    bl_category = "Providence"
    # add labels
    bl_label ="Texture Projection's Tool" # add to the top of the panel
    
    #define the layout of the panel
    def draw(self,context): 
        #define the layout of the panel
        layout = self.layout
        ui = layout.column(align=True)
        
        exec_row = ui.row()
        exec_row.scale_y = 2.0
        exec_row.operator('providence.execute')
        pass
    pass


#register  the panel on blender
def register():
    bpy.utils.register_class(VIEW3D_PT_Providence_Panel)
    bpy.utils.register_class(Providence_Operator)
    bpy.utils.register_class(Providence_Props)
    print("Start")

#unregister the panel
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_Providence_Panel)
    bpy.utils.unregister_class(Providence_Operator)
    bpy.utils.unregister_class(Providence_Props)
    print("finish")

if __name__ == "__main__":
    register()