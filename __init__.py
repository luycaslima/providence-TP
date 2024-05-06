import bpy

from . projection import calculate_cam_projection

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
    tex_width: bpy.props.IntProperty(default=512, min=2, subtype='PIXEL', description="Width of the generated texture.")
    tex_height : bpy.props.IntProperty(default=512, min=2, subtype='PIXEL', description="Height of the generated texture.")
    pass


#Execute the main function of the addon
class Providence_Operator(bpy.types.Operator):
    """Project a image to the UV of an selected Object"""
    bl_label="Execute"
    bl_idname="providence.execute"
    bl_options = {"INTERNAL","UNDO"} #Enable undo operations

    def execute(self,context):
        mesh = []
        camera = []

        #Get visible objects
        objs = context.visible_objects
        for obj in objs:
            if obj.type == "MESH":
                if len(obj.data.polygons) > 0 and len(obj.data.uv_layers) > 0:
                    mesh.append(obj)
                    print(obj.matrix_world)
            if obj.type == "CAMERA":
                if len(obj.data.background_images) > 0:
                    #print(obj.matrix_world.inverted())
                    camera.append(obj)
        
        print("Cameras with image: {} Objects with UV: {}".format(len(camera),len(mesh)))
        
        calculate_cam_projection(camera,512,512)

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

        #List of objects and cameras used
        entities_row= ui.row()
        entities_row.label(text="Entities:")
        #entities_row.prop('')

        ui.separator()
        textures_props_row = ui.row()
        textures_props_row.label(text="Texture Properties:")
        col = ui.column(align=True)
        col.prop(context.scene.providence,'tex_width',text="X")
        col.prop(context.scene.providence,'tex_height',text="Y")
        
        ui.separator()
        #Execution row
        exec_row = ui.row()
        exec_row.scale_y = 2.0
        exec_row.operator('providence.execute')
        pass
    pass


#register  the panel on blender
def register():
    bpy.utils.register_class(Providence_Props)
    bpy.utils.register_class(VIEW3D_PT_Providence_Panel)
    ## Add reference to the program in the scene to the properties
    bpy.types.Scene.providence = bpy.props.PointerProperty(type=Providence_Props)
    bpy.utils.register_class(Providence_Operator)
    print("Start")

#unregister the panel
def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_Providence_Panel)
    bpy.utils.unregister_class(Providence_Operator)
    bpy.utils.unregister_class(Providence_Props)
    print("finish")

if __name__ == "__main__":
    register()