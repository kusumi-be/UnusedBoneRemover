# information
bl_info = {
    "name": "Unused Bone Remover",
    "description": "選択メッシュに使われていないボーンを削除するアドオンです。  VRChatの衣装作成にて必要な「素体に不要なボーンの削除」を効率化するために作りました",
    "author": "kusumi_bell",
    "version": (1, 0, 0),
    "blender": (4, 2, ),
    "location": "3D VIEW",
    "category": "Object" 
}


# import
import bpy

# UI
class RemoveUnusedBoneUI(bpy.types.Panel):
  bl_label = "UnusedBoneRemover"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "BoneRemover"

  def draw(self, context):
    layout = self.layout
    layout.operator(RemoveUnusedBone.bl_idname, text="Remove unused bone")


# operator
class RemoveUnusedBone(bpy.types.Operator):
  bl_idname = "remove_unused_bone.operator"
  bl_label = "Remove"


  # 実行時に呼ばれる関数
  def execute(self, context):
    # 選択メッシュを取得する
    selected_objects = bpy.context.selected_objects

    # 選択メッシュに含まれる頂点グループを取得する
    selected_vertex_groups = []
    for obj in selected_objects:
      selected_vertex_groups.append(obj.vertex_groups)


    # Amatureを探す
    if bpy.context.object.type == 'ARMATURE':
      armature = bpy.context.object
    else:
      self.report({'ERROR'}, "エラー：Armatureを最後に選択してください")
      return {'CANCELLED'}
    if armature is None:
      self.report({'ERROR'}, "エラー：Armatureが見つかりませんでした")
      return {'CANCELLED'}


    # ボーンをすべて選択する
    for bone in armature.data.bones:
      bone.select = True
      bone.select_head = True
      bone.select_tail = True


    # 選択メッシュで利用するボーンの選択を解除する
    for v_groups in selected_vertex_groups:
      for v_group in v_groups:
        print(v_group.name)
        # 選択メッシュで利用するボーンの選択を解除する
        armature.data.bones[v_group.name].select = False
        armature.data.bones[v_group.name].select = False
        armature.data.bones[v_group.name].select = False


    # 選択解除されていないボーンを削除
    bpy.ops.object.mode_set(mode='EDIT')
    selected_bones = [bone for bone in armature.data.edit_bones if bone.select]
    for bone in selected_bones:
      armature.data.edit_bones.remove(bone)

    bpy.ops.object.mode_set(mode='OBJECT')

    return {'FINISHED'}

classes = [
  RemoveUnusedBone,
  RemoveUnusedBoneUI
]

def menu_fn(self, context):
    self.layout.separator()
    self.layout.operator(RemoveUnusedBone.bl_idname)

def register():
  for c in classes:
      bpy.utils.register_class(c)
  bpy.types.VIEW3D_MT_object.append(menu_fn)

def unregister():
  bpy.types.VIEW3D_MT_mesh_add.remove(menu_fn)
  for c in classes:
    bpy.utils.unregister_class(c)

if __name__ == "__main__":
  register()