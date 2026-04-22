// --- Neuro-Insulin Sovereignty Logic ---
const canvas = document.getElementById('matrix-canvas');
const ctx = canvas.getContext('2d');

// جعل الكانفاس يملأ الشاشة
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const chars = "0101010101"; // لغة البيانات الثنائية
const fontSize = 16;
const columns = canvas.width / fontSize;
const drops = Array(Math.floor(columns)).fill(1);

let focusLevel = 100;

function drawMatrix() {
    // خلفية شفافة لتعطي تأثير الذيل (Trail)
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = "#00ff41"; // أخضر سيادة النظام
    ctx.font = fontSize + "px monospace";

    for (let i = 0; i < drops.length; i++) {
        const text = chars[Math.floor(Math.random() * chars.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        drops[i]++;
    }
    
    updateFocusUI();
}

function updateFocusUI() {
    const statusBox = document.getElementById('sovereignty-status');
    // محاكاة بسيطة لاستهلاك التركيز (Neuro-Insulin)
    if (Math.random() > 0.98 && focusLevel > 0) focusLevel -= 1; 
    
    if (statusBox) {
        statusBox.innerText = `[✔] Sovereignty: ${focusLevel}%`;
    }
}

setInterval(drawMatrix, 50);

// إعادة ضبط الأبعاد عند تغيير حجم الشاشة
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

