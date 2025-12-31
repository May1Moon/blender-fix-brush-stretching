import bpy

class MESH_OT_FixBrushStretching(bpy.types.Operator):
    bl_idname = "mesh.fix_scaling"
    bl_label = "fix scaling"
     
    def execute(self, context): 
        obj = context.active_object
        
        
        if not obj or obj.type != 'MESH':
            self.report({'ERROR'}, "Select a mesh object")
            return {'CANCELLED'}
        
        prev_mode = obj.mode
        
        if prev_mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
            
            

        bpy.ops.object.transform_apply(location=False,rotation=False, scale=True)
        
        if prev_mode != 'OBJECT':
            bpy.ops.object.mode_set(mode=prev_mode)
        
        return {'FINISHED'}
    
#@classmethod
#def poll(cls, context):
#    return context.mode == 'SCULPT'
    
class FixPanel(bpy.types.Panel):
    bl_label = "Brush stretching"
    bl_idname = "PT_Brush_stretching"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tools"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "scale")
        
        row = layout.row()
        row.operator("mesh.fix_scaling")
        
        
def register():
    bpy.utils.register_class(MESH_OT_FixBrushStretching)
    bpy.utils.register_class(FixPanel)
    
    
def unregister():
    
    bpy.utils.unregister_class(FixPanel)
    bpy.utils.unregister_class(MESH_OT_FixBrushStretching)
    
    
if  __name__ == '__main__':
    register()
    