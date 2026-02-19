const canvas = document.getElementById("galaxy");
const ctx = canvas.getContext("2d");

let w, h;
function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
}
window.addEventListener("resize", resize);
resize();

/* ⭐ STAR CONFIG */
const STAR_COUNT = 600;
const stars = [];

for (let i = 0; i < STAR_COUNT; i++) {
    stars.push({
        x: Math.random() * w,
        y: Math.random() * h,
        z: Math.random(),
        size: Math.random() * 1.5 + 0.5,
        speed: Math.random() * 0.4 + 0.1
    });
}

/* 🚀 ROCKET PARTICLES */
const rockets = [];
for (let i = 0; i < 6; i++) {
    rockets.push({
        x: Math.random() * w,
        y: Math.random() * h,
        speed: Math.random() * 0.2 + 0.05,
        size: Math.random() * 2 + 1
    });
}

function draw() {
    ctx.clearRect(0, 0, w, h);

    /* 🌌 BACKGROUND GLOW */
    const gradient = ctx.createRadialGradient(
        w / 2, h / 2, 100,
        w / 2, h / 2, w
    );
    gradient.addColorStop(0, "#020617");
    gradient.addColorStop(1, "#000");
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, w, h);

    /* ⭐ STARS */
    stars.forEach(s => {
        ctx.globalAlpha = 0.3 + s.z;
        ctx.fillStyle = "white";
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
        ctx.fill();

        s.y -= s.speed;
        if (s.y < 0) {
            s.y = h;
            s.x = Math.random() * w;
        }
    });

    /* 🚀 ROCKET STREAKS */
    rockets.forEach(r => {
        ctx.globalAlpha = 0.6;
        ctx.strokeStyle = "#7c7cff";
        ctx.lineWidth = r.size;

        ctx.beginPath();
        ctx.moveTo(r.x, r.y);
        ctx.lineTo(r.x + 40, r.y - 80);
        ctx.stroke();

        r.y -= r.speed * 20;
        r.x += r.speed * 5;

        if (r.y < -100 || r.x > w + 100) {
            r.y = h + Math.random() * 200;
            r.x = Math.random() * w;
        }
    });

    requestAnimationFrame(draw);
}

draw();
