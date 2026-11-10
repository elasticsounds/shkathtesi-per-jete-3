  // Colouring: tap-to-fill on a line drawing. Fills are stored as [x, y, colour] and replayed on load.
  var canvas = document.getElementById('paint-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d', { willReadFrequently: true });
  var cursor = document.getElementById('paint-cursor');
  var status = document.getElementById('paint-status');
  var KEY = 'pg016_sec001_paint';
  var fills = [];
  try { fills = JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { fills = []; }
  var W = 0, H = 0, base = null, wall = null, cx = 0, cy = 0;
  var img = new Image();
  img.onload = function () {
    W = canvas.width = img.naturalWidth; H = canvas.height = img.naturalHeight;
    ctx.drawImage(img, 0, 0);
    base = ctx.getImageData(0, 0, W, H);
    wall = new Uint8Array(W * H);
    for (var i = 0; i < W * H; i++) {
      var d = base.data, o = i * 4;
      wall[i] = (0.299 * d[o] + 0.587 * d[o + 1] + 0.114 * d[o + 2]) < 200 ? 1 : 0;
    }
    cx = Math.round(W / 2); cy = Math.round(H / 2);
    redraw(); placeCursor();
  };
  img.src = SRC;
  function rgb(hex) { return [parseInt(hex.slice(1, 3), 16), parseInt(hex.slice(3, 5), 16), parseInt(hex.slice(5, 7), 16)]; }
  function fill(data, x, y, hex) {
    if (x < 0 || y < 0 || x >= W || y >= H || wall[y * W + x]) return false;
    var c = rgb(hex), seen = new Uint8Array(W * H), stack = [y * W + x], b = base.data;
    while (stack.length) {
      var p = stack.pop();
      if (seen[p] || wall[p]) continue;
      seen[p] = 1;
      var o = p * 4;
      data[o] = b[o] * c[0] / 255; data[o + 1] = b[o + 1] * c[1] / 255; data[o + 2] = b[o + 2] * c[2] / 255;
      var px = p % W;
      if (px > 0) stack.push(p - 1);
      if (px < W - 1) stack.push(p + 1);
      if (p >= W) stack.push(p - W);
      if (p < W * (H - 1)) stack.push(p + W);
    }
    // tint the line pixels that border the filled area (two rings), so no pale halo is left along the lines
    for (var pass = 0; pass < 2; pass++) {
      var ring = [];
      for (var q = 0; q < W * H; q++) {
        if (!wall[q] || seen[q]) continue;
        var qx = q % W;
        if ((qx > 0 && seen[q - 1]) || (qx < W - 1 && seen[q + 1]) || (q >= W && seen[q - W]) || (q < W * (H - 1) && seen[q + W])) ring.push(q);
      }
      for (var k = 0; k < ring.length; k++) {
        var o2 = ring[k] * 4;
        seen[ring[k]] = 1;
        data[o2] = b[o2] * c[0] / 255; data[o2 + 1] = b[o2 + 1] * c[1] / 255; data[o2 + 2] = b[o2 + 2] * c[2] / 255;
      }
    }
    return true;
  }
  function redraw() {
    var out = new ImageData(new Uint8ClampedArray(base.data), W, H);
    fills.forEach(function (f) { fill(out.data, f[0], f[1], f[2]); });
    ctx.putImageData(out, 0, 0);
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(fills)); } catch (e) {} }
  function colour() { var r = document.querySelector('input[name="paint"]:checked'); return r ? r.value : '#ef4444'; }
  function colourName() { var r = document.querySelector('input[name="paint"]:checked'); return r ? r.parentNode.textContent.trim() : ''; }
  function paintAt(x, y) {
    if (!base) return;
    if (wall[y * W + x]) { // on a line: look for the nearest paintable pixel
      var found = false;
      for (var r = 1; r <= 4 && !found; r++) {
        for (var dy = -r; dy <= r && !found; dy++) for (var dx = -r; dx <= r && !found; dx++) {
          var nx = x + dx, ny = y + dy;
          if (nx >= 0 && ny >= 0 && nx < W && ny < H && !wall[ny * W + nx]) { x = nx; y = ny; found = true; }
        }
      }
      if (!found) return;
    }
    fills.push([x, y, colour()]);
    if (fills.length > 300) fills.shift();
    redraw(); save();
    if (status) status.textContent = colourName();
  }
  function placeCursor() {
    if (!cursor || !W) return;
    cursor.style.left = (cx / W * 100) + '%'; cursor.style.top = (cy / H * 100) + '%';
  }
  canvas.addEventListener('click', function (e) {
    var r = canvas.getBoundingClientRect();
    cx = Math.max(0, Math.min(W - 1, Math.round((e.clientX - r.left) / r.width * W)));
    cy = Math.max(0, Math.min(H - 1, Math.round((e.clientY - r.top) / r.height * H)));
    placeCursor(); paintAt(cx, cy);
  });
  canvas.addEventListener('keydown', function (e) {
    var step = e.shiftKey ? 40 : 12, k = e.key;
    if (k === 'ArrowLeft') cx = Math.max(0, cx - step);
    else if (k === 'ArrowRight') cx = Math.min(W - 1, cx + step);
    else if (k === 'ArrowUp') cy = Math.max(0, cy - step);
    else if (k === 'ArrowDown') cy = Math.min(H - 1, cy + step);
    else if (k === 'Enter' || k === ' ') { e.preventDefault(); e.stopPropagation(); paintAt(cx, cy); return; }
    else return;
    // the reader uses the arrow keys to turn pages; keep them for the colouring cursor while the picture has focus
    e.preventDefault(); e.stopPropagation(); placeCursor();
  });
  document.getElementById('paint-undo').addEventListener('click', function () { fills.pop(); redraw(); save(); });
  document.getElementById('paint-clear').addEventListener('click', function () { fills = []; redraw(); save(); });
