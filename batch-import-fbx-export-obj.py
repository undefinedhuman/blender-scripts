import bpy
import os

path = "REPLACE WITH FBX DIRECTORY PATH"

model_list = os.listdir( path )

for model in model_list:
    if model != ".DS_Store":

        bpy.ops.import_scene.fbx( filepath = path + model )

        obs = bpy.context.selected_objects

        for ob in obs:
            #deselect all but just one object and make it active
            bpy.ops.object.select_all(action='DESELECT')
            ob.select_set(state=True)
            bpy.context.view_layer.objects.active = ob

            ob.data.polygons.foreach_set('use_smooth',  [True] * len(bpy.context.object.data.polygons))

            bpy.ops.object.location_clear()

            #export fbx
            filename = "REPLACE WITH PATH WHERE OBJ WILL BE SAVED" + ob.name + '.obj'

            bpy.ops.export_scene.obj(filepath=filename,
                                check_existing=True,
                                axis_forward='-Z',
                                axis_up='Y',
                                filter_glob="*.obj;*.mtl",
                                use_selection=True,
                                use_animation=False,
                                use_mesh_modifiers=False,
                                use_edges=False,
                                use_smooth_groups=False,
                                use_smooth_groups_bitflags=False,
                                use_normals=True,
                                use_uvs=True,
                                use_materials=False,
                                use_triangles=True,
                                use_nurbs=False,
                                use_vertex_groups=False,
                                use_blen_objects=True,
                                group_by_object=False,
                                group_by_material=False,
                                keep_vertex_order=False,
                                global_scale=1,
                                path_mode='AUTO')

            bpy.ops.object.delete()
