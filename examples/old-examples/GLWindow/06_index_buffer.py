"""
NOTE: This example is from ModernGL 4 or earlier. We simply disable and archive them for now.
"""

# import struct

# import GLWindow
# import ModernGL

# wnd = GLWindow.create_window()
# ctx = ModernGL.create_context()

# prog = ctx.program(
#     ctx.vertex_shader('''
#         #version 330

#         in vec2 vert;

#         void main() {
#             gl_Position = vec4(vert, 0.0, 1.0);
#         }
#     '''),
#     ctx.fragment_shader('''
#         #version 330

#         out vec4 color;

#         void main() {
#             color = vec4(0.3, 0.5, 1.0, 1.0);
#         }
#     '''),
# ])

# vbo = ctx.buffer(struct.pack(
#     '8f',
#     -0.5, -0.5,
#     -0.5, 0.5,
#     0.5, -0.5,
#     0.5, 0.5,
# ))

# ibo = ctx.buffer(struct.pack('6i', 0, 1, 2, 1, 2, 3))

# vao_content = [
#     (vbo, '2f', ['vert']),
# ]

# vao = ctx.vertex_array(prog, vao_content, ibo)

# while wnd.update():
#     ctx.viewport = wnd.viewport
#     ctx.clear(0.9, 0.9, 0.9)
#     vao.render()
