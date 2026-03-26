from flask import Flask, render_template_string, request, redirect, url_for, session, jsonify
import requests

app = Flask(__name__)
app.secret_key = "clave_secreta_2026"

USUARIO = "admin"
CONTRASENA = "admin2026"

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Login — Interfaz Animada</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root{
            --bg1:#0f172a; --bg2:#0b1220; --accent:#7c3aed;
            --purple: rgb(232,121,249);
            --blue: rgb(96,165,250);
            --green: rgb(94,234,212);
        }
        html,body{height:100%;margin:0;font-family:Inter,system-ui,Arial;background:linear-gradient(135deg,var(--bg1),var(--bg2));color:#e6eef8;overflow:hidden}
        .scene{position:fixed;inset:0;overflow:hidden}
        .gradient{position:absolute;inset:-20%;-webkit-filter:blur(80px);filter:blur(80px);opacity:.5;background:radial-gradient(circle at 20% 30%, rgba(124,58,237,.35), transparent 15%), radial-gradient(circle at 80% 70%, rgba(14,165,233,.18), transparent 18%)}
        canvas.particles{position:absolute;inset:0;pointer-events:none}
        .rainbow-wrap{position:absolute;inset:0;overflow:hidden;pointer-events:none}
        .rainbow{height:100vh;width:0;top:0;position:absolute;transform:rotate(10deg);transform-origin:top right;right:-25vw}
        @keyframes slide{from{right:-25vw;}to{right:125vw;}}
        /* generate 25 stripes with varying colors/delays */
        /* pattern of colors cycles every 6 to mimic random */
        .rainbow:nth-child(1){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--blue),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*1) linear infinite slide;animation-delay: calc(-1/25*45s)}
        .rainbow:nth-child(2){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--green),50px 0 50px 25px var(--blue),130px 0 80px 40px white;animation: calc(45s - 0.9s*2) linear infinite slide;animation-delay: calc(-2/25*45s)}
        .rainbow:nth-child(3){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--green),0 0 50px 25px var(--purple),50px 0 50px 25px var(--blue),130px 0 80px 40px white;animation: calc(45s - 0.9s*3) linear infinite slide;animation-delay: calc(-3/25*45s)}
        .rainbow:nth-child(4){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--green),0 0 50px 25px var(--blue),50px 0 50px 25px var(--purple),130px 0 80px 40px white;animation: calc(45s - 0.9s*4) linear infinite slide;animation-delay: calc(-4/25*45s)}
        .rainbow:nth-child(5){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--blue),0 0 50px 25px var(--green),50px 0 50px 25px var(--purple),130px 0 80px 40px white;animation: calc(45s - 0.9s*5) linear infinite slide;animation-delay: calc(-5/25*45s)}
        .rainbow:nth-child(6){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--blue),0 0 50px 25px var(--purple),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*6) linear infinite slide;animation-delay: calc(-6/25*45s)}
        .rainbow:nth-child(7){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--blue),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*7) linear infinite slide;animation-delay: calc(-7/25*45s)}
        .rainbow:nth-child(8){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--green),50px 0 50px 25px var(--blue),130px 0 80px 40px white;animation: calc(45s - 0.9s*8) linear infinite slide;animation-delay: calc(-8/25*45s)}
        .rainbow:nth-child(9){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--green),0 0 50px 25px var(--purple),50px 0 50px 25px var(--blue),130px 0 80px 40px white;animation: calc(45s - 0.9s*9) linear infinite slide;animation-delay: calc(-9/25*45s)}
        .rainbow:nth-child(10){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--green),0 0 50px 25px var(--blue),50px 0 50px 25px var(--purple),130px 0 80px 40px white;animation: calc(45s - 0.9s*10) linear infinite slide;animation-delay: calc(-10/25*45s)}
        .rainbow:nth-child(11){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--blue),0 0 50px 25px var(--green),50px 0 50px 25px var(--purple),130px 0 80px 40px white;animation: calc(45s - 0.9s*11) linear infinite slide;animation-delay: calc(-11/25*45s)}
        .rainbow:nth-child(12){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--blue),0 0 50px 25px var(--purple),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*12) linear infinite slide;animation-delay: calc(-12/25*45s)}
        .rainbow:nth-child(13){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--blue),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*13) linear infinite slide;animation-delay: calc(-13/25*45s)}
        .rainbow:nth-child(14){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--green),50px 0 50px 25px var(--blue),130px 0 80px 40px white;animation: calc(45s - 0.9s*14) linear infinite slide;animation-delay: calc(-14/25*45s)}
        .rainbow:nth-child(15){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--green),0 0 50px 25px var(--purple),50px 0 50px 25px var(--blue),130px 0 80px 40px white;animation: calc(45s - 0.9s*15) linear infinite slide;animation-delay: calc(-15/25*45s)}
        .rainbow:nth-child(16){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--green),0 0 50px 25px var(--blue),50px 0 50px 25px var(--purple),130px 0 80px 40px white;animation: calc(45s - 0.9s*16) linear infinite slide;animation-delay: calc(-16/25*45s)}
        .rainbow:nth-child(17){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--blue),0 0 50px 25px var(--green),50px 0 50px 25px var(--purple),130px 0 80px 40px white;animation: calc(45s - 0.9s*17) linear infinite slide;animation-delay: calc(-17/25*45s)}
        .rainbow:nth-child(18){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--blue),0 0 50px 25px var(--purple),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*18) linear infinite slide;animation-delay: calc(-18/25*45s)}
        .rainbow:nth-child(19){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--blue),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*19) linear infinite slide;animation-delay: calc(-19/25*45s)}
        .rainbow:nth-child(20){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--green),50px 0 50px 25px var(--blue),130px 0 80px 40px white;animation: calc(45s - 0.9s*20) linear infinite slide;animation-delay: calc(-20/25*45s)}
        .rainbow:nth-child(21){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--green),0 0 50px 25px var(--purple),50px 0 50px 25px var(--blue),130px 0 80px 40px white;animation: calc(45s - 0.9s*21) linear infinite slide;animation-delay: calc(-21/25*45s)}
        .rainbow:nth-child(22){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--green),0 0 50px 25px var(--blue),50px 0 50px 25px var(--purple),130px 0 80px 40px white;animation: calc(45s - 0.9s*22) linear infinite slide;animation-delay: calc(-22/25*45s)}
        .rainbow:nth-child(23){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--blue),0 0 50px 25px var(--green),50px 0 50px 25px var(--purple),130px 0 80px 40px white;animation: calc(45s - 0.9s*23) linear infinite slide;animation-delay: calc(-23/25*45s)}
        .rainbow:nth-child(24){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--blue),0 0 50px 25px var(--purple),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*24) linear infinite slide;animation-delay: calc(-24/25*45s)}
        .rainbow:nth-child(25){box-shadow:-130px 0 80px 40px white,-50px 0 50px 25px var(--purple),0 0 50px 25px var(--blue),50px 0 50px 25px var(--green),130px 0 80px 40px white;animation: calc(45s - 0.9s*25) linear infinite slide;animation-delay: calc(-25/25*45s)}
        .center{position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px}
        .card{width:420px;background:linear-gradient(180deg,rgba(255,255,255,0.04),rgba(255,255,255,0.02));backdrop-filter: blur(6px);border-radius:16px;padding:28px;box-shadow:0 10px 40px rgba(2,6,23,.6);transform:translateY(20px);opacity:0;animation:enter .8s ease-out .12s forwards}
        @keyframes enter{to{transform:none;opacity:1}}
        h1{margin:0 0 10px;font-size:20px;letter-spacing:-0.5px}
        p.lead{margin:0 0 18px;color:rgba(230,238,248,.85)}
        label{display:block;margin:10px 0 6px;color:rgba(230,238,248,.8);font-weight:600}
        input{width:100%;padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.06);background:transparent;color:inherit;box-sizing:border-box}
        input:focus{outline:none;box-shadow:0 4px 18px rgba(124,58,237,.12);border-color:rgba(124,58,237,.5)}
        .btn{display:inline-block;width:100%;padding:12px;border-radius:10px;border:none;background:linear-gradient(90deg,var(--accent),#06b6d4);color:white;font-weight:700;cursor:pointer;margin-top:14px}
        .meta{display:flex;justify-content:space-between;align-items:center;margin-top:12px;color:rgba(230,238,248,.6)}
        .error{margin-top:12px;color:#fb7185;text-align:center}
        .small{font-size:13px;color:rgba(230,238,248,.6)}
        .logo{display:flex;gap:10px;align-items:center;margin-bottom:12px}
        .logo .dot{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#7c3aed,#06b6d4);display:flex;align-items:center;justify-content:center;font-weight:800}
        a.logout{color:#fee2e2;text-decoration:none;padding:8px 12px;border-radius:8px;background:rgba(255,255,255,0.03)}
    </style>
</head>
<body>
    <div class="scene">
        <div class="gradient"></div>
        <canvas class="particles" id="particles"></canvas>
        <div class="rainbow-wrap">
            {% for i in range(25) %}
                <div class="rainbow"></div>
            {% endfor %}
        </div>
    </div>
    <div class="center">
        {% if session.get('autenticado') %}
            <div class="card">
                <div class="logo"><div class="dot">A</div><div><strong>Admin</strong><div class="small">Panel seguro</div></div></div>
                <h1>Bienvenido, administrador</h1>
                <p class="lead">Tienes acceso al dashboard con animaciones y métricas en tiempo real.</p>
                <div class="meta"><span class="small">Usuario: admin</span><a class="logout" href="{{ url_for('logout') }}">Cerrar sesión</a></div>
            </div>
        {% else %}
            <form class="card" method="post" onsubmit="return handleSubmit(this)">
                <div class="logo"><div class="dot">I</div><div><strong>Interfaz</strong><div class="small">versión animada</div></div></div>
                <h1>Iniciar sesión</h1>
                <p class="lead">Accede para ver el dashboard con gráficas y animaciones.</p>
                <label>Usuario</label>
                <input type="text" name="usuario" required autocomplete="username">
                <label>Contraseña</label>
                <input type="password" name="contrasena" required autocomplete="current-password">
                <button class="btn" type="submit">Ingresar</button>
                {% if error %}
                    <div class="error">{{ error }}</div>
                {% endif %}
                <div class="meta"><span class="small">Demo: admin / admin2026</span></div>
            </form>
        {% endif %}
    </div>

    <script>
        // simple particle background
        const canvas = document.getElementById('particles');
        const ctx = canvas.getContext('2d');
        let w = canvas.width = innerWidth; let h = canvas.height = innerHeight;
        window.addEventListener('resize', ()=>{w=canvas.width=innerWidth;h=canvas.height=innerHeight;});
        const particles=[]; for(let i=0;i<80;i++){particles.push({x:Math.random()*w,y:Math.random()*h,r:Math.random()*1.6+0.4,dx:(Math.random()-0.5)*0.4,dy:(Math.random()-0.5)*0.4})}
        function loop(){ctx.clearRect(0,0,w,h);for(const p of particles){p.x+=p.dx;p.y+=p.dy; if(p.x<0)p.x=w; if(p.x>w)p.x=0; if(p.y<0)p.y=h; if(p.y>h)p.y=0; ctx.beginPath();ctx.fillStyle='rgba(255,255,255,0.06)';ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill()}requestAnimationFrame(loop)}loop();

        // subtle submit animation
        function handleSubmit(form){const btn=form.querySelector('.btn');btn.disabled=true;btn.style.transform='translateY(2px) scale(.998)';return true}
    </script>
</body>
</html>
"""

DASHBOARD_HTML = """
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Dashboard — Ejercicios</title>
    <style>
        :root{
            --bg:#f6f7fb;
            --card:#ffffff;
            --accent:#0a84ff;
            --text:#0f172a;
            --muted:#6b7280;
            --shadow:0 18px 40px rgba(15,23,42,0.12);
        }
        html,body{height:100%;margin:0;font-family:-apple-system, "SF Pro Display", "SF Pro Text", Inter, system-ui;background:var(--bg);color:var(--text);overflow-x:hidden}
        /* cinematica ligera con blobs interactivos */
        .cinema{position:fixed;inset:0;z-index:-2;overflow:hidden;pointer-events:none}
        .blob{position:absolute;filter:blur(60px);border-radius:50%;opacity:.45;mix-blend-mode:multiply;transition:transform .5s ease}
        .b1{width:520px;height:520px;left:-120px;top:-80px;background:linear-gradient(135deg,#7dd3fc,#c4b5fd)}
        .b2{width:480px;height:480px;right:-140px;top:40px;background:linear-gradient(135deg,#93c5fd,#a5f3fc)}
        .b3{width:380px;height:380px;left:30%;bottom:-160px;background:linear-gradient(135deg,#f9a8d4,#c7d2fe)}
        .spinner{position:absolute;inset:0;display:grid;place-items:center;z-index:-1;opacity:0.55}
        .spinner .ring{width:260px;height:260px;border:2px solid rgba(10,132,255,0.35);border-radius:50%;animation:spin 18s linear infinite}

        header{position:relative;z-index:2;padding:28px 32px 12px;display:flex;justify-content:space-between;align-items:center}
        .brand{font-weight:800;font-size:18px;letter-spacing:-0.3px;color:var(--text)}
        .chip{padding:8px 12px;border-radius:999px;background:rgba(10,132,255,0.12);color:var(--accent);font-weight:600;border:1px solid rgba(10,132,255,0.2)}
        .logout-chip{display:inline-flex;align-items:center;gap:10px;padding:10px 12px;border-radius:999px;background:rgba(255,255,255,0.22);color:var(--text);font-weight:800;border:1px solid rgba(15,23,42,0.12);text-decoration:none;box-shadow:0 10px 22px rgba(15,23,42,0.12);transition:padding .2s ease, gap .2s ease, box-shadow .2s ease}
        .logout-icon{display:grid;place-items:center;width:36px;height:36px;border-radius:999px;background:linear-gradient(135deg,#ff6b6b,#f97316);color:white;font-size:18px;font-weight:900;animation:wiggle 1.2s ease-in-out infinite}
        .logout-label{max-width:0;overflow:hidden;white-space:nowrap;opacity:0;transition:max-width .2s ease, opacity .2s ease}
        .logout-chip:hover{padding:10px 16px;gap:12px;box-shadow:0 16px 32px rgba(15,23,42,0.18)}
        .logout-chip:hover .logout-label{max-width:140px;opacity:1}
        @keyframes wiggle{0%{transform:rotate(0deg);}25%{transform:rotate(6deg);}50%{transform:rotate(-6deg);}75%{transform:rotate(6deg);}100%{transform:rotate(0deg);}}

        .hero{position:relative;z-index:2;padding:12px 32px 4px;display:grid;grid-template-columns:1.2fr 1fr;gap:24px;align-items:center}
        .hero h1{margin:0;font-size:36px;letter-spacing:-0.8px}
        .hero p{margin:12px 0 18px;color:var(--muted);font-size:16px;line-height:1.6}
        .cta{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(120deg,#0a84ff,#34d399);color:white;padding:12px 16px;border-radius:14px;border:none;font-weight:700;cursor:pointer;box-shadow:0 10px 26px rgba(10,132,255,0.35)}
        .hero-visual{position:relative;height:260px;border-radius:22px;overflow:hidden;background:radial-gradient(circle at 30% 30%,rgba(10,132,255,.18),transparent 50%),radial-gradient(circle at 70% 50%,rgba(52,211,153,.14),transparent 60%),var(--card);box-shadow:var(--shadow)}
        .badge{position:absolute;top:24px;right:24px;background:#0a84ff;color:white;padding:10px 14px;border-radius:12px;font-weight:700;box-shadow:0 12px 30px rgba(10,132,255,0.32)}
        .weather-card{position:absolute;inset:20px;display:grid;grid-template-rows:auto auto auto 1fr;gap:10px;padding:16px;border-radius:16px;background:rgba(255,255,255,0.9);backdrop-filter:blur(10px);box-shadow:0 10px 28px rgba(15,23,42,0.12);border:1px solid rgba(15,23,42,0.06)}
        .weather-city{font-weight:800;font-size:18px;color:var(--text)}
        .weather-main{display:flex;align-items:flex-end;gap:10px;font-size:32px;font-weight:900;color:#0a84ff}
        .weather-cond{font-size:16px;font-weight:700;color:var(--text)}
        .weather-meta{display:flex;gap:14px;font-size:13px;color:var(--muted);flex-wrap:wrap}
        .meta-pill{padding:6px 10px;border-radius:10px;background:rgba(10,132,255,0.08);color:var(--text);font-weight:700;border:1px solid rgba(10,132,255,0.12)}
        .forecast{display:grid;grid-template-columns:repeat(auto-fit,minmax(90px,1fr));gap:8px;font-size:13px;color:var(--muted)}
        .forecast-card{border:1px solid rgba(15,23,42,0.06);border-radius:10px;padding:8px 10px;background:rgba(10,132,255,0.05)}
        .forecast-card .temp{font-weight:700;color:var(--text)}
        .forecast-card .prec{font-size:12px;color:var(--accent);font-weight:700}
        @keyframes spin{to{transform:rotate(360deg)}}

        .cards-wrapper{position:relative;z-index:2;padding:10px 32px 6px}
        .cards-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
        .card-option{display:block;text-decoration:none;color:inherit;background:var(--card);padding:16px 18px;border-radius:16px;border:1px solid rgba(15,23,42,0.06);box-shadow:var(--shadow);transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease;min-height:120px}
        .eyebrow{font-size:12px;color:var(--accent);letter-spacing:.3px;text-transform:uppercase;margin-bottom:8px;font-weight:700}
        .title{font-weight:800;font-size:16px;margin-bottom:4px;letter-spacing:-0.2px}
        .desc{font-size:13px;color:var(--muted);line-height:1.4}
        .pill{display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:12px;background:rgba(10,132,255,0.14);color:var(--accent);font-weight:800;margin-bottom:8px}
        .card-option.active{border-color:rgba(10,132,255,.4);box-shadow:0 18px 48px rgba(10,132,255,.22);transform:translateY(-3px)}
        .card-option:hover{transform:translateY(-3px);box-shadow:0 18px 44px rgba(15,23,42,0.16)}

        .floating-panel{position:fixed;inset:0;display:grid;place-items:center;z-index:7;visibility:hidden;opacity:0;transition:opacity .2s ease, visibility .2s ease}
        .floating-panel.show{visibility:visible;opacity:1}
        .floating-backdrop{position:absolute;inset:0;background:rgba(15,23,42,0.35);backdrop-filter:blur(10px)}
        .panel{position:relative;background:var(--card);padding:18px 18px 20px;border-radius:18px;box-shadow:0 22px 54px rgba(15,23,42,0.28);border:1px solid rgba(15,23,42,0.08);width:480px;max-width:92vw;max-height:82vh;overflow:auto;animation:pop .22s ease}
        @keyframes pop{from{transform:translateY(12px) scale(.97);opacity:0;}to{transform:none;opacity:1;}}
        .panel h2{margin:0 0 10px;padding-right:40px}
        .fields{display:grid;gap:10px}
        label{font-weight:700;font-size:14px;color:var(--text)}
        input,textarea{width:100%;padding:12px;border-radius:12px;border:1px solid rgba(15,23,42,0.08);background:#f9fafb;color:var(--text);box-sizing:border-box}
        input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(10,132,255,0.16)}
        .run{margin-top:12px;padding:12px 16px;border-radius:14px;border:none;background:linear-gradient(120deg,#0a84ff,#34d399);color:white;cursor:pointer;font-weight:800;letter-spacing:-0.1px;box-shadow:0 12px 24px rgba(10,132,255,0.28)}
        .result-card{position:relative;margin-top:14px;padding:14px;border-radius:16px;background:radial-gradient(circle at 20% 20%, rgba(10,132,255,0.12), transparent 35%),
                      radial-gradient(circle at 80% 0%, rgba(52,211,153,0.12), transparent 40%), var(--card);
            border:1px solid rgba(15,23,42,0.06);box-shadow:0 16px 40px rgba(15,23,42,0.16);overflow:hidden}
        .result-card::after{content:"";position:absolute;inset:0;background:linear-gradient(120deg,transparent,rgba(255,255,255,0.4),transparent);opacity:0;transform:translateX(-40%);animation:shine 6s infinite}
        @keyframes shine{0%{opacity:0;transform:translateX(-60%)}10%{opacity:0.6;}25%{opacity:0;transform:translateX(80%)}100%{opacity:0}}
        #output{position:relative;background:rgba(248,250,252,0.9);border:1px solid rgba(15,23,42,0.06);padding:12px;border-radius:12px;min-height:120px;max-height:50vh;overflow:auto;box-shadow:inset 0 1px 0 rgba(255,255,255,0.4)}
        .result-table{width:100%;border-collapse:collapse;margin-top:8px}
        .result-table td{padding:10px 10px;border-bottom:1px solid rgba(15,23,42,0.06)}
        .result-table tr:nth-child(even){background:rgba(10,132,255,0.04)}
        h3{margin:12px 0 6px}
        .text-result{white-space:pre-wrap}
        .meta{color:var(--muted);font-size:13px}

        .panel-close{position:absolute;top:12px;right:12px;border:none;background:rgba(15,23,42,0.06);border-radius:10px;padding:6px 10px;cursor:pointer;color:var(--text);font-weight:700}

        .overlay{position:fixed;inset:0;background:rgba(15,23,42,0.35);backdrop-filter:blur(8px);display:grid;place-items:center;z-index:6;transition:opacity .18s ease, visibility .18s ease}
        .overlay.hidden{opacity:0;visibility:hidden}
        .overlay-card{background:var(--card);padding:20px;border-radius:18px;box-shadow:0 20px 48px rgba(15,23,42,0.2);min-width:260px;max-width:360px;text-align:left;border:1px solid rgba(15,23,42,0.08)}
        .overlay-actions{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}

        @media(max-width:900px){
            .hero{grid-template-columns:1fr;}
            .hero-visual{height:200px}
            .panel{width:auto;max-width:92vw;max-height:78vh}
        }
    </style>
    <script>
        document.addEventListener('DOMContentLoaded', ()=>{
            // Mantener compatibilidad JS mínima — no necesaria para funcionar server-side
            function noop(){return}
            // Parallax suave para blobs (cinematica)
            document.addEventListener('mousemove', (e)=>{
                const { innerWidth: w, innerHeight: h } = window;
                const dx = (e.clientX - w/2) / w;
                const dy = (e.clientY - h/2) / h;
                document.querySelectorAll('.blob').forEach((b, idx)=>{
                    const amp = 12 + idx*6;
                    b.style.transform = `translate(${dx*amp}px, ${dy*amp}px)`;
                });
            });

            const overlay = document.getElementById('overlay');
            const ovTitle = document.getElementById('ov-title');
            const ovDesc = document.getElementById('ov-desc');
            const ovEyebrow = document.getElementById('ov-eyebrow');
            const ovPill = document.getElementById('ov-pill');
            const ovGo = document.getElementById('ov-go');
            const ovClose = document.getElementById('ov-close');
            const floating = document.getElementById('floating-panel');
            const floatingClose = document.getElementById('panel-close');
            const floatingBackdrop = document.getElementById('floating-backdrop');
            const weatherBadge = document.getElementById('weather');
            const weatherCity = document.getElementById('weather-city');
            const weatherMain = document.getElementById('weather-main');
            const weatherCond = document.getElementById('weather-cond');
            const weatherMeta = document.getElementById('weather-meta');
            const forecastBox = document.getElementById('forecast');
            let targetHref = null;

            document.querySelectorAll('.card-option').forEach((card, idx)=>{
                card.addEventListener('click',(e)=>{
                    e.preventDefault();
                    targetHref = card.dataset.href;
                    ovTitle.textContent = card.dataset.title || '';
                    ovDesc.textContent = card.dataset.desc || '';
                    ovEyebrow.textContent = 'Ejercicio ' + (idx+1);
                    ovPill.textContent = card.querySelector('.pill')?.textContent || '';
                    overlay?.classList.remove('hidden');
                });
            });
            ovClose?.addEventListener('click',()=>overlay?.classList.add('hidden'));
            ovGo?.addEventListener('click',()=>{ if(targetHref){ window.location.href = targetHref; overlay?.classList.add('hidden'); }});
            overlay?.addEventListener('click',(e)=>{ if(e.target === overlay){ overlay.classList.add('hidden'); }});

            const showFloating = ()=>{ floating?.classList.add('show'); };
            const hideFloating = ()=>{ floating?.classList.remove('show'); };

            // Mantener visible al cargar si existe
            showFloating();

            floatingClose?.addEventListener('click', hideFloating);
            floatingBackdrop?.addEventListener('click', hideFloating);

            const describeWeather = (code)=>{
                const map = {0:'Despejado',1:'Soleado',2:'Parcial',3:'Nublado',45:'Niebla',48:'Niebla',51:'Llovizna',53:'Llovizna',55:'Llovizna',61:'Lluvia',63:'Lluvia',65:'Lluvia',71:'Nieve',73:'Nieve',75:'Nieve',95:'Tormenta',96:'Tormenta',99:'Tormenta'};
                return map[code] || 'Clima';
            };

            const renderForecast = (daily)=>{
                if(!forecastBox || !daily){return;}
                const days = Math.min(daily.time?.length || 0, 5);
                let html = '';
                for(let i=0;i<days;i++){
                    const label = i === 0 ? 'Hoy' : new Date(daily.time[i]).toLocaleDateString(undefined,{weekday:'short'});
                    const desc = describeWeather(daily.weather_code?.[i]);
                    const tmin = daily.temperature_2m_min?.[i];
                    const tmax = daily.temperature_2m_max?.[i];
                    const precip = daily.precipitation_probability_max?.[i];
                    html += `<div class="forecast-card"><div>${label}</div><div>${desc}</div><div class="temp">${Math.round(tmin)}° / ${Math.round(tmax)}°</div><div class="prec">${precip !== undefined ? precip + '% lluvia' : ''}</div></div>`;
                }
                forecastBox.innerHTML = html;
            };

            const renderMeta = ({hum, wind})=>{
                if(!weatherMeta){return;}
                const pills = [];
                if(hum !== undefined){pills.push(`<span class="meta-pill">Humedad ${hum}%</span>`);}
                if(wind !== undefined){pills.push(`<span class="meta-pill">Viento ${Math.round(wind)} km/h</span>`);}
                weatherMeta.innerHTML = pills.join('');
            };

            const renderCurrent = ({city,country,temp,code,hum,wind,lat,lon})=>{
                if(weatherBadge){ weatherBadge.textContent = 'Clima'; }
                const fallbackLoc = (lat !== undefined && lon !== undefined) ? `Lat ${lat.toFixed(2)}, Lon ${lon.toFixed(2)}` : 'Tu ubicación';
                if(weatherCity){ weatherCity.textContent = `${city || fallbackLoc}${country ? ' · ' + country : ''}`; }
                if(weatherMain && temp !== undefined && code !== undefined){
                    weatherMain.textContent = `${temp.toFixed(1)}°C`;
                }
                if(weatherCond && code !== undefined){
                    weatherCond.textContent = describeWeather(code);
                }
                renderMeta({hum, wind});
            };

            const setUnavailable = (msg)=>{
                if(weatherBadge){ weatherBadge.textContent = msg || 'Clima no disponible'; }
                if(weatherMain){ weatherMain.textContent = msg || 'Clima no disponible'; }
            };

            const fetchWeather = (latitude, longitude)=>{
                const url = `/api/weather?lat=${latitude}&lon=${longitude}`;
                fetch(url).then(r=>{ if(!r.ok) throw new Error('http '+r.status); return r.json(); }).then((payload)=>{
                    if(payload?.error){
                        console.error('Backend clima', payload.error);
                        setUnavailable('Clima no disponible');
                        return;
                    }
                    const temp = payload?.current?.temperature_2m;
                    const code = payload?.current?.weather_code;
                    const hum = payload?.current?.relative_humidity_2m;
                    const wind = payload?.current?.wind_speed_10m;
                    if(temp === undefined || code === undefined){
                        setUnavailable('Clima no disponible');
                        return;
                    }
                    renderCurrent({
                        city: payload?.city || 'Tu ubicación',
                        country: payload?.country || '',
                        lat: payload?.lat,
                        lon: payload?.lon,
                        temp, code, hum, wind
                    });
                    renderForecast(payload?.daily);
                }).catch((err)=>{
                    console.error('Error al obtener clima', err);
                    setUnavailable('Clima no disponible');
                });
            };

            const fallbackLat = 19.4326; // CDMX
            const fallbackLon = -99.1332;

            if(weatherBadge && navigator.geolocation){
                navigator.geolocation.getCurrentPosition(pos=>{
                    const { latitude, longitude } = pos.coords;
                    fetchWeather(latitude, longitude);
                }, ()=>{
                    weatherBadge.textContent = 'Clima';
                    fetchWeather(fallbackLat, fallbackLon);
                });
            }else if(weatherBadge){
                weatherBadge.textContent = 'Clima';
                fetchWeather(fallbackLat, fallbackLon);
            }
        });
    </script>
</head>
<body>
    <div class="cinema">
        <div class="blob b1"></div>
        <div class="blob b2"></div>
        <div class="blob b3"></div>
        <div class="spinner"><div class="ring"></div></div>
    </div>
    <header>
        <div class="brand">Ejercicio · 10 </div>
        <div><a class="logout-chip" href="{{ url_for('logout') }}"><span class="logout-icon">×</span><span class="logout-label">Cerrar sesión</span></a></div>
    </header>

    <section class="hero">
        <div>
            <div class="chip">Alan Alfonso Contreras Montalvo</div>
            <h1>Elige un ejercicio y ejecútalo al instante</h1>
            <p>Cards ordenadas, sombras suaves y una sensación ligera tipo iOS. Selecciona cualquier ejercicio para ver sus campos y resultados en vivo.</p>
            <a href="#seleccion" class="cta">Ver opciones</a>
        </div>
        <div class="hero-visual">
            <div class="badge" id="weather">Clima</div>
            <div class="weather-card">
                <div class="weather-city" id="weather-city">Clima</div>
                <div class="weather-main"><span id="weather-main">—</span><span class="weather-cond" id="weather-cond"></span></div>
                <div class="weather-meta" id="weather-meta"></div>
                <div class="forecast" id="forecast"></div>
            </div>
        </div>
    </section>

    <section class="cards-wrapper" id="seleccion">
        <div class="cards-grid">
            {%- for i, item in ejercicios.items() %}
                <a href="{{ url_for('dashboard', ej=i) }}" class="card-option {{ 'active' if i==selected else '' }}" data-title="{{ item.title }}" data-desc="{{ item.desc }}" data-href="{{ url_for('dashboard', ej=i) }}">
                    <div class="pill">{{ i }}</div>
                    <div class="eyebrow">Ejercicio {{ i }}</div>
                    <div class="title">{{ item.title }}</div>
                    <div class="desc">{{ item.desc }}</div>
                </a>
            {%- endfor %}
        </div>
    </section>

    <div id="overlay" class="overlay hidden">
        <div class="overlay-card">
            <div class="pill" id="ov-pill"></div>
            <div class="eyebrow" id="ov-eyebrow"></div>
            <div class="title" id="ov-title"></div>
            <div class="desc" id="ov-desc"></div>
            <div class="overlay-actions">
                <button id="ov-go" class="run" type="button">Ir a esta opción</button>
                <button id="ov-close" class="chip" type="button" style="border:none">Cerrar</button>
            </div>
        </div>
    </div>

    <div class="floating-panel show" id="floating-panel">
        <div class="floating-backdrop" id="floating-backdrop"></div>
        <div class="panel">
            <button class="panel-close" type="button" id="panel-close">×</button>
            <h2>{{ ejercicios[selected].title }}</h2>
            <form method="post" action="{{ url_for('dashboard') }}">
                <input type="hidden" name="ej" value="{{ selected }}">
                <div class="fields">
                    {%- for f in ejercicios[selected].fields %}
                        <label for="{{ f.name }}">{{ f.label }}</label>
                        <input id="{{ f.name }}" name="{{ f.name }}" type="{{ f.type }}" value="{{ request_values.get(f.name,'') }}">
                    {%- endfor %}
                </div>
                <button class="run" type="submit">Ejecutar</button>
            </form>
            <div class="result-card">
                <div class="eyebrow">Resultado</div>
                <div id="output">{{ result_html|safe }}</div>
            </div>
        </div>
    </div>
</body>
</html>
"""


# --- funciones adaptadas desde tu Ejercicio_7 (sin inputs interactivos) ---
def mostrar_palabra_10_veces_web(palabra: str):
    return "\n".join([palabra] * 10)


def edad_list(edad: int):
    return [i for i in range(1, int(edad) + 1)]


def numero_impares_list(n: int):
    return [i for i in range(1, int(n) + 1, 2)]


def cuenta_atras_list(n: int):
    n = int(n)
    return list(range(n, -1, -1))


def invertir_calc(capital, interes, anos):
    try:
        capital = float(capital)
        interes = float(interes)
        anos = int(anos)
    except Exception:
        return "Entrada inválida"
    final = capital * ((1 + interes / 100) ** anos)
    return f"{final:.2f}"


def triangulo_lines(rango: int):
    r = int(rango)
    return "\n".join(["*" * i for i in range(1, r + 1)])


def tabla_multiplicar_text():
    lines = []
    for i in range(1, 11):
        lines.append(f"Tabla del {i}:")
        for j in range(1, 11):
            lines.append(f"{i} x {j} = {i * j}")
    return "\n".join(lines)


def piramide_numeros_text(numero: int):
    numero = int(numero)
    lines = []
    for i in range(1, numero + 1):
        lines.append(' '.join(str(j) for j in range(2 * i - 1, 0, -2)))
    return "\n".join(lines)


def contrasena_check(original: str, intento: str):
    return "correcto" if intento == original else "incorrecto"


def es_primo(n: int):
    n = int(n)
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def letras_reverse(palabra: str):
    return "\n".join(list(palabra[::-1]))


def contar_letra(frase: str, letra: str):
    return frase.count(letra)


# ---- Nuevos ejercicios solicitados ----
def clasificar_numero_web(valor):
    try:
        numero = int(valor)
    except (TypeError, ValueError):
        return "Error: Debes ingresar un número entero válido."
    partes = []
    partes.append("Cero" if numero == 0 else ("Positivo" if numero > 0 else "Negativo"))
    if numero != 0:
        partes.append("Par" if numero % 2 == 0 else "Impar")
    return " | ".join(partes)


def categoria_edad_web(valor):
    try:
        edad = int(valor)
    except (TypeError, ValueError):
        return "Error: Edad inválida."
    return "Niñez" if edad < 13 else ("Adolescencia" if edad < 18 else "Adultez")


def calcular_tarifa_web(edad, dia, es_estudiante, es_miembro, metodo_pago):
    base = 200
    try:
        edad = int(edad)
        dia = int(dia)
    except (TypeError, ValueError):
        return "Error: Edad o día inválidos."

    es_est = str(es_estudiante).strip().lower() == "si"
    es_memb = str(es_miembro).strip().lower() == "si"
    metodo = str(metodo_pago).strip().upper()

    if not (0 <= edad <= 120) or dia not in range(1, 8):
        return "Error: Edad (0-120) o día (1-7) fuera de rango."

    recargo = base * 0.10 if dia in (6, 7) else 0
    descuentos = [
        50 if edad <= 12 else 20 if edad <= 17 else 30 if edad >= 65 else 0,
        15 if es_est and edad >= 13 else 0,
        10 if es_memb else 0,
        5 if metodo == "E" else 0,
    ]
    total_descuento = min(sum(descuentos), 60)
    total_final = base + recargo - (base * total_descuento / 100)

    return {
        "base": base,
        "recargo": recargo,
        "total_descuento": total_descuento,
        "total_final": total_final,
    }


# Proxy para evitar CORS en peticiones a Open-Meteo
@app.route("/api/weather")
def api_weather():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)
    if lat is None or lon is None:
        return jsonify({"error": "missing lat/lon"}), 400

    base = "https://api.open-meteo.com/v1/forecast"
    geo_base = "https://geocoding-api.open-meteo.com/v1/reverse"
    params_forecast = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code,precipitation_probability_max",
        "timezone": "auto",
    }
    params_geo = {"latitude": lat, "longitude": lon, "count": 1}

    try:
        resp_forecast = requests.get(base, params=params_forecast, timeout=8)
        resp_forecast.raise_for_status()
    except requests.RequestException as exc:
        return jsonify({"error": f"forecast: {exc}"}), 502

    data = resp_forecast.json()

    city = None
    country = None
    try:
        resp_geo = requests.get(geo_base, params=params_geo, timeout=5)
        resp_geo.raise_for_status()
        geo = resp_geo.json()
        if isinstance(geo, dict):
            first = (geo.get("results") or [{}])[0] if geo.get("results") else {}
            city = first.get("name")
            country = first.get("country_code")
    except requests.RequestException:
        # Silently ignore geo failures; return forecast only
        pass

    return jsonify({
        "city": city,
        "country": country,
        "lat": lat,
        "lon": lon,
        "current": data.get("current") if isinstance(data, dict) else None,
        "daily": data.get("daily") if isinstance(data, dict) else None,
    })


def eco_one(palabra: str):
    return palabra


@app.route('/api/ejercicio', methods=['POST'])
def api_ejercicio():
    data = request.get_json() or request.form
    try:
        ej = int(data.get('ej', 0))
    except Exception:
        return {"error": "ej inválido"}, 400

    if ej == 1:
        return {"result": clasificar_numero_web(data.get('numero', 0))}
    if ej == 2:
        return {"result": categoria_edad_web(data.get('edad', 0))}
    if ej == 3:
        return {"result": calcular_tarifa_web(
            data.get('edad', 0),
            data.get('dia', 0),
            data.get('es_estudiante', ''),
            data.get('es_miembro', ''),
            data.get('metodo_pago', ''),
        )}

    return {"error": "Ejercicio no implementado"}, 400


@app.route('/', methods=['GET','POST'])
def login():
        if request.method == 'POST':
                usuario = request.form.get('usuario','').strip()
                contrasena = request.form.get('contrasena','').strip()
                if usuario == USUARIO and contrasena == CONTRASENA:
                        session['autenticado'] = True
                        return redirect(url_for('dashboard'))
                return render_template_string(LOGIN_HTML, error='Usuario o contraseña incorrectos.')
        return render_template_string(LOGIN_HTML, error=None)


def render_result_html(ej, result):
    if result is None:
        return '<div class="meta">Resultados aparecerán aquí...</div>'
    if ej == 7 and isinstance(result, str):
        tables = [t for t in result.split('Tabla del ') if t.strip()]
        html = ''
        for t in tables:
            parts = [p for p in t.split('\n') if p.strip()]
            title = parts[0].replace(':', '').strip()
            html += f'<h3>Tabla del {title}</h3><table class="result-table"><tbody>'
            for line in parts[1:]:
                left_right = line.split('=')
                left = left_right[0].strip() if len(left_right) > 0 else ''
                right = left_right[1].strip() if len(left_right) > 1 else ''
                html += f'<tr><td>{left}</td><td>{right}</td></tr>'
            html += '</tbody></table>'
        return html

    if isinstance(result, (list, tuple)):
        return '<ul>' + ''.join(f'<li>{r}</li>' for r in result) + '</ul>'

    if isinstance(result, dict) and {'base','recargo','total_descuento','total_final'}.issubset(result.keys()):
        return (
            '<table class="result-table">'
            f'<tr><td>Precio Base</td><td>${result["base"]:.2f}</td></tr>'
            f'<tr><td>Recargos</td><td>${result["recargo"]:.2f}</td></tr>'
            f'<tr><td>Descuento aplicado total</td><td>{result["total_descuento"]:.0f}%</td></tr>'
            f'<tr><td><strong>TOTAL FINAL</strong></td><td><strong>${result["total_final"]:.2f}</strong></td></tr>'
            '</table>'
        )

    if isinstance(result, str):
        return '<div class="text-result">' + result.replace('\n', '<br>') + '</div>'

    import json
    return '<pre>' + json.dumps(result, indent=2, ensure_ascii=False) + '</pre>'


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
        if not session.get('autenticado'):
                return redirect(url_for('login'))

        ejercicios = {
            1: { 'title': 'Clasificar número', 'desc': 'Positivo/Negativo/Par/Impar', 'fields': [ {'name':'numero','label':'Número entero','type':'number'} ] },
            2: { 'title': 'Categoría de edad', 'desc': 'Niñez / Adolescencia / Adultez', 'fields': [ {'name':'edad','label':'Edad','type':'number'} ] },
            3: { 'title': 'Calcular tarifa final', 'desc': 'Pase diario con recargos y descuentos', 'fields': [
                {'name':'edad','label':'Edad (0-120)','type':'number'},
                {'name':'dia','label':'Día de la semana (1=Lun ... 7=Dom)','type':'number'},
                {'name':'es_estudiante','label':'¿Es estudiante? (Si/No)','type':'text'},
                {'name':'es_miembro','label':'¿Es miembro? (Si/No)','type':'text'},
                {'name':'metodo_pago','label':'Método de pago (E/T)','type':'text'},
            ] },
        }

        if request.method == 'POST':
            try:
                selected = int(request.form.get('ej', 1))
            except Exception:
                selected = 1
            request_values = request.form
            ej = selected
            if ej == 1:
                result = clasificar_numero_web(request.form.get('numero',0))
            elif ej == 2:
                result = categoria_edad_web(request.form.get('edad',0))
            elif ej == 3:
                result = calcular_tarifa_web(
                    request.form.get('edad',0),
                    request.form.get('dia',0),
                    request.form.get('es_estudiante',''),
                    request.form.get('es_miembro',''),
                    request.form.get('metodo_pago',''),
                )
            else:
                result = None
        else:
            try:
                selected = int(request.args.get('ej', 1))
            except Exception:
                selected = 1
            request_values = request.args
            result = None

        result_html = render_result_html(selected, result)
        return render_template_string(DASHBOARD_HTML, ejercicios=ejercicios, selected=selected, request_values=request_values, result_html=result_html)


@app.route('/logout')
def logout():
        session.clear()
        return redirect(url_for('login'))


if __name__ == '__main__':
        app.run(debug=True)
