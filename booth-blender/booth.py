"""Build a club booth (4 CDJ-style players + 4-channel mixer) entirely from code and render it with Cycles.

Headless render:  blender -b -P booth.py -- <shot: hero|close|dj> <pct> <samples> <out.png>
Live build:       run inside an open Blender (Scripting tab or MCP). Clears the scene's data and rebuilds it,
                  without resetting preferences or add-ons, and without rendering.
Run textures.py first (it writes the screen textures into tex/).
"""
import bpy, math, os, sys, random

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(HERE, "tex")
ARGS = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
LIVE = not bpy.app.background and not ARGS
shot = ARGS[0] if ARGS else "hero"
pct = int(ARGS[1]) if len(ARGS) > 1 else 50
samples = int(ARGS[2]) if len(ARGS) > 2 else 64
out = ARGS[3] if len(ARGS) > 3 else os.path.join(HERE, "out.png")

if LIVE:
    # wipe only scene data, so preferences and add-ons (MCP) stay as they are
    for o in list(bpy.data.objects):
        bpy.data.objects.remove(o, do_unlink=True)
    for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras,
                 bpy.data.curves, bpy.data.images, bpy.data.worlds, bpy.data.node_groups):
        for d in list(coll):
            if d.users == 0 or coll is not bpy.data.worlds:
                coll.remove(d)
else:
    bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
col = sc.collection

# ---------------------------------------------------------------- materials
MATS = {}
def mat(name, color=(0.02, 0.02, 0.02), rough=0.4, metal=0.0, emit=None, strength=0.0, coat=0.0, image=None, img_strength=1.0, generated=False, grain=0.0):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    p = nt.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = (*color, 1)
    p.inputs["Roughness"].default_value = rough
    p.inputs["Metallic"].default_value = metal
    if coat:
        p.inputs["Coat Weight"].default_value = coat
        p.inputs["Coat Roughness"].default_value = 0.08
    if grain:
        nz = nt.nodes.new("ShaderNodeTexNoise")
        nz.inputs["Scale"].default_value = 900.0
        nz.inputs["Detail"].default_value = 4.0
        mr = nt.nodes.new("ShaderNodeMapRange")
        mr.inputs["To Min"].default_value = max(0.0, rough - grain)
        mr.inputs["To Max"].default_value = min(1.0, rough + grain)
        nt.links.new(nz.outputs["Fac"], mr.inputs["Value"])
        nt.links.new(mr.outputs["Result"], p.inputs["Roughness"])
        bm = nt.nodes.new("ShaderNodeBump")
        bm.inputs["Strength"].default_value = 0.04
        nt.links.new(nz.outputs["Fac"], bm.inputs["Height"])
        nt.links.new(bm.outputs["Normal"], p.inputs["Normal"])
    if emit:
        p.inputs["Emission Color"].default_value = (*emit, 1)
        p.inputs["Emission Strength"].default_value = strength
    if image:
        tx = nt.nodes.new("ShaderNodeTexImage")
        tx.image = bpy.data.images.load(os.path.join(TEX, image))
        if generated:
            tc = nt.nodes.new("ShaderNodeTexCoord")
            nt.links.new(tc.outputs["Generated"], tx.inputs["Vector"])
        nt.links.new(tx.outputs["Color"], p.inputs["Emission Color"])
        p.inputs["Emission Strength"].default_value = img_strength
        p.inputs["Base Color"].default_value = (0.0, 0.0, 0.0, 1)
        p.inputs["Roughness"].default_value = 0.4 if generated else 0.14
        p.inputs["Specular IOR Level"].default_value = 0.25 if generated else 0.5
    MATS[name] = m
    return m

BODY = lambda: mat("body", (0.010, 0.010, 0.011), 0.42, 0.2, grain=0.08)
TOP = lambda: mat("top", (0.011, 0.011, 0.012), 0.42, 0.3, grain=0.1)
RUBBER = lambda: mat("rubber", (0.028, 0.028, 0.03), 0.62, grain=0.08)
METAL = lambda: mat("metal", (0.62, 0.62, 0.64), 0.24, 1.0, grain=0.05)
DARKMETAL = lambda: mat("darkmetal", (0.07, 0.07, 0.075), 0.32, 1.0, grain=0.06)
SATIN = lambda: mat("satin", (0.01, 0.01, 0.012), 0.38, 0.5, coat=0.2)
SLOT = lambda: mat("slot", (0.003, 0.003, 0.003), 0.9)
PAINT = lambda: mat("paint", (0.6, 0.6, 0.62), 0.55)

def emissive(name, rgb, s):
    return mat(name, tuple(c * 0.3 for c in rgb), 0.35, emit=rgb, strength=s)

def finish(o, m, bevel=0.0, segs=3):
    o.data.materials.append(m)
    if bevel:
        b = o.modifiers.new("bevel", "BEVEL")
        b.width = bevel
        b.segments = segs
        b.limit_method = "ANGLE"
        b.harden_normals = True
    for poly in o.data.polygons:
        poly.use_smooth = True
    return o

def box(loc, dims, m, bevel=0.002, rot=None, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.active_object
    o.scale = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if rot:
        o.rotation_euler = rot
    if parent:
        o.parent = parent
        o.location = loc
    return finish(o, m, bevel)

def cyl(loc, r, h, m, bevel=0.0, verts=72, parent=None):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=loc)
    o = bpy.context.active_object
    if parent:
        o.parent = parent
        o.location = loc
    return finish(o, m, bevel)

def torus(loc, R, r, m):
    bpy.ops.mesh.primitive_torus_add(major_radius=R, minor_radius=r, location=loc, major_segments=128, minor_segments=12)
    return finish(bpy.context.active_object, m)

def disc(loc, r, m, parent=None):
    bpy.ops.mesh.primitive_circle_add(vertices=96, radius=r, fill_type="NGON", location=loc)
    o = bpy.context.active_object
    o.data.materials.append(m)
    return o

def plane(loc, w, d, m, parent=None):
    bpy.ops.mesh.primitive_plane_add(size=1, location=loc)
    o = bpy.context.active_object
    o.scale = (w, d, 1)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if parent:
        o.parent = parent
        o.location = loc
    o.data.materials.append(m)
    return o

def label(txt, loc, size, m=None, align="CENTER", rot_z=0.0, parent=None):
    cu = bpy.data.curves.new("lbl", "FONT")
    cu.body = txt
    cu.size = size
    cu.align_x = align
    cu.align_y = "CENTER"
    o = bpy.data.objects.new("lbl", cu)
    col.objects.link(o)
    o.location = loc
    o.rotation_euler = (0, 0, rot_z)
    o.data.materials.append(m or PAINT())
    if parent:
        o.parent = parent
        o.location = loc
    return o

def empty(loc, rot=(0, 0, 0)):
    o = bpy.data.objects.new("e", None)
    col.objects.link(o)
    o.location = loc
    o.rotation_euler = rot
    return o

# ---------------------------------------------------------------- CDJ
PADC = [(1, 0.12, 0.35), (1, 0.4, 0.05), (1, 0.85, 0.1), (0.15, 0.95, 0.35), (0.1, 0.75, 1), (0.15, 0.3, 1), (0.6, 0.2, 1), (1, 0.25, 0.75)]
SLOPE_Y, SLOPE_Z = 0.03, 0.04  # front apron: sloped face like the real player

def prism_body(cx, cy, W, D, H, m):
    """Body with a sloped front apron, built from a side profile extruded along X."""
    prof = [(-D / 2, 0.0), (-D / 2, SLOPE_Z), (-D / 2 + SLOPE_Y, H), (D / 2, H), (D / 2, 0.0)]
    verts = [(cx - W / 2, cy + y, z) for y, z in prof] + [(cx + W / 2, cy + y, z) for y, z in prof]
    n = len(prof)
    faces = [tuple(range(n))[::-1], tuple(range(n, 2 * n))]
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, n + j, n + i))
    me = bpy.data.meshes.new("body")
    me.from_pydata(verts, [], faces)
    me.update()
    o = bpy.data.objects.new("body", me)
    col.objects.link(o)
    b = o.modifiers.new("bevel", "BEVEL")
    b.width, b.segments, b.limit_method, b.harden_normals = 0.004, 4, "ANGLE", True
    o.data.materials.append(m)
    for p in o.data.polygons:
        p.use_smooth = True
    return o

def apron(cx, cy, D, H, x, w, m, txt=None, size=0.008):
    """Place a strip or label on the sloped front face."""
    ang = math.atan2(H - SLOPE_Z, SLOPE_Y)  # slope angle from horizontal
    th = ang
    nrm = (0, -math.sin(th), math.cos(th))
    yc, zc = cy - D / 2 + SLOPE_Y / 2 + nrm[1] * 0.0008, (SLOPE_Z + H) / 2 + nrm[2] * 0.0008
    if txt:
        o = label(txt, (cx + x, yc, zc), size, align="LEFT")
        o.rotation_euler = (th, 0, 0)
        return o
    bpy.ops.mesh.primitive_plane_add(size=1, location=(cx + x, yc, zc))
    o = bpy.context.active_object
    o.scale = (w, 0.006, 1)
    o.rotation_euler = (th, 0, 0)
    o.data.materials.append(m)
    return o

def btn(x, y, z, w, d, led=None, s=4.0):
    box((x, y, z + 0.002), (w, d, 0.004), RUBBER(), 0.0015)
    if led:
        box((x, y + d / 2 - 0.0012, z + 0.0041), (w * 0.7, 0.0012, 0.0004), emissive(f"led{led}{s}", led, s), 0.0)

def cdj(cx, idx):
    W, D, H = 0.329, 0.453, 0.106
    rnd = random.Random(idx)
    prism_body(cx, 0, W, D, H, BODY())
    box((cx, SLOPE_Y / 2 + 0.002, H + 0.0012), (W - 0.008, D - SLOPE_Y - 0.008, 0.0024), TOP(), 0.0012)
    z = H + 0.0024
    BLUE, ORANGE, GREEN, WHITE, RED = (0.1, 0.45, 1), (1, 0.45, 0.05), (0.1, 1, 0.3), (0.9, 0.9, 1), (1, 0.08, 0.05)

    # front apron: blue light bar + model badge
    apron(cx, 0, D, H, 0.06, 0, None, txt="SN-3000", size=0.0085)

    # touchscreen housing, tilted toward the DJ
    e = empty((cx - 0.012, 0.142, z + 0.007), (math.radians(9), 0, 0))
    box((0, 0, 0), (0.252, 0.158, 0.016), SATIN(), 0.003, parent=e)
    box((0, 0, 0.0082), (0.226, 0.136, 0.0008), mat("glassblack", (0, 0, 0), 0.04), 0.0, parent=e)
    plane((0, 0, 0.0088), 0.216, 0.1296, mat(f"screen{idx}", image=f"screen{idx}.png", img_strength=2.2), parent=e)
    for k in range(7):  # small lit buttons along the top of the housing
        box((-0.105 + k * 0.035, 0.074, 0.0085), (0.018, 0.005, 0.002), RUBBER() if k % 3 else emissive("hbtn", WHITE, 0.8), 0.0008, parent=e)

    # source / browse column left of the screen
    for k in range(5):
        btn(cx - 0.153, 0.205 - k * 0.026, z, 0.016, 0.011, WHITE if k == 0 else None, 2.0)
    # rotary selector + buttons right of the screen
    cyl((cx + 0.142, 0.19, z + 0.003), 0.0145, 0.006, DARKMETAL(), 0.001)
    cyl((cx + 0.142, 0.19, z + 0.009), 0.012, 0.012, RUBBER(), 0.002, verts=48)
    for k in range(4):
        btn(cx + 0.142, 0.155 - k * 0.024, z, 0.02, 0.011)

    # hot cue pads under the screen, with their labels strip
    for k in range(8):
        box((cx - 0.105 + k * 0.03, 0.047, z + 0.0026), (0.025, 0.017, 0.005), RUBBER(), 0.0018)
        on = k < 4 + (idx % 3)  # set hot cues glow in their cue colour, like the real pads
        box((cx - 0.105 + k * 0.03, 0.0385, z + 0.0035), (0.02, 0.0016, 0.0016), emissive(f"padled{k}{on}", PADC[k], 3.0 if on else 0.04), 0.0004)
    label("HOT CUE", (cx - 0.105, 0.03, z + 0.0002), 0.0045)

    # loop / beat-jump section on the left
    for r, y in enumerate((0.016, -0.008, -0.032)):
        for c, x in enumerate((-0.156, -0.132)):
            btn(cx + x, y, z, 0.019, 0.013, ORANGE if r == 0 else None, 1.8)
    for x in (-0.156, -0.132):  # track search / search
        cyl((cx + x, -0.062, z + 0.003), 0.0075, 0.006, RUBBER(), 0.0015, verts=40)

    # jog wheel
    jx, jy = cx, -0.076
    cyl((jx, jy, z + 0.0006), 0.114, 0.0012, SLOT(), verts=160)
    torus((jx, jy, z + 0.0016), 0.1115, 0.0018, METAL())
    torus((jx, jy, z + 0.0018), 0.1075, 0.0016, METAL())  # chrome inner lip (the CDJ-3000 has no lit ring here)
    cyl((jx, jy, z + 0.009), 0.104, 0.015, DARKMETAL(), 0.0015, verts=160)
    n = 120
    for k in range(n):  # knurled side
        a = 2 * math.pi * k / n
        o = box((jx + 0.1042 * math.cos(a), jy + 0.1042 * math.sin(a), z + 0.009), (0.0016, 0.004, 0.012), METAL(), 0.0)
        o.rotation_euler = (0, 0, a)
    ring = mat("jogring", (0.55, 0.55, 0.57), 0.28, 1.0, grain=0.05)
    cyl((jx, jy, z + 0.0168), 0.1015, 0.0016, ring, 0.0006, verts=160)
    platter = mat("platter", (0.005, 0.005, 0.006), 0.72, 0.0, grain=0.1)
    cyl((jx, jy, z + 0.0185), 0.097, 0.0024, platter, 0.0009, verts=160)
    torus((jx, jy, z + 0.0197), 0.0455, 0.0016, METAL())
    disc((jx, jy, z + 0.0199), 0.044, mat(f"jog{idx}", image=f"jog{idx}.png", img_strength=2.0, generated=True))

    # CUE + PLAY
    for (yy, c, name, nm) in ((-0.118, ORANGE, "cue", "CUE"), (-0.168, GREEN, "play", "PLAY/PAUSE")):
        bx = cx - 0.143
        # brushed-metal button face inside a full lit ring, like the CDJ-3000
        cyl((bx, yy, z + 0.0015), 0.0185, 0.003, DARKMETAL(), 0.001)
        cyl((bx, yy, z + 0.0035), 0.0150, 0.005, mat("cueface", (0.70, 0.70, 0.72), 0.3, 1.0, grain=0.05), 0.0015)
        torus((bx, yy, z + 0.0055), 0.0167, 0.0014, emissive(name, c, 3.5))
        label(nm, (bx, yy + 0.0235, z + 0.0002), 0.0045)
    label("SEARCH", (cx - 0.144, -0.073, z + 0.0002), 0.004)
    for k, t in enumerate(("SOURCE", "BROWSE", "TAG LIST", "PLAYLIST", "SEARCH")):
        label(t, (cx - 0.153, 0.205 - k * 0.026 - 0.0095, z + 0.0002), 0.0028)
    for k, t in enumerate(("BACK", "TAG TRACK", "MENU", "SHORTCUT")):
        label(t, (cx + 0.142, 0.155 - k * 0.024 - 0.0095, z + 0.0002), 0.0028)
    for (x, y, t) in ((-0.156, 0.026, "IN"), (-0.132, 0.026, "OUT"), (-0.156, 0.002, "4 BEAT"), (-0.132, 0.002, "RELOOP"), (-0.156, -0.022, "BEAT JUMP"), (-0.132, -0.022, "CALL")):
        label(t, (cx + x, y, z + 0.0002), 0.0026)
    label("LOOP", (cx - 0.144, 0.034, z + 0.0002), 0.0032)

    # right side: sync / master, jog adjust, tempo section
    btn(cx + 0.122, 0.016, z, 0.02, 0.012, ORANGE, 1.5)
    btn(cx + 0.148, 0.016, z, 0.02, 0.012, ORANGE, 1.5)
    label("SYNC", (cx + 0.122, 0.03, z + 0.0002), 0.004)
    label("MASTER", (cx + 0.148, 0.03, z + 0.0002), 0.004)
    btn(cx + 0.148, -0.008, z, 0.02, 0.011, WHITE, 1.5)
    btn(cx + 0.148, -0.03, z, 0.02, 0.011)
    fx = cx + 0.148
    box((fx, -0.118, z + 0.0004), (0.006, 0.13, 0.0012), SLOT(), 0.0)
    for k in range(13):
        box((fx - 0.011, -0.178 + k * 0.01, z + 0.0002), (0.004 if k % 3 else 0.007, 0.0007, 0.0003), PAINT(), 0.0)
    fy = -0.118 + rnd.uniform(-0.035, 0.035)
    box((fx, fy, z + 0.009), (0.022, 0.018, 0.016), DARKMETAL(), 0.003)
    box((fx, fy, z + 0.0172), (0.02, 0.0012, 0.0004), PAINT(), 0.0)
    cyl((fx - 0.026, -0.17, z + 0.004), 0.0075, 0.008, METAL(), 0.0015, verts=40)
    label("TEMPO", (fx, -0.047, z + 0.0002), 0.0045)
    # brand + usb
    label("SN DJ", (cx + 0.1, -0.188, z + 0.0002), 0.008)
    box((cx + 0.11, 0.214, z + 0.0004), (0.03, 0.006, 0.001), SLOT(), 0.0)

# ---------------------------------------------------------------- mixer
def knob(x, y, z, cap=None, r=0.0085):
    cyl((x, y, z + 0.0015), r * 1.3, 0.003, DARKMETAL(), 0.0008, verts=48)
    cyl((x, y, z + 0.011), r, 0.016, RUBBER(), 0.0025, verts=48)
    cyl((x, y, z + 0.0192), r * 0.78, 0.0006, cap or DARKMETAL(), 0.0, verts=48)
    a = random.uniform(-2.3, 2.3)
    o = box((x + 0.55 * r * math.sin(a), y + 0.55 * r * math.cos(a), z + 0.0198), (0.0012, r * 0.85, 0.0004), PAINT(), 0.0)
    o.rotation_euler = (0, 0, -a)

def mixer(cx, cy):
    random.seed(7)
    W, D, H = 0.413, 0.386, 0.106
    prism_body(cx, cy, W, D, H, BODY())
    box((cx, cy + SLOPE_Y / 2 + 0.002, H + 0.0012), (W - 0.008, D - SLOPE_Y - 0.008, 0.0024), TOP(), 0.0012)
    apron(cx, cy, D, H, -0.18, 0, None, txt="SN-M4", size=0.009)
    z = H + 0.0024
    ORANGE, BLUE = (1, 0.45, 0.05), (0.1, 0.45, 1)
    # mic / return column
    for k, y in enumerate((0.15, 0.118, 0.086, 0.054)):
        knob(cx - 0.182, cy + y, z, r=0.0068)
    btn(cx - 0.182, cy + 0.02, z, 0.018, 0.011, (1, 0.08, 0.05), 2.0)
    chs = [-0.135, -0.078, -0.021, 0.036]
    levels = [11, 14, 9, 13]
    for i, x in enumerate(chs):
        X = cx + x
        for k in range(3):  # input selector buttons
            box((X - 0.012 + k * 0.012, cy + 0.178, z + 0.0015), (0.009, 0.007, 0.003), emissive("insel", (0.9, 0.9, 1), 1.0) if k == 1 else RUBBER(), 0.001)
        for y in (0.156, 0.126, 0.098, 0.07):
            knob(X, cy + y, z)
        # colour fx knob, larger, with a lit ring
        cyl((X, cy + 0.034, z + 0.001), 0.0135, 0.002, DARKMETAL(), 0.0005, verts=48)
        knob(X, cy + 0.034, z + 0.001, r=0.0105)
        for k in range(2):
            btn(X - 0.008 + k * 0.016, cy + 0.006, z, 0.012, 0.009)
        box((X, cy - 0.016, z + 0.003), (0.022, 0.013, 0.005), emissive(f"cuebtn{i}", ORANGE, 2.0 if i == 1 else 0.08), 0.0016)
        # channel fader
        box((X, cy - 0.088, z + 0.0004), (0.0045, 0.098, 0.0012), SLOT(), 0.0)
        for k in range(9):
            box((X + 0.011, cy - 0.132 + k * 0.011, z + 0.0002), (0.004, 0.0007, 0.0003), PAINT(), 0.0)
        fy = cy - 0.088 + [0.036, 0.042, -0.01, 0.03][i]
        box((X, fy, z + 0.009), (0.017, 0.026, 0.016), DARKMETAL(), 0.003)
        box((X, fy, z + 0.0172), (0.015, 0.0012, 0.0004), PAINT(), 0.0)
        # level meter
        mx = X + 0.0255
        for k in range(16):
            c = (0.1, 1, 0.3) if k < 11 else ((1, 0.6, 0.05) if k < 15 else (1, 0.08, 0.05))
            on = k < levels[i]
            box((mx, cy + 0.03 + k * 0.0082, z + 0.0008), (0.005, 0.0045, 0.0014), emissive(f"led{c}{on}", c, 6.0 if on else 0.05), 0.0004)
        label(f"{i + 1}", (X, cy + 0.192, z + 0.0002), 0.0065)
    for t, y in (("TRIM", 0.156), ("HI", 0.126), ("MID", 0.098), ("LOW", 0.07), ("COLOR", 0.034), ("CUE", -0.016)):
        label(t, (cx - 0.158, cy + y, z + 0.0002), 0.0028)
    # beat fx section on the right
    e = empty((cx + 0.14, cy + 0.158, z + 0.004), (math.radians(8), 0, 0))
    box((0, 0, 0), (0.104, 0.054, 0.008), SATIN(), 0.002, parent=e)
    plane((0, 0, 0.0043), 0.092, 0.042, mat("mixscreen", image="mixer.png", img_strength=1.8), parent=e)
    for r in range(2):
        for c in range(4):
            btn(cx + 0.1 + c * 0.026, cy + 0.11 - r * 0.02, z, 0.018, 0.011, (0.9, 0.9, 1) if (r, c) == (0, 1) else None, 2.0)
    cyl((cx + 0.115, cy + 0.052, z + 0.002), 0.017, 0.004, DARKMETAL(), 0.001)
    knob(cx + 0.115, cy + 0.052, z + 0.002, r=0.0135)
    box((cx + 0.172, cy + 0.052, z + 0.004), (0.03, 0.022, 0.007), emissive("fxon", (1, 0.1, 0.08), 1.5), 0.003)
    label("FX ON", (cx + 0.172, cy + 0.072, z + 0.0002), 0.0045)
    for x in (0.105, 0.145, 0.185):
        knob(cx + x, cy + 0.0, z, r=0.0078)
    for k in range(10):  # master meter
        c = (0.1, 1, 0.3) if k < 7 else (1, 0.6, 0.05)
        for s in (-1, 1):
            box((cx + 0.145 + s * 0.006, cy - 0.04 + k * 0.007, z + 0.0008), (0.0045, 0.004, 0.0014), emissive(f"mm{c}{k < 8}", c, 6.0 if k < 8 else 0.05), 0.0004)
    # front: crossfader + headphone section
    box((cx - 0.05, cy - 0.158, z + 0.0004), (0.11, 0.0045, 0.0012), SLOT(), 0.0)
    box((cx - 0.044, cy - 0.158, z + 0.009), (0.026, 0.017, 0.016), DARKMETAL(), 0.003)
    for x in (0.105, 0.145, 0.185):
        knob(cx + x, cy - 0.13, z, r=0.0072)
    for c in range(3):
        btn(cx + 0.105 + c * 0.04, cy - 0.165, z, 0.02, 0.01, ORANGE if c == 0 else None, 2.5)
    for x in (-0.182,):
        knob(cx + x, cy - 0.14, z, r=0.007)

# ---------------------------------------------------------------- scene
CW, MW = 0.329, 0.413
g = 0.012
xs_in = MW / 2 + g + CW / 2
xs_out = xs_in + CW + g
for i, x in enumerate([-xs_out, -xs_in, xs_in, xs_out]):
    cdj(x, i)
mixer(0, -0.2265 + 0.193)

# booth table, a little glossy so the glows reflect
box((0, 0.6, -0.03), (3.2, 2.0, 0.06), mat("table", (0.012, 0.012, 0.013), 0.5, 0.0, grain=0.1), 0.004)
box((0, -0.47, -0.25), (2.6, 0.06, 0.5), mat("tablefront", (0.008, 0.008, 0.009), 0.6), 0.004)
# back wall
box((0, 3.2, 1.5), (14, 0.1, 6), mat("wall", (0.02, 0.02, 0.021), 0.85), 0)

def area(name, loc, rot, size, energy, color, sx=None):
    ld = bpy.data.lights.new(name, "AREA")
    ld.energy = energy
    ld.color = color
    if sx:
        ld.shape = "RECTANGLE"
        ld.size, ld.size_y = sx
    else:
        ld.size = size
    o = bpy.data.objects.new(name, ld)
    col.objects.link(o)
    o.location = loc
    o.rotation_euler = rot
    return o

# big overhead softbox slightly behind, so tops get a soft sheen without washing out
# neutral studio lighting: every light is plain white, no warm or cool tint
WHITE_LIGHT = (1, 1, 1)
area("key", (0, 0.55, 1.35), (math.radians(-22), 0, 0), 0, 26, WHITE_LIGHT, sx=(2.6, 0.9))
# thin strip lights behind for crisp edge highlights
area("stripL", (-1.3, 1.2, 0.55), (math.radians(-75), math.radians(-40), 0), 0, 35, WHITE_LIGHT, sx=(1.4, 0.08))
area("stripR", (1.3, 1.2, 0.55), (math.radians(-75), math.radians(40), 0), 0, 35, WHITE_LIGHT, sx=(1.4, 0.08))
# soft front fill
area("fill", (0, -2.2, 1.0), (math.radians(65), 0, 0), 3.0, 6, WHITE_LIGHT)
# gentle gradient on the back wall
area("wallwash", (0, 2.6, 2.2), (math.radians(-150), 0, 0), 3.0, 9, WHITE_LIGHT)

w = bpy.data.worlds.new("w")
w.use_nodes = True
w.node_tree.nodes["Background"].inputs["Color"].default_value = (0.002, 0.002, 0.002, 1)
sc.world = w

# camera
cams = {
    "hero": ((-1.12, -0.98, 0.80), (0.10, 0.08, 0.02), 35, 4.0),
    "close": ((-0.95, -0.62, 0.42), (-0.30, -0.05, 0.10), 50, 2.2),
    "dj": ((-0.02, -0.78, 0.72), (0.0, -0.02, 0.09), 28, 3.2),
}
cl, tgt, lens, fstop = cams[shot]
cd = bpy.data.cameras.new("cam")
cd.lens = lens
cd.dof.use_dof = True
cd.dof.aperture_fstop = fstop
cam = bpy.data.objects.new("cam", cd)
col.objects.link(cam)
cam.location = cl
t = empty(tgt)
c = cam.constraints.new("TRACK_TO")
c.target = t
c.track_axis = "TRACK_NEGATIVE_Z"
c.up_axis = "UP_Y"
cd.dof.focus_object = t
sc.camera = cam

r = sc.render
r.engine = "CYCLES"
sc.cycles.device = "CPU"
sc.cycles.samples = samples
sc.cycles.use_denoising = True
sc.cycles.max_bounces = 6
r.resolution_x, r.resolution_y = 1920, 1080
r.resolution_percentage = pct
r.filepath = out
try:
    sc.view_settings.view_transform = "AgX"
    sc.view_settings.look = "AgX - Base Contrast"
except Exception as ex:
    print("look", ex)
if not LIVE:
    bpy.ops.render.render(write_still=True)
    print("rendered", out)
