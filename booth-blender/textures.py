"""Generate screen textures for the booth test render (CDJ touchscreens, jog displays, mixer screen)."""
import math, random, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = os.path.join(os.path.dirname(__file__), "tex")
os.makedirs(OUT, exist_ok=True)

def font(size, bold=False):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

TRACKS = [
    ("Voice Agent QA", "Shaurya Nigam", "126.00", "-04:10.2", (61, 169, 255)),
    ("F1 Strategy Optimizer", "Shaurya Nigam", "128.00", "-03:22.4", (255, 138, 31)),
    ("CivicFix", "Shaurya Nigam", "124.00", "-05:01.7", (51, 209, 122)),
    ("TerraLens", "Shaurya Nigam", "122.00", "-06:15.0", (200, 90, 255)),
]

def screen(i):
    title, artist, bpm, t, accent = TRACKS[i]
    W, H = 1600, 960
    im = Image.new("RGB", (W, H), (6, 7, 10))
    d = ImageDraw.Draw(im)
    rnd = random.Random(i + 3)
    # header bar
    d.rectangle([0, 0, W, 120], fill=(16, 18, 24))
    d.rectangle([24, 20, 104, 100], fill=(40, 44, 54))
    d.text((130, 18), title, font=font(46, True), fill=(240, 240, 245))
    d.text((130, 72), artist, font=font(30), fill=(150, 152, 160))
    d.text((W - 380, 14), bpm, font=font(64, True), fill=(240, 240, 245))
    d.text((W - 130, 44), "BPM", font=font(28), fill=(150, 152, 160))
    d.text((W - 380, 84), "+0.00%  KEY 8A", font=font(24), fill=(120, 200, 255))
    # big zoomed waveform, 3 band
    cy, amp = 420, 230
    for x in range(0, W, 2):
        ph = x / W * 14 + i
        e = 0.35 + 0.65 * abs(math.sin(ph * 0.9)) * (0.6 + 0.4 * rnd.random())
        if (x // 120) % 8 == 7:
            e *= 0.35
        lo = amp * e
        mid = lo * (0.55 + 0.2 * rnd.random())
        hi = lo * (0.25 + 0.15 * rnd.random())
        d.line([x, cy - lo, x, cy + lo], fill=(200, 20, 90), width=2)
        d.line([x, cy - mid, x, cy + mid], fill=(255, 70, 150), width=2)
        d.line([x, cy - hi, x, cy + hi], fill=(255, 225, 240), width=2)
    # beat grid + playhead
    for x in range(40, W, 100):
        d.line([x, 170, x, 190], fill=(90, 90, 100), width=3)
    d.line([W // 2, 160, W // 2, 680], fill=(255, 60, 60), width=5)
    # hot cue markers
    cols = [(255, 60, 120), (255, 140, 30), (255, 220, 40), (60, 220, 120), (40, 200, 255), (60, 110, 255), (170, 80, 255), (255, 90, 200)]
    for k in range(5):
        x = 140 + k * 300
        d.polygon([(x, 690), (x + 30, 690), (x + 15, 712)], fill=cols[k])
    # overview strip
    oy = 800
    d.rectangle([0, 730, W, 960], fill=(12, 13, 17))
    for x in range(40, W - 40, 3):
        e = 0.3 + 0.7 * abs(math.sin(x / 90 + i)) * (0.5 + 0.5 * rnd.random())
        c = (90, 60, 80) if x < W * 0.38 else (235, 90, 160)
        d.line([x, oy - 50 * e, x, oy + 50 * e], fill=c)
    d.line([int(W * 0.38), 740, int(W * 0.38), 860], fill=(255, 60, 60), width=4)
    d.text((40, 880), "REMAIN", font=font(26), fill=(150, 152, 160))
    d.text((170, 866), t, font=font(48, True), fill=(240, 240, 245))
    d.text((W - 480, 880), "MASTER   SYNC   Q", font=font(28, True), fill=(90, 160, 255))
    im = im.filter(ImageFilter.GaussianBlur(0.6))
    im.save(f"{OUT}/screen{i}.png")

def jog(i):
    _, _, _, _, accent = TRACKS[i]
    S = 800
    im = Image.new("RGB", (S, S), (0, 0, 0))
    d = ImageDraw.Draw(im)
    c = S // 2
    d.ellipse([20, 20, S - 20, S - 20], fill=(8, 9, 12))
    # progress ring
    d.arc([60, 60, S - 60, S - 60], -90, -90 + 360 * (0.38 + 0.1 * i), fill=(230, 235, 245), width=30)
    d.arc([60, 60, S - 60, S - 60], -90 + 360 * (0.38 + 0.1 * i), 270, fill=(40, 42, 50), width=34)
    # artwork square
    d.rounded_rectangle([c - 150, c - 190, c + 150, c + 110], 24, fill=(28, 30, 38))
    for k in range(6):
        r = 30 + k * 22
        d.ellipse([c - r, c - 40 - r, c + r, c - 40 + r], outline=(70, 130, 230), width=3)
    d.text((c - 120, c + 140), "-0" + str(3 + i) + ":1" + str(i) + ".2", font=font(64, True), fill=(240, 240, 245))
    # marker
    d.line([c, 70, c, 140], fill=(255, 255, 255), width=10)
    im.save(f"{OUT}/jog{i}.png")

def mixer_screen():
    W, H = 900, 360
    im = Image.new("RGB", (W, H), (6, 7, 10))
    d = ImageDraw.Draw(im)
    d.text((30, 24), "BEAT FX", font=font(40, True), fill=(240, 240, 245))
    d.text((30, 90), "ECHO   1/2   CH2", font=font(34), fill=(120, 180, 255))
    d.text((W - 300, 24), "128.0", font=font(64, True), fill=(240, 240, 245))
    for k in range(16):
        h = 30 + (k * 37 % 90)
        d.rectangle([30 + k * 52, 300 - h, 66 + k * 52, 300], fill=(60, 130, 255) if k % 4 else (230, 235, 245))
    im.save(f"{OUT}/mixer.png")

for i in range(4):
    screen(i); jog(i)
mixer_screen()
print("ok")
