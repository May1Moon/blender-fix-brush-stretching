# blender-fix-brush-stretching
Blender Fix Brush Stretching

A small Blender add-on that fixes sculpt brush stretching caused by non-applied object scale.

When a mesh is scaled in Object Mode without applying the scale, sculpt brushes can become stretched/distorted because Blender uses a scale multiplier during brush calculations. This add-on applies the object’s scale (Ctrl + A → Scale) to the mesh, converting the transform into real geometry so sculpt brushes behave correctly again

How to use:
Select a mesh object, open the 3D Viewport sidebar, go to the Tools tab, and click “Fix Brush Stretching”.

Additional Note:
This tool fixes scale-related brush distortion only.

