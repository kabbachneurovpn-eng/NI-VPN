function activateSovereignty() {
    const msg = document.getElementById('status-message');
    const gate = document.getElementById('gateway');
    
    msg.innerText = "جاري تفعيل درع التركيز...";
    
    setTimeout(() => {
        gate.style.borderColor = "#fff";
        gate.innerHTML = `
            <h1 style="color: #fff;">تم تفعيل السيادة</h1>
            <p>أنت الآن في منطقة العمل العميق.</p>
            <button class="btn-gate" onclick="location.reload()">إغلاق البوابة</button>
        `;
        console.log("Sovereignty status: FREE & ACTIVE");
    }, 1500);
}

