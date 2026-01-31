async function submitLogin() {
    const user = document.getElementById('user').value;
    const pass = document.getElementById('pass').value;
    const msg = document.getElementById('msg');

    const fpPromise = FingerprintJS.load();
    const fp = await fpPromise;
    const result = await fp.get();

    const browserName = navigator.userAgent.includes("Chrome") ? "Chrome" : "Boshqa brauzer";

    try {
        const response = await fetch('http://127.0.0.1:8000/api/login/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                username: user,
                password: pass,
                fingerprint: result.visitorId,
                device_name: browserName
            })
        });

        const data = await response.json();
        msg.innerText = data.message || data.error;
        msg.style.color = response.ok ? "green" : "red";
    } catch (err) {
        msg.innerText = "Xato: Serverga ulanib bo'lmadi";
    }
}